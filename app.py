# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session

from flask import session as login_session
from databases import *
from user_DB import *

app = Flask(__name__)

# App routing code here
@app.route('/')
def home():
    return render_template('home.html')



@app.route('/add_event',  methods=['GET', 'POST'])
def add_event_route():
    if(request.method == 'GET'):
        return render_template("add_event.html")
    else:                                                          
        event_name = request.form['event_name']
        event_loction = request.form['event_location']
        event_description = request.form['event_description']
        event_topic = request.form['event_topic']
        age_limit = request.form['age_limit']
        add_event(event_name, event_topic, event_location , event_description , age_limit)
        return render_template("add_event.html")

    
@app.route('/',  methods=['GET', 'POST'])
def add_user_route():
    if(request.method == 'GET'):
        return render_template("add.html")
    else:                                                          
        us_name = request.form['user_name']
        us_loction = request.form['user_location']
        us_age = request.form['user_age']
        user = add_user(us_name,us_age,us_location)
        login_session['name']=user.user_name
        return render_template("home.html")


@app.route('/welcome',methods=['GET','POST'])
def welcome():
    return render_template('welcome.html', interests = ['Music','Poetry','Theatre','Art','Dance','Science','Cooking','Books'])

@app.route('/interest_page/<x>')
def interests(topic):
    return render_template('interest_page.html')



# del login_session['id']


if __name__ == "__main__":
    app.run(debug=True)
    