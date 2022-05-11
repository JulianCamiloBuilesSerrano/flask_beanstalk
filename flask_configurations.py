from flask import Flask
from flask_login import LoginManager
from flask_cors import CORS

application = Flask(__name__)
CORS(application, supports_credentials=True)
cors = CORS( resource={ r"/*": { "origins": "*" } } )
login_manager=LoginManager()
login_manager=LoginManager()
login_manager.init_app(application)
application.config["SECRET_KEY"] = "1dafafghsdsf5378167ugfdsasdfghj98797781234741arfcshzgwffzgnssaerASXMHMRMDwefsrvs8945)(/%#"
application.secret_key = "test_secret"