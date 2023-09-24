from flask import Blueprint
from ..controllers.controller_servers import ServerController

bp_servers = Blueprint('servers', __name__)

bp_servers.route("/", method= ["GET"]) (ServerController.get)
bp_servers.route("/<int:server_id>", method=["GET"])(ServerController.get_id)
bp_servers.route("/", method=["POST"])(ServerController.create)
bp_servers.route("/<int:server_id>", method =["PUT"])(ServerController.update)
bp_servers.route("/<int:server_id>", method= ["DELETE"])(ServerController.delete)
bp_servers.route("<int:server_id>/users",method=["GET"])(ServerController.get_users)
bp_servers.route("<int:server_id>/channels",method=["GET"])(ServerController.get_channels)