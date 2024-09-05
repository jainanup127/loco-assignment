from transaction.models.transaction import Transaction


class TransactionRepository:

    @staticmethod
    def add_transaction(transaction):
        from app import db

        db.session.add(transaction)
        db.session.commit()

    @staticmethod
    def get_transaction_by_id(transaction_id):
        return Transaction.query.get(transaction_id)

    @staticmethod
    def get_transactions_by_type(transaction_type):
        return Transaction.query.filter_by(type=transaction_type).all()

    @staticmethod
    def get_child_transactions(transaction_id):
        return Transaction.query.filter_by(parent_id=transaction_id).all()
