import click
from flask import current_app, g
from flask.cli import with_appcontext
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = ""

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    sqlalchemy_url = 'dummy'
    engine = create_engine(sqlalchemy_url)

    if 'conn' not in g:
        g.conn = engine.connect()

    return g.conn


def close_db(e=None):
    conn = g.pop('conn', None)

    if conn is not None:
        conn.close()


def init_db():
    db = get_db()
    with current_app.open_resource("schema.sql") as f:
        for item in f.read().decode("utf-8").split(';'):
            print(item)
            db.execute(item)

    click.echo("Initialized the database.")


@click.command("init_db")
@with_appcontext
def init_db_command():
    init_db()


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
