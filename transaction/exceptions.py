class ParentTransactionNotFoundError(Exception):
    def __init__(self, transaction_id):
        self.transaction_id = transaction_id
        self.message = f'Parent transaction with id {self.transaction_id} not found'
        super().__init__(self.message)


class CircularDependencyDetectedError(Exception):
    def __init__(self):
        self.message = f'Circular dependency detected'
