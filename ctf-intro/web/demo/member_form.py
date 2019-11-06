from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

class MemberForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={'autofocus': True, 'placeholder': 'Username'})
    cool = SelectField('Cool', choices=[("1", "yes"), ("0", "no")], default="1")
    answers = StringField('Answers', widget=TextArea())
    submit = SubmitField('Search')

    def __str__(self):
        return str(self.username.data) + ' ' + str(self.cool.data)