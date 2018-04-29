from flask import Flask 
from configuration.config import configurations
from flask_mysqldb import MySQL

app = Flask(__name__,template_folder='templates')

app.config['MYSQL_HOST']        = configurations.HOSTNAME
app.config['MYSQL_USER']        = configurations.USERNAME
app.config['MYSQL_PASSWORD']    = configurations.PASSWORD
app.config['MYSQL_DB']          = configurations.DATABASE
app.config['MYSQL_CURSORCLASS'] = configurations.CURSOR_CL

db = MySQL(app)

# import all views
from view.views import *

if __name__ == '__main__':
    app.secret_key = configurations.SECRET_KEY
    app.run()
