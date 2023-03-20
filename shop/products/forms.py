from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import Form,StringField, IntegerField, BooleanField, TextAreaField, validators, DecimalField

class AddProducts(Form):
    name = StringField("Name", [validators.DataRequired()])
    price = IntegerField("Precio ", [validators.DataRequired()])
    stock = IntegerField("Stock", [validators.DataRequired()])
    desc = TextAreaField("Description", [validators.DataRequired()])
    # colors = TextAreaField("Colors", [validators.DataRequired()])
    image_1 = FileField('image_1', validators=[FileAllowed(['jpg'], 'JPEG images only!')])
                        