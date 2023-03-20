from flask import redirect, url_for, request, flash, render_template, session, current_app,abort
from shop import db, app, photos
from shop import bcrypt
from .forms import CustomerRegistrationForm, CustomerLoginForm
from .models import RegisterModel
import secrets, os
from shop import login_manager
from flask_login import login_required, current_user, logout_user, login_user

@app.route('/customer/register', methods=["POST", "GET"])
def register_customer():
    form  = CustomerRegistrationForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        register = RegisterModel(name=form.name.data, username=form.username.data, email=form.email.data,
                password=hash_password, country=form.country.data, state=form.state.data,city=form.city.data,
                address=form.address.data, contact=form.contact.data)
        db.session.add(register)
        db.session.commit()
        flash(f"Welcome:{form.name.data} Thank Your for Registering", 'success')
        return redirect(url_for('login'))
    #abort(500)
    return render_template('customers/register.html', form=form)


@app.route('/customer/login', methods=['GET', "POST"])
def customerLogin():
    form = CustomerLoginForm()
    if form.validate_on_submit():
        user = RegisterModel.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Succesfully Logged in", 'success')
            next = request.args.get('next')
            return redirect(next or url_for('home'))
        flash("Incorrect email or password")
        return redirect(url_for('customerLogin'))
    #abort(501)
    return render_template('customers/login.html', form=form)

@app.route('/500')
def error():
    abort(500)

@app.route('/501')
def error_1():
    abort(501)

@app.route('/403')
def error_2():
    abort(403)

@app.route('/customer/logout')
def customerLogout():
    logout_user()
    return redirect(url_for('customerLogin'))

@app.route('/nosotros')
def nosotros():
    
    return render_template('nosotros.html')

@app.route('/presentation')
def presentation():
    
    return render_template('presentation.html')

@app.route('/developers')
def developers():
    
    return render_template('developers.html')