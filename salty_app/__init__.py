import os
from flask import Flask
from dotenv import load_dotenv
from salty_app.models import db, migrate
from salty_app.routes.about_routes import about_routes
from salty_app.routes.home_routes import home_routes
from salty_app.routes.marketing_routes import marketing_routes
from salty_app.routes.modeling_routes import modeling_routes
from salty_app.routes.register_routes import register_routes
from salty_app.routes.stats_routes import stats_routes
from salty_app.routes.user_routes import user_routes


# Creating DataBase name in the current directory -- using relative filepath
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")


# Defining Function "create_app"
def create_app():
    # Instantiating Flask App
    app = Flask(__name__)

    # Configures the DataBase w/ name specified by "DATABASE_URI"
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    # Initializes the DataBase
    db.init_app(app)
    # Migrates the app and DataBase
    migrate.init_app(app, db)

    # Registering the blueprints from the different routes
    app.register_blueprint(about_routes)
    app.register_blueprint(home_routes)
    app.register_blueprint(marketing_routes)
    app.register_blueprint(modeling_routes)
    app.register_blueprint(register_routes)
    app.register_blueprint(stats_routes)
    app.register_blueprint(user_routes)

    # Returning / Running Flask App
    return app


# Factory pattern; Flask best practice -- creating and running app
if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
