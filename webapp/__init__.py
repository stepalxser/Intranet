import locale

import flask
import flask_login
import flask_migrate
import flask_avatars

from webapp.database import db
from webapp.user.models import User, UserInfo
from webapp.main_page.models import Structure

from webapp.auth.views import blueprint as auth_blueprint
from webapp.main_page.views import blueprint as main_page_blueprint
from webapp.user.views import blueprint as user_blueprint


def create_app():
    app = flask.Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = flask_migrate.Migrate(app, db)
    avatars = flask_avatars.Avatars(app)


    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_page_blueprint)
    app.register_blueprint(user_blueprint)

    login_manager = flask_login.LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    locale.setlocale(locale.LC_ALL, 'russian')

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.shell_context_processor
    def make_shell_context():
        return {'db': db, "User": User, 'Structure': Structure, 'UserInfo': UserInfo}


    return app
