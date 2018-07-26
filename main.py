
from flask import Flask, request, Markup, render_template,redirect,flash,url_for,session
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from flask_mail import Mail,Message
from random import randint,seed
import sqlfun as dbhandler




app = Flask(__name__)
app.secret_key = 'abhiportfolio'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
<<<<<<< HEAD
app.config['MAIL_USERNAME'] = '' #confidential
app.config['MAIL_PASSWORD'] = ''  #confidential
=======
app.config['MAIL_USERNAME'] = '' #email
app.config['MAIL_PASSWORD'] =  #password
>>>>>>> 238d3c9781a6521b3d70cb36364042eef006ca6c
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


class msgform(Form):
      name = TextField('Name')
      email=TextField('Email')
      msg = TextAreaField('Leave Message')
class EmailForm(Form):
    email= TextField("Email",[validators.Required("Recepients Email id"),validators.Email("Enter Email")])   
class Verifyform(Form):
      num = TextField('number')
class emailnameform(Form):
      username = TextField('username')
      name= TextField('name')
      email= TextField("Email",[validators.Required("Recepients Email id"),validators.Email("Enter Email")])   




@app.route('/register',methods=['GET','POST'])
def register():
    form = emailnameform(request.form)
    
    
    if request.method == 'POST':
        email=request.form['email']
        name=request.form['name']
        username = request.form['username']

        chk =  dbhandler.checkUserName(username,email,name)
        
        if chk== False:
            flash("User name is not available, Sorry!")
            return render_template('register.html',form=form)
          
        #Generate Unique password
        #Number of digits d
        seed(randint(10,1000))
        d = randint(6,15)
        num=0
        for i in range(d):
            r = randint(1,9)
            num = num*10 + r
        print(num)    
        session['otp'] = str(num)
        #Send this number to the email provided
        mail = Mail(app)            
        newmsg = Message('Verification | !Sarahah', sender = 'handoverabhi@gmail.com', recipients = [email])
        newmsg.html =  " <p> Hey! <b> <i> " +  name + " </i></b>  kindly enter this number to verify your email id </p> <hr> <h2>" + str(num) + "</h2>";    
        mail.send(newmsg)    
        return render_template('verify1.html',name=name,email=email,uname=username)
    else:    
        return render_template('register.html',form=form)    


@app.route('/verify',methods=['GET','POST'])
def verify():
    form = Verifyform(request.form)
    
    chk  = session['otp']    
    num = request.form['otp']
    username = request.form['username']
    email = request.form['email']
    name = request.form['name']

    print(num)
    print(chk)
    print(num==chk)
    if num == chk:
        session.pop('otp',None)
        dbhandler.insertUser(username,email,name)
        return render_template('newuser.html',name=name,uname=username,email=email) 
    else:
        session.pop('otp',None)
        return redirect(url_for('register'))
    session.pop('otp',None)
    return render_template('verify1.html',form=form)    
       

@app.route('/user/<username>',methods=['GET','POST'])
def userprofile(username):
    form = msgform(request.form)
    
    name = dbhandler.getName(username)
    email = dbhandler.getEmail(username)

    if request.method == 'POST':
         
         msg=request.form['msg']
        
         if form.validate():
            #Sending an email        
            mail = Mail(app)            
            newmsg = Message('!Sarahah', sender = 'handoverabhi@gmail.com', recipients = [email])
            newmsg.html = "<br> Message: <p> <b> <i> " + msg + "</b> </i> </p>"
            mail.send(newmsg)
            flash("Message Sent! ")
            return render_template('contact.html',form=form,name=name,uname=username)
         else:
             flash('Email Not correct bro!') 
    return render_template('contact.html',form=form,name=name,uname=username)


@app.route('/',methods=['GET','POST']) 
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
    return render_template('contact.html',form=form,name=name)

   


if __name__ == "__main__":
<<<<<<< HEAD
    app.run()
=======
    app.run() 
>>>>>>> 238d3c9781a6521b3d70cb36364042eef006ca6c
