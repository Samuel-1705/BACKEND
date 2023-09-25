from flask import Blueprint
from ..controllers.controller_messages import MessageController

bp_messages= Blueprint('messages', __name__)

bp_messages.route("/", methods= ["GET"]) (MessageController.get)
bp_messages.route("/<int:message_id>", methods=["GET"])(MessageController.get_id)
bp_messages.route("/", methods=["POST"])(MessageController.create)
bp_messages.route("/<int:message_id>", methods= ["DELETE"])(MessageController.delete)