"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import datetime 
from hashlib import sha256

from project import app,login_manager
from project.forms import LoginForm,CoupSearchForm
from project.models import UserProfile
from flask import render_template, request, redirect, url_for, flash,session
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash
from project.database import *



###
# Routing for your application.
###


@app.route('/',methods=["GET","POST"])
def home():
    loginform=LoginForm()
    if request.method == "POST" and loginform.validate_on_submit():
        username = loginform.username.data
        password = loginform.password.data
          
        hashedpassword= sha256(password.encode('utf-8')).hexdigest()
        user=getuser(username)
        

        if user is not None and  user['Password']==hashedpassword and user['Username']==username:
            realuser = UserProfile(username,password)
            # get user id, load into session
            session['UserID']=user['UserId']
            login_user(realuser)

            print("yes")
            return redirect(url_for('coupsearch'))



        print(username,password)

    return render_template('home.html',form=loginform)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are logged out.', 'warning')
    return redirect(url_for('home'))

@app.route('/coupsearch',methods=["GET","POST"])
@login_required
def coupsearch():
    search=CoupSearchForm()
    if request.method == "POST" and search.validate_on_submit():
        print(search.CouponCode.data)
        couponcode=search.CouponCode.data
        coupons=findcoupon(couponcode)
        print(coupons)
        return render_template('coupsearch.html',coupon=search,coupons=coupons)

	
    return render_template('coupsearch.html',coupon=search)

@app.route('/redeem/<couponId>')
@login_required
def Redeem(couponId):
    Userid=session.get('UserID')
    
    r=redeemcoupon(Userid,couponId)
    print(r)
    return redirect(url_for('coupsearch'))

@app.route('/newcoupon')
@login_required
def NewCoupons():
    """Render the website's about page."""
    return render_template('NewCoupons.html')



@login_manager.user_loader
def load_user(username):
    userlog=getuser(username)
    if userlog:
        user = UserProfile(userlog['Username'],userlog['Password'])
        return user
    return

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
