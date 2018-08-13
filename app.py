
from flask import Flask, render_template, url_for, redirect, request, session
from flask import session as login_session
from databases import *
from user_DB import *
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/add_event',  methods=['GET', 'POST'])
def add_event_route():
    if(request.method == 'GET'):
        return render_template("add.html")
    else:                                                          
        ev_name = request.form['event_name']
        ev_loction = request.form['event_location']
        ev_description = request.form['event_description']
        ev_topic = request.form['event_topic']
        age_limit = request.form['age_limit']
        add_event(ev_name, ev_topic, ev_location , ev_description , age_limit)
        return render_template("add_event.html")

    
@app.route('/',  methods=['GET', 'POST'])
def add_user_route():
    if(request.method == 'GET'):
        return render_template("add.html")
    else:                                                          
        us_name = request.form['user_name']
        us_loction = request.form['user_location']
        us_age = request.form['user_age']
        add_user(us_name,us_age,us_location)
        login_session['id']=user.id
    
        return render_template("home.html")


# del login_session['id']

if __name__ == "__main__":
    app.run(debug=True)
