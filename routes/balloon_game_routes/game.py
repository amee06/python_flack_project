from flask import Blueprint,session,redirect,render_template,url_for
from database import db,cursor

game_bp = Blueprint("ballon",__name__)

@game_bp.route("/game")
def game_start():
   return render_template("ballon_game/page1.html")