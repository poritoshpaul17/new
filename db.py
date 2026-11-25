from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/training"
DATABASE_URL = "postgresql+psycopg2://training_tqc8_user:mGNvU7fUfETMzU7sTd4qIIIEGjvQyayN@dpg-dc36fd3rjlhs73euqnrg-a.oregon-postgres.render.com/training_tqc8"

engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit = False, autoflush= False, bind=engine)
base = declarative_base()
