from flask import Blueprint, render_template, jsonify
from post.utils import get_post_by_pk, get_comments_by_post_id

post_blueprint = Blueprint("post_blueprint", __name__, template_folder="templates")


@post_blueprint.route("/posts/<int:post_id>")
def post_page(post_id):
    post = get_post_by_pk(post_id)
    comments = get_comments_by_post_id(post_id)
    comments_value = len(comments)
    return render_template("post.html", post=post, comments=comments, comments_value=comments_value)


@post_blueprint.route("/api/posts/<int:post_id>")
def get_posts_json(post_id):
    post = get_post_by_pk(post_id)

    return jsonify(post)
