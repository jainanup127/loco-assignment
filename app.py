from flask import render_template, request, send_from_directory
from flask import Flask
from config import get_config
from db import db
from transaction.services.transaction_service import TransactionService


def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config())
    db.init_app(app)

    from transaction.api import transaction_blueprint
    app.register_blueprint(transaction_blueprint)

    return app


app = create_app()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sum', methods=['POST'])
def sum_api():
    transaction_id = request.form.get('transaction_id')
    # Call the service to get the sum
    response = TransactionService().get_transaction_sum(transaction_id)
    return render_template('sum.html', sum=response)


@app.route('/types', methods=['POST'])
def types_api():
    transaction_type = request.form.get('type')
    # Call the service to get transaction IDs
    transactions = TransactionService().get_transaction_by_type(transaction_type)

    return render_template('types.html', ids=[transaction.id for transaction in transactions])


@app.route('/add')
def add_transaction():
    return send_from_directory('templates', 'add.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
