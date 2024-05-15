from flask import jsonify,request
from . import user_controller_blueprint
from ..facade import UserFacade

user_facade = UserFacade()

@user_controller_blueprint.route("/users", methods=["GET"])
def get_users():
    users = user_facade.get_all_users()
    return jsonify(users)

@user_controller_blueprint.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = user_facade.get_user_by_id(user_id)

    if user is not None:
        return jsonify(user), 200
    else:
        return jsonify({"message": "Usuario no encontrado"}), 404


@user_controller_blueprint.route("/users", methods=["POST"])
def create_user():
    data = request.json
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({'message': 'Name and email are required fields'}), 400
    
    new_user = user_facade.create_user(name, email)
    return jsonify(new_user), 201
    
@user_controller_blueprint.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    deleted = user_facade.delete_user(user_id)
    if deleted:
        return jsonify(message='User deleted successfully'), 200
    else:
        return jsonify(message='User not found'), 404
    
@user_controller_blueprint.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()  

    if not data:
        return jsonify({"message": "Datos no proporcionados"}), 400

    new_name = data.get("name")
    new_email = data.get("email")

    if not new_name or not new_email:
        return jsonify({"message": "Nombre y correo electrónico son obligatorios"}), 400

    updated_user = user_facade.update_user(user_id, new_name, new_email)
    
    if updated_user:
        return jsonify({"message": "Usuario actualizado exitosamente"}), 200
    else:
        return jsonify({"message": "Usuario no encontrado"}), 404

