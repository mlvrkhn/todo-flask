from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from db import db
import models

from resources.habit import bp as HabitBlueprint
from resources.user import bp as UserBlueprint
from resources.habit_completion import bp as HabitCompletionBlueprint


def create_app(db_url=None):
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    app.config["JWT_SECRET_KEY"] = "3908982254207764219527071196126709504"
    jwt = JWTManager(app)

    api = Api(app)

    with app.app_context():
        db.create_all()

    # @app.before_first_request
    # def create_tables():
    #     db.create_all()

    api.register_blueprint(HabitBlueprint)
    api.register_blueprint(UserBlueprint)
    api.register_blueprint(HabitCompletionBlueprint)

    return app
