from transaction.adaptors.transaction_adaptor import TransactionAdaptor
from transaction.models.transaction import Transaction
from transaction.repositories.transaction_repository import TransactionRepository


class TransactionService:

    def __init__(self):
        self.transaction_repository = TransactionRepository()

    def create_transaction(self, transaction_data):
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
        total_sum = 0
        transaction = self.transaction_repository.get_transaction_by_id(transaction_id)
        if transaction:
            total_sum += transaction.amount
            child_transactions = self.transaction_repository.get_child_transactions(transaction_id)
            for child in child_transactions:
                total_sum += self.get_transaction_sum(child.id)
        return total_sum

    def get_transaction_by_id(self, transaction_id):
        transaction = self.transaction_repository.get_transaction_by_id(transaction_id)
        return TransactionAdaptor.entity_to_dto(transaction)

    def get_transaction_by_type(self, transaction_type):
        transactions = self.transaction_repository.get_transactions_by_type(transaction_type)
        return [TransactionAdaptor.entity_to_dto(transaction) for transaction in transactions]
