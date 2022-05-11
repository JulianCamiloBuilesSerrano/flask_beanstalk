from flask import current_app, jsonify, make_response, request, session
from flask_login import login_required
from flask_configurations import application,login_manager
from models import Emocion_x_Estudiante, Usuario
from datetime import datetime

########################################################
# @application.route("/resultado", methods=['GET'])
# @login_required
# def get_resultados():
#     user = Usuario.get_user(session["_user_id"])
#     id_sesion_activa = user.get_actual_sesion_profesor()
#     print("sesion_activa: " , id_sesion_activa)
#     list = []
#     if id_sesion_activa == None:
#         print("NONE")
#         resultado = "No hay sesions activas"
#         info = {'status': 1}
#         list.append(info)
#     else:
#         resultado = Emocion_x_Estudiante.get_emocion_x_estudiante(id_sesion_activa)        
#         for ex in resultado:
#             porcentaje = ex[4] * 100
#             info = { 'emocion_id' : ex[3], 'sesion_id' : ex[1], 'porcentaje': porcentaje, 'estudiante_id' : ex[0], 'fecha' : ex[2], 'status' : 0 }
#             list.append(info)
#             info = {}
#     print("List: ", list)
#     print("resultado: ", resultado)
#     #TO DO... don't duplicate students count
#     return jsonify(list)
########################################################
# @application.route("/info_sesion",methods=["GET"])
# @login_required
# def obtener_info_sesion():
#     id = request.args.get('id')
    
#     try:
#         #La sesión la envía el historial.
#         resultado = Emocion_x_Estudiante.get_emocions_for_sesion(10)
#         current_app.logger.info(f"solicitud de sesion {id}")
#         if len(resultado) == 0:
#             return make_response(jsonify({"error":"no data"}),400)
#         horas =  set()
#         estudiantes = set()
#         data = []
#         for r in resultado:
#             d = {}
#             d["nombre"] = r["name"] + " "+ r["last_name"]
            
#             estudiantes.add(
#                 d["nombre"]
#             )
#             d["emocion"] = r["nombre"]
#             d["fecha"] =  str(r["fecha"])
#             horas.add(str(r["fecha"]))
            
#             data.append(d)
#         horas = list(horas)
#         horas.sort(key= lambda date: datetime.strptime(date, "%Y-%m-%d %H:%M:%S"))
#         print("estudiantes" , estudiantes)
#         response = {
#             "dates" : horas,
#             "data":data,
#             "students": list(estudiantes)
#         }
        
#         return make_response(jsonify(response), 200) 
#     except Exception as err:
#         print("error: ",err)
#         return make_response(jsonify({"error":f"{err}"}),400)
########################################################
# @application.route("/course-sessions", methods=["GET"])
# @login_required
# def get_course_sessions():
#     req_user = request.args.get('user')
#     req_course_id = request.args.get('courseId')

#     if req_user == None: 
#         return make_response(jsonify('Unathorized request'), 403)

#     course_sessions = Usuario.get_course_sessions(req_course_id)

#     response = []
#     for session in course_sessions:
#         class_number = session._asdict().get('clase_id')
#         session_date = datetime.strftime(session._asdict().get('hora_inicio'), '%d/%b/%Y')
#         state = 'Finalizado'
#         session_id = session._asdict().get('sesion_id')
#         response.append({"clase": class_number, "fecha": session_date, "estado": state, "id": session_id})
#     # Eof

#     return make_response(jsonify(response))

########################################################
@application.route("/courses", methods=["GET"])
@login_required
def get_courses(): 

    # req_user = request.args.get('user')
    # req_user_id = request.args.get('id')

    # if req_user == None: 
    #     return make_response(jsonify('Unathorized request'), 403)

    # teacher_courses = Usuario.get_teacher_courses(req_user_id)
    # response = []
    # for course in teacher_courses:
    #     courseId = course._asdict().get('id')
    #     courseName = course._asdict().get('nombre')
    #     response.append({'courseCode': courseId, 'courseName': courseName})

    # return make_response(jsonify(response), 200) 
    return "ss"
# Eod