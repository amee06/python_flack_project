from flask import Blueprint,redirect,render_template,session,url_for,request
from database import db,cursor

game_bp = Blueprint("result_game",__name__)

@game_bp.route("/ballon_game/result_ballon_game",methods=["POST"])
def result_ballon_game():

  
    print("SESSION DATA:", session)

    user_id = session.get("user_id")

    print("USER ID:", user_id)

    
    score = request.form["score"]
    correct_words = request.form["correct_words"]
    wrong_words = request.form["wrong_words"]

    cursor.execute(
        """
        insert into balloon_scores(user_id,score,correct_words,wrong_words) values(%s,%s,%s,%s)
        """
     , (user_id,score,correct_words,wrong_words)
     )

    db.commit()

    return render_template("/ballon_game/result_ballon_game.html",
                           score=score,correct_words=correct_words,wrong_words=wrong_words)
   