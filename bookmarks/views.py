from flask import Blueprint, render_template, redirect
from bookmarks.utils import get_bookmarks, add_bookmark, remove_bookmark

bookmarks_blueprint = Blueprint("bookmarks_blueprint", __name__, template_folder="templates")


@bookmarks_blueprint.route("/bookmarks/add/<int:post_id>")
def bookmark_add(post_id):
    add_bookmark(post_id)

    return redirect("/", code=302)


@bookmarks_blueprint.route("/bookmarks/remove/<int:post_id>")
def bookmark_remove(post_id):
    remove_bookmark(post_id)

    return redirect("/", code=302)


@bookmarks_blueprint.route("/bookmarks/")
def bookmarks_page():
    bookmarks = get_bookmarks()

    return render_template("bookmarks.html", bookmarks=bookmarks)