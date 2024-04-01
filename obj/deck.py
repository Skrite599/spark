class Deck:

  def __init__(self, deck_id, user_id, score=0, deck_name='default'):
    self.deck_id = deck_id
    self.user_id = user_id
    self.score = score
    self.deck_name = deck_name

  def set_score(self, score):
    self.score = score

  def set_deck_name(self, deck_name):
    self.deck_name = deck_name

  def get_score(self):
    return self.score

  def get_user_id(self):
    return self.user_id

  def get_deck_name(self):
    return self.deck_name

  def get_deck_id(self):
    return self.deck_id
