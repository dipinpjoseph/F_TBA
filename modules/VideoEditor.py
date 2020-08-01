from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField

class VidForm(FlaskForm):
    intervals = StringField('Insert the intervals in seconds following the format - start1:end1,start2:end2 etc')
    split_trigger = SubmitField('Start Video Split')
    target_file = FileField('Upload your video here:')
    file_download = StringField()