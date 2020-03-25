from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class GenForm(FlaskForm):
    n_val = IntegerField('No.of Rows', validators=[DataRequired()])
    gen_layout = SubmitField('Generate Layout')

class DetForm(FlaskForm):
    det_cal = SubmitField('Calculate Determinant')


