from flask import Blueprint, render_template, request, redirect,session
from controller.todo_controller import add_todo, get_status, get_todo_by_id, get_todos

r_app = Blueprint('app', __name__)


@r_app.route('/app', methods=['GET',])
def landing():
    if session['user'] == None: return redirect('/')

        
    return render_template('app/app.j2',
                           user=session['user'],
                           todos=get_todos(session['user']['id']))

@r_app.route('/app/todo/<id>', methods=['GET',])
def get_by_id(id: str):
    if session['user'] == None: return redirect('/')
    todos = {}
    try:
        todos = get_todo_by_id(id)
    except TypeError:
        return render_template('app/message.j2',
                               message={
                                   'route': '/app',
                                   'title': 'Todo not found!',
                                   'desc': 'Your todo is not found!'
                                   },)

    return render_template('app/item.j2',
                           user=session['user'],
                           todos=todos,
                           status=get_status())





@r_app.route('/app/todo', methods=['POST',])
def create_todo():
    
    title = request.form.get("title","")
    desc = request.form.get("description", "")

    add_todo(session['user']['id'],title, desc)

    return render_template('app/message.j2',
      message={
        'route': '/app',
        'title': 'Todo Created!',
        'desc': 'Your todo is now saved'
        },)

