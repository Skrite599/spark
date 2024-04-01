from flask import Blueprint, render_template, request

from core.spark import get_decks, get_deck, get_record

views = Blueprint(__name__, "views")


@views.route('/')
def index():

  decks = get_decks({"session-id": "a06e2d2b-2245-4178-b652-720a71b95aa1"})
  decks = decks['decks']

  return render_template('index.html', decks=decks)


@views.route('/create-deck')
def create_deck():

  return render_template('create-deck.html')


@views.route('/deck/<string:deck_id>')
def deck_profile(deck_id):

  deck = get_deck(deck_id)
  record = get_record(request.headers)

  deck['wins'] = record['wins'] if record['wins'] else None
  deck['loss'] = record['loss'] if record['loss'] else None

  return render_template('deck-profile.html')
