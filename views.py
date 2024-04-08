from flask import Blueprint, render_template, session

from core.spark import get_decks, get_deck, get_record, get_user

views = Blueprint(__name__, "views")


@views.route('/')
def index():

  loggedin = False
  decks = []

  if 'user_id' in session:
    user_id = session['user_id']
    loggedin = True
    decks = get_decks(user_id)
    decks = decks['decks']

  return render_template('index.html', decks=decks, loggedin=loggedin)


@views.route('/create-deck')
def create_deck():

  loggedin = False

  if 'user_id' not in session:
    return render_template('index.html')
  
  if 'user_id' in session:
    loggedin = True

  return render_template('create-deck.html', loggedin=loggedin)


@views.route('/deck/<deck_id>')
def deck_profile(deck_id):

  loggedin = False

  deck = get_deck(deck_id)
  record = get_record(deck_id)

  if 'user_id' in session:
    loggedin = True

  deck['win'] = record['win']
  deck['loss'] = record['loss']

  return render_template('deck-profile.html', deck=deck, loggedin=loggedin)

@views.route('/create-game')
def create_game():

  loggedin = False

  if 'user_id' not in session:
    return render_template('index.html')
  
  if 'user_id' in session:
    loggedin = True
  
  user_id = session['user_id']
  decks = get_decks(user_id)
  decks = decks['decks']

  return render_template('create-game.html', decks=decks, loggedin=loggedin)

@views.route('/login')
def login():

  return render_template('login.html')

@views.route('/user/<user_id>')
def user_profile(user_id):

  loggedin = False

  user = get_user(user_id)

  user = user['data']

  if 'user_id' in session:
    loggedin = True

  return render_template('user-profile.html', user=user, loggedin=loggedin)

@views.route('/sign-up')
def sign_up():

  return render_template('sign-up.html')

@views.route('/decks')
def decks_view():

  loggedin = False
  user_id = None

  if 'user_id' in session:
    loggedin = True
    user_id = session['user_id']

  decks = get_decks(user_id)
  decks = decks['decks']

  return render_template('decks.html', loggedin=loggedin, decks=decks)