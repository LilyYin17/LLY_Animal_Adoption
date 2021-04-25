from flask import Flask, render_template, session
from flask import request, redirect, url_for
from flaskext.mysql import MySQL
import database.db_connector as db
from pets.crud import crud_api
from flask import Blueprint
import base64

cats_api = Blueprint('cats_api', __name__)

#Cats Archive page, show all cats
@cats_api.route('/cats_archive')
def dogs_archive():
    db_connection = db.db_connection
    query = 'SELECT * FROM Pets WHERE type = "%s";' % ("cat")
    cursor = db.execute_query(db_connection, query)
    results = cursor.fetchall()
    return render_template('cats_archive.j2', cats=results, base64=base64)