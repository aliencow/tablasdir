from flask import Flask, redirect, session
from mod_tables.models import TableBuilder


app = Flask(__name__)

table_builder = TableBuilder()


from common.routes import main
from mod_tables.controllers import tables


# Register the different blueprints
app.register_blueprint(main)
app.register_blueprint(tables)
