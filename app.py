from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def home_page():
    """Renders the home page showing input form"""

    return render_template("questions.html", prompts=silly_story.prompts)

@app.get("/results")
def get_results():
    """Renders results page based on inputs"""
    # Make these variables and pull them out of the return
    return render_template(
        "results.html",
        final_story=silly_story.generate(request.args))