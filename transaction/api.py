from flask import jsonify, request, Blueprint
from pydantic import ValidationError

from transaction.dtos.transaction_dto import TransactionDTO
from transaction.services.transaction_service import TransactionService

transaction_blueprint = Blueprint('transaction', __name__, url_prefix='/transactionservice/')


@transaction_blueprint.route('transaction/<int:transaction_id>', methods=['PUT'])
def add_transaction(transaction_id):
    try:
        request_data = request.json
        request_data['id'] = transaction_id
        transaction_dto = TransactionDTO(**request_data)
        TransactionService().create_transaction(transaction_dto)
        return jsonify({'status': 'ok'})
    except ValidationError as e:
        return jsonify({'error': e.errors()}), 400
    except Exception as e:
        return jsonify({'error': "something is wrong with database"}), 500


@transaction_blueprint.route('transaction/<int:transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    transaction = TransactionService().get_transaction_by_id(transaction_id)
    if transaction:
        return jsonify(transaction.dict())
    return jsonify({'error': 'Transaction not found'}), 404


@transaction_blueprint.route('types/<string:transaction_type>', methods=['GET'])
def get_transactions_by_type(transaction_type):
    transactions = TransactionService().get_transaction_by_type(transaction_type)
    return jsonify([transaction.id for transaction in transactions])


@transaction_blueprint.route('sum/<int:transaction_id>', methods=['GET'])
def get_transaction_sum(transaction_id):
    total_sum = TransactionService().get_transaction_sum(transaction_id)
    return jsonify({'sum': total_sum})
