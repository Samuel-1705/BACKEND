from flask import Blueprint
from ..controllers.controller_users import UserController

bp_users = Blueprint('users', __name__)

bp_users.route("/", method= ["GET"]) (UserController.get)
bp_users.route("/<int:user_id>", method=["GET"])(UserController.get_id)
bp_users.route("/", method=["POST"])(UserController.create)
bp_users.route("/<int:user_id>", method =["PUT"])(UserController.update)
bp_users.route("/<int:user_id>", method= ["DELETE"])(UserController.delete)
bp_users.route("<int:user_id>/servers",method=["GET"])(UserController.get_server)

 

 
  

 

   

  

