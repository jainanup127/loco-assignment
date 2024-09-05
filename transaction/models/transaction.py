from sqlalchemy import Index

from db import db


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(50), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('transaction.id'), nullable=True)

    type_index = Index('type_index', type)
