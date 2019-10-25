from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
    
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={'autofocus': True, 'placeholder': 'Username'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'placeholder': 'Password'})
    submit = SubmitField('Log In')

    def __str__(self):
        return str(self.username.data) + ' ' + str(self.password.data)