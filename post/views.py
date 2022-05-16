from flask import Blueprint, render_template, jsonify
from post.utils import get_post_by_pk, get_comments_by_post_id

post_blueprint = Blueprint("post_blueprint", __name__, template_folder="templates")


@post_blueprint.route("/posts/<post_id>")
def post_page(post_id):
    try:
        post = get_post_by_pk(post_id)
        comments = get_comments_by_post_id(post_id)
        comments_value = len(comments)

        return render_template("post.html", post=post, comments=comments, comments_value=comments_value)

    except ValueError:
        return "Неправильный номер поста"

    except TypeError:
        post = {"content":"Поста с таким номером не существует"}
        return render_template("post.html", post=post)


@post_blueprint.route("/api/posts/<int:post_id>")
def get_posts_json(post_id):
    post = get_post_by_pk(post_id)

    return jsonify(post)
