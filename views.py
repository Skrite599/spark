from flask import Blueprint, render_template

from core.spark import get_decks

views = Blueprint(__name__, "views")


@views.route('/')
def index():

  decks = get_decks({"session-id": "a06e2d2b-2245-4178-b652-720a71b95aa1"})
  decks = decks['decks']

  return render_template('index.html', decks=decks)

@views.route('/create-deck')
def create_deck():

  return render_template('create-deck.html')
