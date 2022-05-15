from flask import Blueprint, request, render_template
from search.utils import search_for_posts

search_blueprint = Blueprint("search_blueprint", __name__, template_folder="templates")


@search_blueprint.route("/search/")
def search_page():
    s = request.args.get('s')
    posts = search_for_posts(str(s))
    posts_value = len(posts)

    return render_template("search.html", posts=posts, posts_value=posts_value)
