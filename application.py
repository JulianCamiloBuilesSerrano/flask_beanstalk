
# from flask_configurations  import application, login_manager
from controllers import application
from models import *



@application.route("/")
def main():
    return "main"


    return make_response(jsonify(response_user), 200)
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()