from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)




@app.route("/", method=['post','get'])
def index():
    if request.method== 'get':
        pass
    elif request.method=='post':
        pass







