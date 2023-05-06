from flask import Blueprint, render_template, jsonify

bp = Blueprint("main", __name__, url_prefix="/")


# ---------page routing-----------
@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/mypage")
def mypage():
    return render_template("mypage.html")


@bp.route("/odd")
def odd():
    return render_template("odd.html")


@bp.route("/help")
def help():
    return render_template("index.html")


# ---------json data------------


@bp.route("/test")
def test():
    data = {"test1": [65, 59, 80, 81, 80], "test2": [46, 25, 30]}
    return jsonify(data)
