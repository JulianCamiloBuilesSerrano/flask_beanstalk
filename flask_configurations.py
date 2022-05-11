from datetime import timedelta
from flask import Flask
from flask_login import LoginManager
from flask_cors import CORS

application = Flask(__name__)

application.config["SECRET_KEY"] = "1dafafghsdsf5378167ugfdsasdfghj98797781234741arfcshzgwffzgnssaerASXMHMRMDwefsrvs8945)(/%#"
application.secret_key = "test_secret"
application.config["SESSION_TYPE"] = "filesystem"
application.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://admin:tesis2022@database-1-tesis.cbzzayw2ryjl.us-east-1.rds.amazonaws.com/bd_tesis"
application.config["REMEMBER_COOKIE_DURATION"] = timedelta(hours=1)
CORS(application, supports_credentials=True)
cors = CORS( resource={ r"/*": { "origins": "*" } } )
login_manager=LoginManager()
login_manager.init_app(application)
application.config['TESTING'] = False