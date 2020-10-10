from flask import Flask
import sys
import os
from flask import Flask, render_template
from flask_login import LoginManager
from flask_mysqldb import MySQL
from flaskwebgui import FlaskUI #get the FlaskUI class

if getattr(sys, 'frozen', False):                                                                                                                                     
    template_folder = os.path.join(sys._MEIPASS, 'templates') 
    static_folder = os.path.join(sys._MEIPASS, 'static') 

    print(template_folder) 
    print(static_folder) 

    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    app = Flask(__name__)



app.config['SECRET_KEY'] = 'testgZvTtlPtjGRqeMBaLji3HxoKB5EZCsNL'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'GIFTCHEMIST'
app.config['MYSQL_CURSORCLASS']="DictCursor"

# Intialize MySQL
mysql = MySQL()
mysql.init_app(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'home'

from project import views