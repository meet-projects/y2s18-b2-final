# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session

from flask import session as login_session
from databases import *
from user_DB import *

app = Flask(__name__)

app.secret_key = 'super secret key'
# App routing code here
# @app.route('/')
# def home():
#     return render_template('home.html')



@app.route('/add_event',  methods=['GET', 'POST'])
def add_event_route():
    if(request.method == 'GET'):
        return render_template("add_event.html")
    else:                                                          
        event_name = request.form['event_name']
        event_location = request.form['event_location']
        event_description = request.form['event_description']
        event_topic = request.form['topic']
        age_limit = request.form['age_limit']
        add_event(event_name, event_topic, event_location , event_description , age_limit)
        return render_template("add_event.html")

    
@app.route('/',  methods=['GET', 'POST'])
def add_user_route():
    if(request.method == 'GET'):
        return render_template("home.html")
    else:
        us_name = request.form['user_name']
        us_location = request.form['user_location']
        us_age = request.form['user_age']
        user = add_user(us_name,us_age,us_location)
        login_session['name']=us_name
        return redirect("welcome")


@app.route('/welcome',methods=['GET','POST'])
def welcome():
    return render_template('welcome.html', interests = ['Music','Poetry','Theatre','Art','Dance','Science','Cooking','Books' , 'Animals','Movies','Gaming'])

@app.route('/interest_page/<string:topic>')
def interests(topic):
    user  = query_user(login_session['name'])
    events=event_query_by_topiclocation(topic, user.user_location)
    return render_template('interest_page.html', events=events, topic=topic)


@app.route('/contact' , methods=['GET', 'POST'])
def add_complaint():
    if(request.method == 'GET'):
        return render_template("contact.html")
    else:
        ms_name = request.form['massager']
        ms_content = request.form['content']
        return redirect("/")
# del login_session['name']


if __name__ == "__main__":
    app.run(debug=True)
    