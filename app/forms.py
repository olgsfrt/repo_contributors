from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

class RepoForm(FlaskForm):
    repo_url = StringField('Repository URL', validators=[DataRequired(), URL()])
    submit = SubmitField('Submit')
