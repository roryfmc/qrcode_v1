from wtforms import Form, StringField, PasswordField, validators
from wtforms.validators import DataRequired


class RegisterForm(Form):

    email = StringField("Email", validators=[validators.Length
                                             (min=7, max=20), validators.DataRequired(message="Please enter your email")])
    password = PasswordField("Password", validators=[validators.DataRequired(message="Please enter your password"),
                                                     validators.EqualTo(fieldname="confirm", message=
                                                     "Your password do not match")])
    confirm = PasswordField("Confirm Password", validators=[validators.DataRequired(message="Please fill this field")])