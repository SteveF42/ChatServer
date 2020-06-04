from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=False)

    with app.app_context():
        from application.views import view

        app.register_blueprint(view,url_prefix='/')

    return app