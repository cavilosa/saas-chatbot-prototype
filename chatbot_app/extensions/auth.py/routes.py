import json
from os import environ as env
from urllib.parse import quote_plus, urlencode

from flask import Blueprint, redirect, render_template, session, url_for
from chatbot_app.extensions.oauth import oauth

# Create a Blueprint
auth_bp = Blueprint(
    'auth_bp', __name__,
    template_folder='templates'
)

@auth_bp.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("auth_bp.callback", _external=True)
    )

@auth_bp.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    return redirect(url_for('main_bp.home')) # Redirect to the main home route

@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(
        f'https://{env.get("AUTH0_DOMAIN")}/v2/logout?' +
        urlencode({
            "returnTo": url_for('main_bp.home', _external=True),
            "client_id": env.get("AUTH0_CLIENT_ID"),
        }, quote_via=quote_plus)
    )