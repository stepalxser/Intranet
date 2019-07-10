import flask
import flask_login
import flask_migrate

from webapp.database import db
from webapp.user.models import User
from webapp.main_page.models import Structure

from webapp.auth.views import blueprint as auth_blueprint
from webapp.main_page.views import blueprint as main_page_blueprint


def create_app():
    app = flask.Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = flask_migrate.Migrate(app, db)

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_page_blueprint)

    login_manager = flask_login.LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app
