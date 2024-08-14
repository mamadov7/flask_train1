from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)

####################data-base##################

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///user.db'
app.config['SQLALCHEMY_POOL_RECYCLE'] = 280
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db?check_same_thread=False'

db=SQLAlchemy(app)


class user(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(20))
    lname = db.Column(db.String(20))
    city = db.Column(db.String(20))
    resume = db.Column(db.Text)


with app.app_context():
    db.create_all()






##################app############################

@app.route("/", methods=['POST','GET'])
def index():
    if request.method== 'GET':
        return render_template('index.html')
    elif request.method=='POST':
        fname=request.form.get('first_name')
        lname=request.form.get('last_name')
        city=request.form.get('city')
        resume=request.form.get('resume')


        new_user=user(fname=fname , lname=lname , city=city , resume=resume)

        db.session.add(new_user)
        db.session.commit()
        return render_template('index.html')









@app.route('/show')
def show():
    resumes=user.query.all()
    
    return render_template('show.html', resumes=resumes)


if __name__=='__main__':
    app.run(debug=True)







