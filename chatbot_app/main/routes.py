import json
from flask import Blueprint, render_template, session

main_bp = Blueprint(
    'main_bp', __name__,
    template_folder='templates'
)

@main_bp.route("/")
def home():
    return render_template(
        "home.html", 
        session=session.get('user'), 
        pretty=json.dumps(session.get('user'), indent=4)
    )