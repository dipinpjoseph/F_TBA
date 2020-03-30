
from app import db


class E_List(db.Model):
    __tablename__ = 'e_list'

    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(1000))
    sol = db.Column(db.String(1000))
    comment = db.Column(db.String(1000))
    cat = db.Column(db.String(200))
    votes = db.Column(db.Integer, default = 0)

    def __init__(self, topic, sol, comment, cat):
        self.topic = topic
        self.sol = sol
        self.comment = comment
        self.cat = cat

    def __repr__(self):
        return '<id {}>'.format(self.id)
