from flask import Blueprint, render_template, request, redirect, session

from controller.auth import login_user

index = Blueprint('index', __name__)
@index.before_request
def before_request():
    session['user'] = session.get('user',None)
    if session['user'] != None: return redirect('/app')
    


@index.route('/', methods=['GET',])
def landing():
        
    return render_template('index/index.j2',)


@index.route('/auth/login', methods=['POST',])
def login():

    user = request.form.get("username")
    password = request.form.get("password")

    result=login_user(str(user), str(password))
    
    if result == None:
        return render_template('index/login-error.j2',)

    session['user'] = result
    return redirect('/app',)


@index.route('/auth/logout', methods=['POST',])
def logout():
    session['user'] = None
    return redirect('/')
