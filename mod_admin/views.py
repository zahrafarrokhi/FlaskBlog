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
            return "Incorrent Credentials", 400
        if not user.check_password(form.password.data):
            return "Incorrent Credentials", 400
        session['email'] = user.email
        session['user_id'] = user.id
        return "Logged in successfully" 
    print(session) 
    # <SecureCookieSession {'csrf_token': 'd36f80594222731588967b204cd4b876d5e0df38', 'email': 'zahrafarrokhi2017@gamil.com', 'name': 'Zahra', 'user_id': 1}>  
    if session.get('email') is not None:
        return "You are already logged in"
    return render_template('admin/login.html', form=form)