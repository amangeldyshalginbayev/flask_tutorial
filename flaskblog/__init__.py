from flask import Flask
import click
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flaskblog.config import TestConfig

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('configuration.cfg')

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    from flaskblog.main.routes import main
    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.comments.routes import comments
    from flaskblog.errors.handlers import errors

    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(comments)
    app.register_blueprint(errors)

    app.cli.add_command(init_db_command)
    app.cli.add_command(drop_db_command)

    return app


@click.command('init-db')
@with_appcontext
def init_db_command():
    """This function is used only once from command line for initial
    database setup when configuring the app in new environment
    """
    with create_app().app_context():
        db.create_all()
    click.echo('Initialized the database.')


@click.command('drop-db')
@with_appcontext
def drop_db_command():
    """This function is used to drop database from command line
    """
    with create_app().app_context():
        db.drop_all()
    click.echo('Dropped the database.')


def create_test_app():
    app = Flask(__name__)
    app.config.from_object(TestConfig)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    from flaskblog.main.routes import main
    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.comments.routes import comments
    from flaskblog.errors.handlers import errors

    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(comments)
    app.register_blueprint(errors)

    return app
