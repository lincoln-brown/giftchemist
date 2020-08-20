from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import InputRequired, DataRequired, Email

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


class CoupSearchForm(FlaskForm):
    CouponCode = StringField('Coupon Code ', validators=[InputRequired()])
