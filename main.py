from flask import Flask
from feed.views import feed_blueprint
from post.views import post_blueprint
from search.views import search_blueprint
from user.views import user_blueprint
from tag.views import tag_blueprint
from bookmarks.views import bookmarks_blueprint

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


app.register_blueprint(feed_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(tag_blueprint)
app.register_blueprint(bookmarks_blueprint)

if __name__ == "__main__":
    app.run()
