import flask
import flask_login
import flask_migrate

from webapp.database import db
from webapp.user.models import User

from webapp.auth.views import blueprint as auth_blueprint


def create_app():
    app = flask.Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = flask_migrate.Migrate(app, db)

    app.register_blueprint(auth_blueprint)

    login_manager = flask_login.LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/')
    @app.route('/index')
    @flask_login.login_required
    def index():
        title = 'Главная'
        return flask.render_template('index.html', page_title=title)

    return app
