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
