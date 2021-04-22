from flask import Flask, render_template, session
from flask import request, redirect, url_for
from flaskext.mysql import MySQL
import database.db_connector as db
from pets.crud import crud_api
from flask import Blueprint
from base64 import b64encode

dogs_api = Blueprint('dogs_api', __name__)

#Routes
@dogs_api.route('/browse_dogs')
def browse_dogs():
    return render_template('browse_dogs.j2')

#Dogs Archive page, show all dogs
@dogs_api.route('/dogs_archive')
def dogs_archive():
    db_connection = db.db_connection
    query = 'SELECT * FROM Pets WHERE name = "%s";' % ("Lily")
    cursor = db.execute_query(db_connection, query)
    results = cursor.fetchall()
    return render_template('dogs_archive.j2', dogs=results)