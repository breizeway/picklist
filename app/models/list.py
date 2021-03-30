from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship

from .db import db


class List(db.Model):
    __tablename__ = 'lists'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='lists')
    picks = db.relationship('Pick', back_populates='parent_list')
