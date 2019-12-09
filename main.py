import os
from flask import Flask, render_template
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify
from models import table_1
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from contextlib import contextmanager
from flask_bootstrap import Bootstrap

import uuid

@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
    except:
        raise
    finally:
        if session is not None:
            session.close()

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    val = 0
    return render_template('index.html', val=val)



def load_csv(file):
    df = pd.read_csv(file, encoding="shift-jis")
    # df = pd.read_csv(path,encoding="SHIFT-JIS")
    return df



@app.route('/post', methods=['POST'])
def predict_api(): 
    global uuids
    uuids = []
    file = request.files.get('file')
    df = load_csv(file)
    df.to_csv('data/output/csv.csv')
    return df

def insert_table(df):
    for index,row in df.iterrows():
        data = PredictionInputData()
        data.id = str(uuid.uuid1())
        scoped_session.add(data)
        scoped_session.commit()
    print(uuids)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)