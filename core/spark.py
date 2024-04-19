from data.obj.db import SparkSession
from data.write import insert_user, insert_deck, insert_game, insert_session, insert_card
from data.read import get_user_id, get_decks as get_decks_from_db, get_deck as get_deck_from_db, get_record as get_record_from_db, get_users_from_db, get_user_from_db

import requests
import json


def create_user(user_data):
  response = {}
  session = SparkSession()
  opened_session = session.open_session()
  username = user_data.get('username')
  email = user_data.get('email')
  user = insert_user(username, email, opened_session)
  if not user:
    response = {
      'status': 'error',
      'message': 'user fail to create'
    }
  else:
    response = {
      'status': 'success',
      'message': 'user created successfuly',
      'user_id': user,
      'username': username
    }
  session.close_session()
  return response

def process_deck(deck_list):
  cards = []
  card = {}
  for line in deck_list:
    qty = int(line[0:1])
    line = line[2:]
    name = ''
    for char in line:
      if char == '(':
        break
      if char != ' ':
        name += char
    oracle_id = get_oracle_id(name)
    card = {
      'qty': qty,
      'oracle_id': oracle_id
    }
    cards.append(card)
    return cards


def create_deck(deck_data, user_id):
  response = {}
  session = SparkSession()
  opened_session = session.open_session()
  deck_name = deck_data['deck_name']
  deck_score = deck_data['deck_score']
  deck_cards = process_deck(deck_data['deck_list'])

  # deck_id = insert_deck(deck_name,deck_score, deck_cards, user_id, opened_session)

  # if deck_id:
  #   response = {
  #       'status': 'success',
  #       'message': 'Deck created successfully',
  #       'deck_id': deck_id
  #   }
  # else:
  #   response = {'status': 'error', 'message': 'Deck creation failed'}
  # session.close_session()
  # return response


def submit_game(game_data, user_id):
  response = {}
  session = SparkSession()
  opened_session = session.open_session()
  record = game_data.get('record')
  deck_id = game_data.get('deck_name')
  deck_id = deck_id[5:]
  game_id = insert_game(user_id, deck_id, record, opened_session)
  if game_id:
    response = {
        'status': 'success',
        'message': 'Game submitted successfully',
        'game_id': game_id
    }
  else:
    response = {'status': 'error', 'message': 'Game submission failed'}
  session.close_session()
  return response


def login(user_data):
  username = user_data.get('username')
  response = process_login(username)
  return response


def process_login(username):
  session = SparkSession()
  opened_session = session.open_session()
  qry_params = {'username': username}
  user_id = get_user_id(qry_params, opened_session)
  response = {}
  if not user_id:
    response['status'] = 'error'
    response['message'] = 'user does not exist'
  else:
    response['status'] = 'success'
    response['user_id'] = user_id
    response['message'] = 'user logged in'
  session.close_session()
  return response


def get_decks(user_id):
  response = {}
  session = SparkSession()
  opened_session = session.open_session()
  if user_id:
    decks = get_decks_from_db(user_id, opened_session)
    decks_obj = []
    for deck in decks:
      deck_obj = {}
      deck_obj['deck_id'] = deck.deck_id
      deck_obj['deck_name'] = deck.deck_name
      deck_obj['deck_score'] = deck.deck_score
      decks_obj.append(deck_obj)
    response = {'status': 'success', 'decks': decks_obj}
  else:
    response = {
        'status': 'error',
        'message': 'Something went wrong'
    }
  session.close_session()
  return response

def get_deck(deck_id):
  response = {}
  session = SparkSession()
  opened_session = session.open_session()
  deck = get_deck_from_db(deck_id, opened_session)
  if deck:
    response = {
      'deck_score': deck.deck_score,
      'deck_name': deck.deck_name
    }
  session.close_session()
  return response

def get_record(deck_id):
  response = {}
  session = SparkSession()
  opened_session = session.open_session()
  if deck_id:
    response = get_record_from_db(deck_id, opened_session)
  session.close_session
  return response

def query_user(userQuery):
  response = {}
  session = SparkSession()
  opened_session = session.open_session()
  if userQuery == '' or userQuery is None:
    response = {
      'status': 'error',
      'message': 'Something went wrong'
    }
    return response
  users = get_users_from_db(userQuery, opened_session)
  if users:
    users_obj = []
    for user in users:
      user_obj = {}
      user_obj['user_id'] = user.user_id
      user_obj['username'] = user.username
      user_obj['score'] = user.score
      users_obj.append(user_obj)
    response = {
      'status': 'success',
      'data': users_obj
    }
  else:
    response = {
      'status': 'error',
      'message': 'Something went wrong'
    }
  session.close_session()
  return response

def get_user(user_id):
  response = {}
  session = SparkSession()
  opened_session = session.open_session()
  user = get_user_from_db(user_id, opened_session)
  if not user:
    response = {
      'status': 'error',
      'message': 'User does not exist'
    }
    session.close_session()
    return response
  response = {
    'status': 'success',
    'data': user
  }
  session.close_session()
  return response

def process_combos():

  # count = 0
  
  # with open("C:/Users/Skrite/Desktop/variants.json", 'r', encoding="utf8") as file:
  #   for line in file:
  #     data = json.loads(line)
  #     variants = data['variants']
  #     for v in variants:
  #       count += 1

  # print(count)

  response = requests.get('https://backend.commanderspellbook.com/features/?limit=100')

  data = response.json()
  while response.status_code == 200:
    if 'results' in data: 
      for result in data['results']:
        combo_result = {}
        combo_result['id'] = result['id']
        combo_result['name'] = result['name']
        print(combo_result)
    if data['next'] is None:
      break
    response = requests.get(data['next'])
    data = response.json()


def process_cards():

  session = SparkSession()
  opened_session = session.open_session()

  with open("C:/Users/Skrite\Desktop/all-cards-20240414212309.json", 'r', encoding="utf8") as file:

    count = 0

    for line in file:
      card = {}
      if count == 0:
        count += 1
      elif count == 456272:
        break
      else:
        line = line[:-2]
        data = json.loads(line)
        if data['legalities']['commander'] == 'legal' and data['lang'] == 'en' and data['set'] != 'sld':
          card['scryfall_id'] = data['id']
          if 'oracle_id' not in data:
            if 'card_faces' in data:
              card['oracle_id'] = data['card_faces'][0]['oracle_id']
          else:
            card['oracle_id'] = data['oracle_id']
          if 'image_uris' not in data:
            if 'card_faces' in data:
              card['image_uris'] = data['card_faces'][0]['image_uris']['png']
          else:
            card['image_uris'] = data['image_uris']['png']
          card['uri'] = data['uri']
          card['name'] = data['name']
          if 'mana_cost' not in data:
            if 'card_faces' in data:
              card['mana_cost'] = data['card_faces'][0]['mana_cost']
          else:
            card['mana_cost'] = data['mana_cost']
          if 'cmc' in data:
            card['cmc'] = data['cmc']
          else:
            card['cmc'] = 0.0
          if 'type_line' not in data:
            if 'card_faces' in data:
              card['type_line'] = data['card_faces'][0]['type_line']
          else:
            card['type_line'] = data['type_line']
          if 'oracle_text' in data:
            card['oracle_text'] = data['oracle_text']
          else:
            card['oracle_text'] = ''
          if 'power' in data:
            card['power'] = data['power']
          else:
            card['power'] = ''
          if 'toughness' in data:
            card['toughness'] = data['toughness']
          else:
            card['toughness'] = ''
          colors = ''
          color = ''
          if 'mana_cost' not in data:
            if 'card_faces' in data:
              colors = data['card_faces'][0]['colors']
          else:
            colors = data['colors']
          for c in colors:
            color += c
          card['colors'] = color

          colors_identity = ''
          color_identity = ''
          if 'color_identity' not in data:
            if 'card_faces' in data:
              colors_identity = data['card_faces'][0]['color_identity']
          else:
            colors_identity = data['color_identity']
          for c in colors_identity:
            color_identity += c
          card['color_identity'] = color_identity
          card['set_name'] = data['set_name']
          card['set'] = data['set']

          print(card)

          insert_card(card, opened_session)
        count += 1

  session.close_session()