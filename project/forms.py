from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SelectField,IntegerField
from wtforms.fields.html5 import DateField
from wtforms.fields import html5 as h5fields
from wtforms.widgets import html5 as h5widgets
from wtforms.validators import InputRequired, DataRequired, Email,NumberRange

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


class CoupSearchForm(FlaskForm):
    CouponCode = StringField('Coupon Code ', validators=[InputRequired()])

class MakeCoupon(FlaskForm):
    Value = IntegerField('Coupon Value')
    Expiration_date = DateField('Expiration Date', validators=[DataRequired()],format='%Y-%m-%d')
    Quantity = h5fields.IntegerField(
        "Quantity", widget=h5widgets.NumberInput(min=0, max=50, step=1)
    )

class NewUserForm(FlaskForm):
    First_Name = StringField('First Name',validators=[DataRequired()])
    Last_Name = StringField('Last Name',validators=[DataRequired()])
    Username = StringField('Username',validators=[DataRequired()])
    Password = PasswordField('Password',validators=[DataRequired()])
    VPassword = PasswordField(' Verify Password',validators=[DataRequired()])
