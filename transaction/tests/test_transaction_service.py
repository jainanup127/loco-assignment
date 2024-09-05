import unittest
from app import create_app, db
from transaction.models.transaction import Transaction
from transaction.services.transaction_service import TransactionService
from transaction.dtos.transaction_dto import TransactionDTO


class TransactionServiceTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.app_context = create_app().app_context()
        cls.app_context.push()
        with cls.app_context:
            db.create_all()

    def setUp(self):
        # Clear the database before each test
        with self.app_context:
            db.session.remove()
            db.drop_all()
            db.create_all()

    def test_create_transaction_success(self):
        service = TransactionService()
        dto = TransactionDTO(id= 1, amount=100.0, type='food', parent_id=None)
        result = service.create_transaction(dto)

        with self.app_context:
            transaction = Transaction.query.filter_by(amount=100.0, type='food').first()
            self.assertIsNotNone(transaction)
            self.assertEqual(transaction.amount, 100.0)
            self.assertEqual(transaction.type, 'food')
            self.assertIsNone(transaction.parent_id)

    def test_create_transaction_with_parent(self):
        service = TransactionService()
        parent_dto = TransactionDTO(id= 1, amount=200.0, type='office', parent_id=None)
        service.create_transaction(parent_dto)
        child_dto = TransactionDTO(id=2, amount=50.0, type='food', parent_id=1)
        service.create_transaction(child_dto)

        with self.app_context:
            child_transaction = Transaction.query.filter_by(amount=50.0, type='food').first()
            self.assertIsNotNone(child_transaction)
            self.assertEqual(child_transaction.amount, 50.0)
            self.assertEqual(child_transaction.parent_id, 1)

    def test_get_total_amount(self):
        service = TransactionService()
        parent_dto = TransactionDTO(id=1, amount=500.0, type='office', parent_id=None)
        service.create_transaction(parent_dto)
        parent_transaction = Transaction.query.filter_by(amount=500.0).first()

        child1_dto = TransactionDTO(id=2, amount=100.0, type='food', parent_id=1)
        child2_dto = TransactionDTO(id=3, amount=200.0, type='food', parent_id=2)
        service.create_transaction(child1_dto)
        service.create_transaction(child2_dto)

        total = service.get_transaction_sum(parent_transaction.id)
        self.assertEqual(total, 500.0 + 100.0 + 200.0)

    def test_create_transaction_error(self):
        service = TransactionService()
        with self.app_context:
            db.session.remove()
            with self.assertRaises(Exception):
                dto = TransactionDTO(amount=100.0, type='food', parent_id=None)
                service.create_transaction(dto)


if __name__ == '__main__':
    unittest.main()
