from flask import Blueprint
from ..controllers.controller_channels import ChannelController

bp_channels = Blueprint('channels', __name__)

bp_channels.route("/", methods= ["GET"]) (ChannelController.get)
bp_channels.route("/<int:channel_id>", methods=["GET"])(ChannelController.get_id)
bp_channels.route("/", methods=["POST"])(ChannelController.create)
bp_channels.route("/<int:channel_id>", methods =["PUT"])(ChannelController.update)
bp_channels.route("/<int:channel_id>", methods= ["DELETE"])(ChannelController.delete)
"""bp_channels.route("<int:channel_id>/messages",methods=["GET"])(ChannelController.get_messages)"""