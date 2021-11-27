from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

from blogex.auth import login_required
from blogex.db import get_db

bp = Blueprint("about", __name__)


@bp.route("/about")
def about():
    return render_template("about/about.html")