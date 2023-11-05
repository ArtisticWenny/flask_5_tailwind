from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os



app = Flask(__name__)

# Create a SQLite database (you can change this to your specific database)
# DATABASE_URL = "mysql+mysqlconnector://wenny:Cakelover1@34.172.190.54:3306/GCP4b"
DATABASE_URL = 'mysql+pymysql://wenny:Cakelover1@34.172.190.54:3306/GCP4b'

#app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL#
#Base.metadata.bind = app

# Create a SQLAlchemy engine and session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/')
def index():
    # Retrieve data from the database
    patients = session.query(patients).all()
    return render_template('index.html', patients=patients)

if __name__ == '__main__':
    app.run(debug=True)
