from flask import Flask
from flask_login import LoginManager

application = Flask(__name__)
login_manager=LoginManager()
login_manager.init_app(application)
application.config["SECRET_KEY"] = "1dafafghsdsf5378167ugfdsasdfghj98797781234741arfcshzgwffzgnssaerASXMHMRMDwefsrvs8945)(/%#"
application.secret_key = "test_secret"