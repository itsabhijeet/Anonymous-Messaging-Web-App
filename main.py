
from flask import Flask, request, Markup, render_template,redirect,flash,url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

app = Flask(__name__)
app.secret_key = 'abhiportfolio'

class msgform(Form):
      name = TextField('Name')
      email=TextField('Email')
      msg = TextAreaField('Leave Message')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/message',methods=['GET','POST']) 
def msg():
    form = msgform(request.form)
     
    if request.method == 'POST':
         name=request.form['name']
         email=request.form['email']
         msg=request.form['msg']
         print(name)
         print (email)
         print(msg)
         if form.validate():
             flash('Recieved :' + name)             
         else:
             flash('Email Not correct bro!') 
    return render_template('contact.html',form=form)

    


if __name__ == "__main__":
    app.run() 