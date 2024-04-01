class User:

  def __init__(self, user_id, username, score = 0, record = {}) :
      self.user_id = user_id
      self.username = username
      self.score = score
      self.record = record
  
  def set_score(self, score) :
      self.score = score
  
  def set_record(self, record) :
      self.record = record
  
  def get_score(self) :
      return self.score
  
  def get_record(self):
      return self.record
  
  def get_username(self) :
      return self.username
  
  def get_user_id(self) :
      return self.user_id