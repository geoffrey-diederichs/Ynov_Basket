from flask import *
from flask_login import *
from flask_sqlalchemy import SQLAlchemy
from api import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SECRET_KEY"] = "VERY_SECRET_KEY"
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)

with app.app_context():
    db.create_all()

@login_manager.user_loader
def loader_user(user_id):
    return Users.query.get(int(user_id))

@app.route("/")
def go_to_home():
    return redirect(url_for("home"))

@app.route("/home")
def home():
    if current_user.is_authenticated:
        return redirect(url_for("players"))
    else:
        return render_template("home.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return "Already logged in."
    if request.method == "POST":
        if Users.query.filter_by(username=request.form.get("username")).first():
            return "User already exists !"
        elif not request.form.get("password"):
            return "Don't forget the password !"
        user = Users(username=request.form.get("username"), password=request.form.get("password"))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return "Already logged in."
    if request.method == "POST":
        user = Users.query.filter_by(username=request.form.get("username")).first()
        if not user or user.password != request.form.get("password"):
            return "Wrong credentials !"
        else:
            login_user(user)
            return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/logout")
def logout():
    if not current_user.is_authenticated:
        return "Not logged in."
    logout_user()
    return redirect(url_for("home"))

@app.route("/players")
def players():
    if not current_user.is_authenticated:
        return "Log in first."
    return render_template("players.html", players=get_api("players"))

@app.route("/player/<int:player_id>")
def player_detail(player_id:int):
    if not current_user.is_authenticated:
        return "Log in first."
    return render_template("player_detail.html", player=get_api("players/"+str(player_id)))

@app.route("/teams")
def teams():
    if not current_user.is_authenticated:
        return "Log in first."
    return render_template("teams.html", teams=get_api("teams"))

@app.route("/team/<int:team_id>")
def team_detail(team_id:int):
    if not current_user.is_authenticated:
        return "Log in first."
    return render_template("team_detail.html", team=get_api("teams/"+str(team_id)))

@app.route("/games")
def games():
    if not current_user.is_authenticated:
        return "Log in first."
    return render_template("games.html", games=get_api("/games"))

@app.route("/game/<int:game_id>")
def game_detail(game_id:int):
    if not current_user.is_authenticated:
        return "Log in first."
    return render_template("game_detail.html", game=get_api("/games/"+str(game_id)))

if __name__ == "__main__":
    load_key()
    app.run()
