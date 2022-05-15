from flask import Blueprint, render_template
from tag.utils import get_posts_by_tag

tag_blueprint = Blueprint("tag_blueprint", __name__, template_folder="templates")


@tag_blueprint.route("/tag/<tag_name>")
def tag_page(tag_name):
    posts = get_posts_by_tag(tag_name)
    return render_template("tag.html", posts=posts, tag_name=tag_name)
