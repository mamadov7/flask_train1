from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)




@app.route("/", methods=['POST','GET'])
def index():
    if request.method== 'GET':
        return render_template('index.html')
    elif request.method=='POST':
        name=request.form.get('first_name')










if __name__=='__main__':
    app.run(debug=True)







