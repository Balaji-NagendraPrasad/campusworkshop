"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi81du4dadc9vm2ru3g-a.oregon-postgres.render.com",
        database="todo_eghg",
        user="root",
        password="9hvNm8R5qKJVnnT97Fvd9jysNt2E213y")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
