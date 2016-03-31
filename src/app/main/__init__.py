
from flask import Blueprint

main = Blueprint('main', "spamapp")

from . import views, errors


