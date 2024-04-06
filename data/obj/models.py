from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base()

class Users(Base):
  __tablename__ = 'users'

  user_id: Mapped[int] = mapped_column(primary_key=True)
  username: Mapped[str] = mapped_column(nullable=False)
  score: Mapped[int] = mapped_column(nullable=False)
  email: Mapped[str] = mapped_column(nullable=False)

  def __repr__(self):
    return f"User(user_id={self.user_id}, username={self.username}, score={self.score}, email={self.email}"

class Deck(Base):
  __tablename__ = 'deck'

  deck_id: Mapped[int] = mapped_column(primary_key=True)
  user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
  deck_score: Mapped[int] = mapped_column(nullable=False)
  deck_name: Mapped[str] = mapped_column(nullable=False)

  def __repr__(self):
    return f"Deck(deck_id={self.deck_id}, user_id={self.user_id}, deck_score={self.deck_score}, deck_name={self.deck_name}"


class Games(Base):
  __tablename__ = 'games'
  
  game_id: Mapped[int] = mapped_column(primary_key=True)
  user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
  deck_id: Mapped[int] = mapped_column(ForeignKey("deck.deck_id"))
  record: Mapped[int] = mapped_column(nullable=False)

  def __repr__(self):
    return f"Games(game_id={self.game_id}, user_id={self.user_id}, deck=id={self.deck_id}, record={self.record}"

class Sessions(Base):
  __tablename__ = 'sessions'

  session_id: Mapped[str] = mapped_column(primary_key=True)
  user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
  created_at: Mapped[str] = mapped_column(nullable=False)

  def __repr__(self):
    return f"Sessions(session_id={self.session_id}, user_id={self.user_id}, created_at={self.created_at})"