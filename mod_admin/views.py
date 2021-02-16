from flask import session, render_template, request, abort
from mod_users.forms import LoginForm
from mod_users.models import User
from . import admin


@admin.route('/')
def index():
    return "Hello from admin Index"

@admin.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        # print(f"form is validated!{form.validate_on_submit()}")
        # form is validated!True
        if not form.validate_on_submit():
            abort(400)
        user = User.query.filter(User.email.ilike(f'{form.email.data}')).first()
        # print(user)
        # id user in db 
        # <User 1>
        if not user:
            return "Incorrect Credentials", 400
        if not user.check_password(form.password.data):
            return "Incorrect Credentials", 400
        session['email'] = user.email
        session['user_id'] = user.id
        return "Logged in successfully" 
#     print(session) 
   
#     if session.get('email') is not None:
#         return "You are already logged in"
    return render_template('admin/login.html', form=form)
