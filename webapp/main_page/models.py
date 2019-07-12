from webapp.database import db


class Structure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    lead = db.Column(db.String, db.ForeignKey('user.username'), nullable=False)
    parent_id = db.Column(db.Integer, nullable=False, default=0)
    workers = db.relationship('UserInfo', backref='unit')
