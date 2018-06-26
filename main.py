
from flask import Flask, request, Markup, render_template,redirect,flash,url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from flask_mail import Mail,Message

app = Flask(__name__)
app.secret_key = 'abhiportfolio'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'handoverabhi@gmail.com'
app.config['MAIL_PASSWORD'] = 'handover'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


class msgform(Form):
      name = TextField('Name')
      email=TextField('Email')
      msg = TextAreaField('Leave Message')
class EmailForm(Form):
    email= TextField("Email",[validators.Required("Recepients Email id"),validators.Email("Enter Email")])      

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
            #Sending an email to myself           
            mail = Mail(app)            
            newmsg = Message('!Sarahah', sender = 'handoverabhi@gmail.com', recipients = ['abhijeetown540@outlook.com'])
            newmsg.html = "<p> Name : " + name + "</p> <br> <p> Email :" + email  + "</p>" + "<br> Message: <p> <b> <i> " + msg + "</b> </i> </p>"
            mail.send(newmsg)
            return redirect(url_for('takeemail'))
         else:
             flash('Email Not correct bro!') 
    return render_template('contact.html',form=form)

@app.route('/takeemail',methods=['GET','POST'])
def takeemail():
     form = EmailForm(request.form)
     
     if request.method == 'POST':
         email=request.form['email']
         print (email)
         if form.validate():
             mail= Mail(app)
             Nmsg = Message('Not Sarahah',sender='handoverabhi@gmail.com',recipients=[email])
             Nmsg.html  = " <b> Thanks for your interest. We are working for you! </b> <br> <i> Abhijeet </i> "
             mail.send(Nmsg)
             Nmsg = Message('People Interested',sender='hanoverabhi@gmail.com',recipients=['abhijeetown540@outlook.com'])
             Nmsg.body = email + "\nHe/she seems to be Interested."
             mail.send(Nmsg)
             return render_template('email.html')
         else:
             flash('Email Not correct bro!') 
     return render_template('takeemail.html',form=form)



    


if __name__ == "__main__":
    app.run() 