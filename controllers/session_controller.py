from flask import current_app, jsonify, make_response, request, session
from flask_login import login_required, login_user, logout_user
from flask_configurations import application,login_manager
from werkzeug.security import check_password_hash
from models import Usuario



@login_manager.user_loader
def load_user(user_name):
    return Usuario.get_user(user_name)

@application.route("/login", methods=["POST"])
def login():

    req_username = request.json["user"]
    req_password = request.json["password"]
    user = Usuario.get_user(req_username)
    
    if user == None:
        return make_response(jsonify("Usuario no existe"), 400)

    if not check_password_hash(user.password, req_password):
        return make_response(jsonify("contraseña incorrecta"), 403)
    current_app.logger.info(f"Usuario {req_username} logueado")
    login_user(user)

    response_user = {'username': user.user, 'id': user.id,
                     "rol":user.type}
    return make_response(jsonify(response_user), 200)

@application.route("/logout", methods=["POST"])
@login_required
def logout():
    current_app.logger.info("Usuario {} deslogueado logueado".format(session["_user_id"]))
    logout_user()
    return make_response(jsonify({"respuesta":"cerrado"}),200)

@application.route("/courses", methods=["GET"])
@login_required
def get_courses(): 

    req_user = request.args.get('user')
    req_user_id = request.args.get('id')

    if req_user == None: 
        return make_response(jsonify('Unathorized request'), 403)

    teacher_courses = Usuario.get_teacher_courses(req_user_id)
    response = []
    for course in teacher_courses:
        courseId = course._asdict().get('id')
        courseName = course._asdict().get('nombre')
        response.append({'courseCode': courseId, 'courseName': courseName})

    return make_response(jsonify(response), 200) 