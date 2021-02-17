from flask import session, render_template, request, abort, flash
from mod_users.forms import LoginForm
from mod_users.models import User
from . import admin
from .utils import admin_only_view


@admin.route('/')
@admin_only_view
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
        # check user
        if not user:
            flash('Incorrect Credentials', category='error')
            return render_template('admin/login.html', form=form)
        # check pass    
        if not user.check_password(form.password.data):
            flash('Incorrect Credentials', category='error')
            return render_template('admin/login.html', form=form)
        # check user  is admin 
        if not user.is_admin():
            flash('Incorrect Credentials', category='error')
            return render_template('admin/login.html', form=form)
        session['email'] = user.email
        session['user_id'] = user.id
        # use maraidb(mysql client and inter password)
        # USE flask_blog;
        #  SELECT id,email,role FROM users;
        # UPDATE users SET role=1 WHERE id=1;
        #   SELECT id,email,role FROM users;
        session['role'] = user.role
        return "Logged in successfully"
    # print(session) 
    # session.get('role')
    if session.get('role') == 1:
        print(session)
        return "You are already logged in"
    # create another user for testing role
    #  flask shell
    #  from mod_users import User 
    #  user=User()
    #  user.email="z@gmail.com"
    # user.set_password('123')
    # db
    #  from app import db
    # db.session.add(user)
    # db.session.commit()
    # exit()
    # flask run 127../admin/login
    # for admin role==1 Logged in successfully
    # for z@gmail.com role!=1 Incorrect Credentials
    return render_template('admin/login.html', form=form)