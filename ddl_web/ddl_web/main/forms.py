from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired


class Form_create_user(FlaskForm):
    name = StringField('Register your user account:', validators=[DataRequired()])
    submit = SubmitField('Form_create_user')

class Form_query_dataset(FlaskForm):
    name = StringField('What is your name:', validators=[DataRequired()])
    dataset = StringField('Query dataset:', validators=[DataRequired()])
    submit = SubmitField('Form_query_dataset')

class Form_submit_job(FlaskForm):
    name = StringField('What is your name:', validators=[DataRequired()])
    #job_code = StringField('submit your code:', validators=[DataRequired()])
    job_code = FileField('Upload Case', validators=[FileRequired(), DataRequired()])
    submit = SubmitField('Form_submit_job')

class Form_query_job(FlaskForm):
    name = StringField('What is your name:', validators=[DataRequired()])
    job_id = StringField('query job (input job id):', validators=[DataRequired()])
    submit = SubmitField('Form_query_job')

class Form_kill_job(FlaskForm):
    name = StringField('What is your name:', validators=[DataRequired()])
    job_id = StringField('kill job (input job id):', validators=[DataRequired()])
    submit = SubmitField('Form_kill_job')




