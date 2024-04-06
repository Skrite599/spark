from data.obj.models import Users, Sessions, Deck, Games


def insert_user(username, email, session):

  user = None

  try:
    user = Users(username=username, email=email)
    session.add(user)
    session.commit()
  except Exception as e:
    print(f"Error occurred: {e}")
    session.rollback()

  return user.user_id if user else None


def insert_deck(deck_name, deck_score, user_id, session):

  deck = None

  try:
    deck = Deck(deck_name=deck_name, deck_score=deck_score, user_id=user_id)

    session.add(deck)

    session.commit()

  except Exception as e:
    print(f"Error occurred: {e}")
    session.rollback()

  return deck.deck_id if deck else None


def insert_game(user_id, deck_id, record, session):

  game = None

  try:
    game = Games(user_id=user_id, deck_id=deck_id, record=record)

    session.add(game)

    session.commit()

  except Exception as e:
    print(f"Error occurred: {e}")
    session.rollback()

  return game.game_id if game else None


def insert_session(session_id, user_id, session):

  session_token = None

  try:
    session_token = Sessions(session_id=session_id, user_id=user_id)

    session.add(session_token)

    session.commit()

  except Exception as e:
    print(f"Error occurred: {e}")
    session.rollback()

  return session_token.session_id if session_token else None
