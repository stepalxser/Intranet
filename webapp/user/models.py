import flask_login
from werkzeug.security import generate_password_hash, check_password_hash

from webapp.database import db


class User(db.Model, flask_login.UserMixin):
    username = db.Column(db.String(), unique=True, nullable=False, primary_key=True, index=True)
    password_hash = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(64), nullable=False, index=True)
    last_name = db.Column(db.String(64), nullable=False, index=True)
    privilege = db.Column(db.Boolean, default=False)
    need_reset = db.Column(db.Boolean, default=True)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def is_admin(self):
        return self.privilege

    def get_id(self):
        return self.username

    def __repr__(self):
        return '<user> {}'.format(self.username)

