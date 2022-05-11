
from flask import Flask, current_app, jsonify, make_response, request
from flask_login import LoginManager
from werkzeug.security import check_password_hash
from flask_login import LoginManager
from flask_login import login_user, login_required, logout_user

from models import *
# # print a nice greeting.
# def say_hello(username = "World"):
#     return '<p>Hello %s!</p>\n' % username

# # some bits of text for the page.
# header_text = '''
#     <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
# instructions = '''
#     <p><em>Hint</em>: This is a RESTful web service! Append a username
#     to the URL (for example: <code>/Thelonious</code>) to say hello to
#     someone specific.</p>\n'''
# home_link = '<p><a href="/">Back</a></p>\n'
# footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
application = Flask(__name__)
# login_manager=LoginManager()
# login_manager.init_app(application)
# application.config["SECRET_KEY"] = "1dafafghsdsf5378167ugfdsasdfghj98797781234741arfcshzgwffzgnssaerASXMHMRMDwefsrvs8945)(/%#"
# application.secret_key = "test_secret"
# # add a rule for the index page.
# application.add_url_rule('/', 'index', (lambda: header_text +
#     say_hello() + instructions + footer_text))

# # add a rule when the page is accessed with a name appended to the site
# # URL.
# application.add_url_rule('/<username>', 'hello', (lambda username:
#     header_text + say_hello(username) + home_link + footer_text))

# # run the app.

# @login_manager.user_loader
# def load_user(user_name):
#     return Usuario.get_user(user_name)
@application.route("/")
def main():
    return make_response(jsonify({"respuesta":"hola"}),200)

# @application.route("/login", methods=["POST"])
# def login():

#     req_username = request.json["user"]
#     req_password = request.json["password"]
#     user = Usuario.get_user(req_username)
    
#     if user == None:
#         return make_response(jsonify("Usuario no existe"), 400)

#     if not check_password_hash(user.password, req_password):
#         return make_response(jsonify("contraseña incorrecta"), 403)
#     current_app.logger.info(f"Usuario {req_username} logueado")
#     login_user(user)

#     response_user = {'username': user.user, 'id': user.id,
#                      "rol":user.type}

#     return make_response(jsonify(response_user), 200)
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()