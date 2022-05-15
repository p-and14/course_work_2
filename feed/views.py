from flask import Blueprint, render_template, jsonify
from feed.dao.feed_dao import FeedDAO
from config import POSTS_PATH
from bookmarks.utils import get_bookmarks

feed_blueprint = Blueprint("feed_blueprint", __name__, template_folder="templates")

feed_dao = FeedDAO(POSTS_PATH)


@feed_blueprint.route("/")
def feed_page():
    posts = feed_dao.get_posts_all()
    bookmarks_count = len(get_bookmarks())

    return render_template("index.html", posts=posts, bookmarks_count=bookmarks_count)


@feed_blueprint.route("/api/posts")
def get_posts_json():
    posts = feed_dao.get_posts_all()

    return jsonify(posts)
