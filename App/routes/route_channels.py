from flask import Blueprint
from ..controllers.controller_channels import ChannelController

bp_channels = Blueprint('channels', __name__)

bp_channels.route("/", method= ["GET"]) (ChannelController.get)
bp_channels.route("/<int:channel_id>", method=["GET"])(ChannelController.get_id)
bp_channels.route("/", method=["POST"])(ChannelController.create)
bp_channels.route("/<int:channel_id>", method =["PUT"])(ChannelController.update)
bp_channels.route("/<int:channel:id>", method= ["DELETE"])(ChannelController.delete)
bp_channels.route("<int:channel_id>/messages",method=["GET"])(ChannelController.get_messages)