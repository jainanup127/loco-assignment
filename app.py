from flask import Flask, jsonify
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import get_config
from db import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config())
    db.init_app(app)

    from transaction.api import transaction_blueprint
    app.register_blueprint(transaction_blueprint)

    return app



app  =create_app()

@app.route('/routes', methods=['GET'])
def list_routes():
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append({
            "endpoint": rule.endpoint,
            "methods": list(rule.methods),
            "url": str(rule)
        })
    return jsonify(routes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
