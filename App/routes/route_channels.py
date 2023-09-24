from flask import Blueprint
from ..controllers.controller_channels import ChannelController

bp_servers = Blueprint('channels', __name__)

bp_servers.route("/", method= ["GET"]) (ChannelController.get)
bp_servers.route("/<int:channel_id>", method=["GET"])(ChannelController.get_id)
bp_servers.route("/", method=["POST"])(ChannelController.create)
bp_servers.route("/<int:channel_id>", method =["PUT"])(ChannelController.update)
bp_servers.route("/<int:channel:id>", method= ["DELETE"])(ChannelController.delete)
bp_servers.route("<int:channel_id>/messages",method=["GET"])(ChannelController.get_messages)