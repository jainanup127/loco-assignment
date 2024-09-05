from sqlalchemy import text

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

    @staticmethod
    def get_transaction_sum(transaction_id):
        from app import db
        query = text('''
                WITH RECURSIVE transaction_hierarchy AS (
                    -- Base case: start with the given transaction
                    SELECT id, amount, parent_id
                    FROM "transaction"
                    WHERE id = :transaction_id

                    UNION ALL

                    -- Recursive case: select all child transactions
                    SELECT t.id, t.amount, t.parent_id
                    FROM "transaction" t
                    INNER JOIN transaction_hierarchy th ON t.parent_id = th.id
                )
                SELECT SUM(amount) AS total_amount FROM transaction_hierarchy;
                ''')
        return db.session.execute(query, {'transaction_id': transaction_id}).fetchone()
