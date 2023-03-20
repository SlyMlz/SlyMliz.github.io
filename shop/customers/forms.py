from wtforms import StringField, TextAreaField, PasswordField, SubmitField, IntegerField, validators, Form, ValidationError
from flask_wtf.file import FileRequired, FileAllowed, FileField
from flask_wtf import FlaskForm
from .models import RegisterModel

class CustomerRegistrationForm(FlaskForm):
    name = StringField('Nombre', [validators.DataRequired()])
    username = StringField('Nombre de usaurio', [validators.DataRequired()])
    email = StringField("Email", validators=[validators.Email(), validators.DataRequired()])
    password = PasswordField('Contraseña', [validators.DataRequired(), validators.EqualTo('confirm', message="Both passwords should match")])
    confirm = PasswordField("Repetir contraseña", [validators.DataRequired()])    
    country = StringField('Pais', [validators.DataRequired()])
    state = StringField('Departamento', [validators.DataRequired()])
    city = StringField('Ciudad', [validators.DataRequired()])
    contact = StringField('Contacto', [validators.DataRequired()])
    address = StringField('Dirección', [validators.DataRequired()])

    profile_image = FileField("Elegir foto", validators=[FileAllowed(['jpg', 'png', 'jpeg'], "Images only")])
    
    submit = SubmitField("Registrar")

    def validate_username(self, username):
        if RegisterModel.query.filter_by(username=username.data).first():
            raise ValidationError("Nombre de usuario ya existe.")

    def validate_email(self, email):
        if RegisterModel.query.filter_by(email=email.data).first():
            raise ValidationError("Correo electronico ya existe.")

class CustomerLoginForm(FlaskForm):
    email = StringField("Email", validators=[validators.Email(), validators.DataRequired()])
    password = PasswordField('Contraseña', [validators.DataRequired()])