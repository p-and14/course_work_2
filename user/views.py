from flask import Blueprint, render_template
from user.utils import get_posts_by_user

user_blueprint = Blueprint("user_blueprint", __name__, template_folder="templates")


@user_blueprint.route("/users/<username>")
def user_page(username):
    posts = get_posts_by_user(username)

    return render_template("user-feed.html", posts=posts)
