from flask import Blueprint
from ..controllers.controller_servers import ServerController

bp_servers = Blueprint('servers', __name__)

bp_servers.route("/", methods= ["GET"]) (ServerController.get)
bp_servers.route("/<int:server_id>", methods=["GET"])(ServerController.get_id)
bp_servers.route("/", methods=["POST"])(ServerController.create)
bp_servers.route("/<int:server_id>", methods =["PUT"])(ServerController.update)
bp_servers.route("/<int:server_id>", methods = ["DELETE"])(ServerController.delete)
bp_servers.route("<int:server_id>/users",methods=["GET"])(ServerController.get_users)

"""
bp_servers.route("<int:server_id>/channels",method=["GET"])(ServerController.get_channels)"""