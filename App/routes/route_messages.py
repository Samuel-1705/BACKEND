from flask import Blueprint
from ..controllers.controller_messages import MessageController

bp_messages= Blueprint('messages', __name__)

bp_messages.route("/", method= ["GET"]) (MessageController.get)
bp_messages.route("/<int:message_id>", method=["GET"])(MessageController.get_id)
bp_messages.route("/", method=["POST"])(MessageController.create)
bp_messages.route("/<int:message_id>", method =["PUT"])(MessageController.update)
bp_messages.route("/<int:message:id>", method= ["DELETE"])(MessageController.delete)