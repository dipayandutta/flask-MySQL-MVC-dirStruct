from wtforms import Form , StringField,TextAreaField , PasswordField , validators

class RegisterForm(Form):
    name        = StringField('Name:',[validators.Length(min=1,max=50)])
    username	= StringField('User Name',[validators.Length(min=5,max=20)])
    email       = StringField('E-Mail:',[validators.Length(min=6,max=40)])
    password    = PasswordField('Password',[
        validators.DataRequired(),
        validators.EqualTo('confirm',message="Password Dont match")
    ])
    confirm     = PasswordField('Confirm Password')
     