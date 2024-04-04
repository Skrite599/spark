from flask import Blueprint, render_template, redirect, url_for, session

from core.spark import get_decks, get_deck, get_record

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
  user_id = session['user_id']
  record = get_record(user_id, deck_id)

  deck['win'] = record['win'] if record['win'] else None
  deck['loss'] = record['loss'] if record['loss'] else None

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