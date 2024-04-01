from data.obj.db import SparkSession
from data.write import insert_user, insert_deck, insert_game, insert_session
from data.read import get_user_id, get_decks as get_decks_from_db, get_deck as get_deck_from_db, get_record as get_record_from_db
import uuid


def create_user(username):
  session = SparkSession()
  opened_session = session.open_session()
  insert_user(username, opened_session)
  session.close_session()


def create_deck(deck_data):
  response = {}
  session = SparkSession()
  opened_session = session.open_session()
  user_id = get_user_id(deck_data.headers, opened_session)
  deck_data = deck_data.form
  deck_name = deck_data['deck_name']
  deck_id = insert_deck(deck_name, user_id, opened_session)
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


def submit_game(game_data):
  response = {}
  session = SparkSession()
  opened_session = session.open_session()
  win = game_data['record']['win']
  loss = game_data['record']['loss']
  deck_id = game_data['deck_id']
  session_id = game_data['session_id']
  qry_params = {'session_id': session_id}
  user_id = get_user_id(qry_params, opened_session)
  game_id = insert_game(user_id, deck_id, win, loss, opened_session)
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
  username = user_data['username']
  session_token = process_login(username)
  return session_token


def process_login(username):
  session = SparkSession()
  opened_session = session.open_session()
  qry_params = {'username': username}
  user_id = get_user_id(qry_params, opened_session)
  response = {}
  if not user_id:
    create_user(username)
    return process_login(username)
  else:
    session_id = str(uuid.uuid4())
    insert_session(session_id, user_id, opened_session)
    response = {'login': 'success', 'session_id': session_id}
  session.close_session()
  return response


def get_decks(session_id):
  response = {}
  session = SparkSession()
  opened_session = session.open_session()
  user_id = get_user_id(session_id, opened_session)
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
        'message': 'Something went wrong',
        'details': str(session_id)
    }
  session.close_session()
  return response

def get_deck(deck_id):
  session = SparkSession()
  opened_session = session.open_session()
  deck = get_deck_from_db(deck_id, opened_session)
  session.close_session()
  return deck

def get_record(session_id):
  response = {}
  session = SparkSession()
  opened_session = session.open_session()
  user_id = get_user_id(session_id, opened_session)
  if user_id:
    response = get_record(user_id, opened_session)
  session.close_session
  return response
  