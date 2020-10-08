from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import db.db_config as cf

engine = create_engine(cf.DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

