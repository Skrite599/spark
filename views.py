from flask import Blueprint, render_template, redirect, url_for, session

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

  if 'user_id' not in session:
    return render_template('index.html')

  return render_template('create-deck.html')


@views.route('/deck/<deck_id>')
def deck_profile(deck_id):

  deck = get_deck(deck_id)
  record = get_record(deck_id)

  print(record)

  deck['win'] = record['win']
  deck['loss'] = record['loss']

  return render_template('deck-profile.html', deck=deck)

@views.route('/create-game')
def create_game():

  if 'user_id' not in session:
    return render_template('index.html')
  
  user_id = session['user_id']
  decks = get_decks(user_id)
  decks = decks['decks']

  return render_template('create-game.html', decks=decks)

@views.route('/login')
def login():

  return render_template('login.html')

@views.route('/user/<user_id>')
def user_profile(user_id):

  user = get_user(user_id)

  user = user['data']

  return render_template('user-profile.html', user=user)

@views.route('/sign-up')
def sign_up():

  return render_template('sign-up.html')