from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class SparkSession:

  def __init__(self):
    self.engine = create_engine(
        "postgresql://neondb_owner:gJP9x6UYSzZc@ep-odd-fire-a5kp7bcr.us-east-2.aws.neon.tech/neondb?sslmode=require&options=project%3Dep-odd-fire-a5kp7bcr"
    )
    self.session = sessionmaker(bind=self.engine)

  def open_session(self):
    self.open_session = self.session()
    return self.open_session

  def close_session(self):
    self.open_session.close()

  def commit(self):
    self.open_session.commit()
