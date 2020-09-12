from flask import Flask,session
app=Flask(__name__)
from check_login import check_logged_in
@app.route('/')
def hello()->str:
    return "this is the first simple Page"

@app.route('/login')
def login()->str:
    session['logged_in']=True
    return "You are logged in"
@app.route('/logout')
def logout()->str:
    if 'logged_in' in session:
        session.pop('logged_in')
    return 'You are logged out'
@app.route('/status')
def status()->str:
    if 'logged_in' in session:
        return 'You are logged in ,Sir'
    return 'Your are not logged in ,Sir'
app.secret_key="EncryptingString"


@app.route('/page1')
@check_logged_in
def page1()->str:
    return 'This is page1'
    


@app.route('/page2')
#This is the custom function decorator
@check_logged_in

def page2()->str:
    return 'This is page2'

@app.route('/page3')
def page3()->str:
    return 'This is page3'

if __name__=='__main__':
    app.run(debug=True)

