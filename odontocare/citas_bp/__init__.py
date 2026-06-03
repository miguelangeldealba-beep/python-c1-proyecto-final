from flask import Blueprint

citas_bp = Blueprint("citas_bp", __name__)

from . import routes