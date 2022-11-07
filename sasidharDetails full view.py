import json
from datetime import datetime
import psycopg2
from flask import Flask, request
from flask_restful import Api
from sqlalchemy import Column, String, Integer, Date, BOOLEAN, and_, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool



app = Flask(__name__)
api = Api(app)
Base = declarative_base()
database_url = "postgresql://postgres:1234@localhost:5432/postgres"
engine = create_engine(database_url, echo=True, poolclass=NullPool)
Session = sessionmaker(bind=engine)
session = Session()

class sasidharFmailyDetails(Base):
    __tablename__ = "sasidhardetails"
    name = Column("name", String)
    age = Column("age", Integer)
    salary = Column("salary", Integer)
    address = Column("address", String)
    mobile = Column("mobile", Integer,primary_key=True)

# http://127.0.0.1:5000/sasidhar/fmaily/details
@app.route('/sasidhar/fmaily/details', methods=['GET'])
def home():
    results = session.query(sasidharFmailyDetails).all()
    results_1 = [item.__dict__ for item in results]
    for item in results_1:
        del item['_sa_instance_state']
    return json.dumps(results_1)
app.run(debug=True)