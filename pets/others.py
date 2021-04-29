from flask import Flask, render_template, session
from flask import request, redirect, url_for
from flaskext.mysql import MySQL
import database.db_connector as db
from pets.crud import crud_api
from flask import Blueprint
import base64

others_api = Blueprint('others_api', __name__)

#Routes
@others_api.route('/browse_others')
def browse_others():
    return render_template('browse_others.j2')

#Other pets Archive page, show all other pets.
@others_api.route('/others_archive')
def others_archive():
    db_connection = db.db_connection
    query = 'SELECT * FROM Pets WHERE type = "%s";' % ("others")
    cursor = db.execute_query(db_connection, query)
    results = cursor.fetchall()
    return render_template('others_archive.j2', others=results, base64=base64)


# Delete selected pet, given id is petsID in Pets table
@others_api.route('/admin_delete_other/<int:id>')
def delete_other(id):
   db_connection = db.db_connection

   # Delete selected pet
   query = "DELETE FROM Pets WHERE petsID=%d;" % (id)
   db.execute_query(db_connection, query)

   # Show updated other pets information
   query = 'SELECT * FROM Pets WHERE type = "%s";' % ("others")
   cursor = db.execute_query(db_connection, query)
   results = cursor.fetchall()
   return redirect(url_for('others_api.others_archive'))