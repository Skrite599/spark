from data.obj.models import Users, Sessions, Deck, Games, Card


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

def insert_card(card_data, session):

  card = None

  scryfall_id = card_data['scryfall_id']
  oracle_id = card_data['oracle_id']
  image_uri = card_data['image_uris']
  uri = card_data['uri']
  name = card_data['name']
  mana_cost = card_data['mana_cost']
  cmc = card_data['cmc']
  power = card_data['power']
  toughness = card_data['toughness']
  type_line = card_data['type_line']
  oracle_text = card_data['oracle_text']
  colors = card_data['colors']
  color_identity = card_data['color_identity']
  set_name = card_data['set_name']
  set = card_data['set']

  try:
    card = Card(
      scryfall_id=scryfall_id,
      oracle_id = oracle_id,
      image_uri = image_uri,
      uri = uri,
      name = name,
      mana_cost = mana_cost,
      cmc = cmc,
      power = power,
      toughness = toughness,
      type_line = type_line,
      oracle_text = oracle_text,
      colors = colors,
      color_identity = color_identity,
      set_name = set_name,
      set_code = set
    )

    session.add(card)

    session.commit()

  except Exception as e:
    print(f"Error occurred: {e}")
    session.rollback()

  return card.card_id if card else None