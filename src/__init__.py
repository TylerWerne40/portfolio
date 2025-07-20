from flask import Flask, abort

app = Flask(__name__)

projects = [
    {
        "name": "Headpat Clicker",
        "thumb": None,
        "hero": None,
        "categories": ["java", "game-dev"],
        "slug": "headpat-clicker",
        "prod": "https://itch.io",
    },
    {
        "name": "Habit tracking app with Python and MongoDB",
        "thumb": "img/habit-tracking.png",
        "hero": "img/habit-tracking-hero.png",
        "categories": ["python", "web"],
        "slug": "habit-tracking",
        "prod": "https://udemy.com",
    },
]

slug_project = {project["slug"]: project for project in projects}

@app.route("/")
def home():
    return render_template("home.html", projects=projects)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")
    
@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_projects:
        abort(404)
    return render_template(
        f"project_{slug}.html",
        project=slug_to_project[slug]
    )

@app.errorhandler(404):
def fourohfour(error):
    return render_template("404.html")