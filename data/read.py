from sqlalchemy import func
from data.obj.models import Users, Sessions, Deck, Games


def get_user_id(qry_params, session):

  user = None

  if 'username' in qry_params:
    username = qry_params['username']
    user = session.query(Users).filter_by(username=username).first()
  elif 'session-id' in qry_params:
    session_id = qry_params['session-id']
    user = session.query(Sessions).filter_by(session_id=session_id).first()

  user_id = user.user_id if user else None

  return user_id


def get_session(user_id, session):

  session_token = session.query(Sessions).filter_by(user_id=user_id).first()

  return session_token


def get_deck_id(user_id, deck_name, session):

  deck = session.query(Deck).filter_by(user_id=user_id,
                                       deck_name=deck_name).first()

  deck_id = deck.deck_id if deck else None

  return deck_id


def get_decks(user_id, session):

  decks = session.query(Deck).filter_by(user_id=user_id).all()

  return decks

def get_deck(deck_id, session):

  deck = session.query(Deck).filter_by(deck_id=deck_id).first()

  return deck

def get_record(deck_id, session):

  games = session.query(Games).filter_by(deck_id=deck_id).all()

  win = 0
  loss = 0

  for game in games:
    if not game.record :
      continue
    if game.record > 0 :
      win = win + game.record
    else :
      loss = loss + (game.record * -1)

  return {
      'win': win,
      'loss': loss
  }

def get_users_from_db(userQuery, session):

  users = session.query(Users).filter(Users.username.like(userQuery + '%')).all()

  return users

def get_user_from_db(user_id, session):

  user = session.query(Users).filter(Users.user_id==user_id).first()

  return user