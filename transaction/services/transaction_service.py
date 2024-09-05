from transaction.adaptors.transaction_adaptor import TransactionAdaptor
from transaction.exceptions import ParentTransactionNotFoundError
from transaction.models.transaction import Transaction
from transaction.repositories.transaction_repository import TransactionRepository


class TransactionService:

    def __init__(self):
        self.transaction_repository = TransactionRepository()

    def create_transaction(self, transaction_data):
        parent_transaction = None
        if transaction_data.parent_id is not None:
            parent_transaction = self.transaction_repository.get_transaction_by_id(transaction_data.parent_id)
            if parent_transaction is None:
                raise ParentTransactionNotFoundError(transaction_data.parent_id)
        transaction = Transaction(
            id=transaction_data.id,
            amount=transaction_data.amount,
            type=transaction_data.type,
            parent_id=transaction_data.parent_id
        )
        self.transaction_repository.add_transaction(transaction)

    def get_transaction_sum(self, transaction_id):
        """
        Get the total sum of a transaction and all its child transactions
        :param transaction_id:
        :return:
        """
        result = self.transaction_repository.get_transaction_sum(transaction_id)
        if result is None or result[0] is None:
            total_amount = 0
        else:
            total_amount = result[0]
        return total_amount

    def get_transaction_by_id(self, transaction_id):
        transaction = self.transaction_repository.get_transaction_by_id(transaction_id)
        return TransactionAdaptor.entity_to_dto(transaction)

    def get_transaction_by_type(self, transaction_type):
        transactions = self.transaction_repository.get_transactions_by_type(transaction_type)
        return [TransactionAdaptor.entity_to_dto(transaction) for transaction in transactions]
