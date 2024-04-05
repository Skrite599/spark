from data.obj.db import SparkSession
from data.write import insert_user, insert_deck, insert_game, insert_session
from data.read import get_user_id, get_decks as get_decks_from_db, get_deck as get_deck_from_db, get_record as get_record_from_db, get_users_from_db, get_user_from_db


def create_user(username):
  session = SparkSession()
  opened_session = session.open_session()
  insert_user(username, opened_session)
  session.close_session()


def create_deck(deck_data, user_id):
  response = {}
  session = SparkSession()
  opened_session = session.open_session()
  deck_name = deck_data.get('deck_name')
  deck_score = 0
  if deck_data.get('deck_score'):
    deck_score = deck_data['deck_score']
  deck_id = insert_deck(deck_name, deck_score, user_id, opened_session)
  if deck_id:
    response = {
        'status': 'success',
        'message': 'Deck created successfully',
        'deck_id': deck_id
    }
  else:
    response = {'status': 'error', 'message': 'Deck creation failed'}
  session.close_session()
  return response


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
    create_user(username)
    response['message'] = 'created user'
    return process_login(username)
  else:
    response['status'] = 'success'
    response['user_id'] = user_id
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
      'message': 'Something went wrong'
    }
    session.close_session()
    return response
  response = {
    'status': 'success',
    'data': user
  }
  session.close_session()
  return response