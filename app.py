from flask import Flask,render_template,request,redirect,url_for,session
from database import db,cursor


import mysql.connector
import os
import random

app = Flask(__name__)

app.secret_key = "my_sec"


from routes.user_routes.registration import user_bp as res_bp
app.register_blueprint(res_bp)

from routes.user_routes.login import user_bp as login_bp
app.register_blueprint(login_bp)

from routes.user_routes.profile import user_bp as profile_bp
app.register_blueprint(profile_bp)

from routes.user_routes.edit_profile import user_bp as edit_pf_bp
app.register_blueprint(edit_pf_bp)

from routes.user_routes.dashboard import user_bp as dashboard_bp
app.register_blueprint(dashboard_bp)

from routes.game_routes.result import game_bp as typing_res
app.register_blueprint(typing_res)


from routes.balloon_game_routes.game import game_bp as game
app.register_blueprint(game)


from routes.balloon_game_routes.game_result import game_bp as game_res
app.register_blueprint(game_res)








@app.route("/")
def home():
    return "Hello Flask!"




    
    

#Dashboard Page













print(app.url_map)

if __name__ == "__main__":
    app.run(debug=True)
