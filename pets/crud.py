from flask import Flask, render_template, session
from flask import request, redirect, url_for
from flaskext.mysql import MySQL
from flask import Blueprint
import database.db_connector as db
import base64

crud_api = Blueprint('crud_api', __name__)

#Routes
#Admin add new pet page
@crud_api.route('/admin_new_pets', methods=['GET', 'POST'])
def admin_new_pets():
    if request.method == 'GET':
        return render_template('admin_new_pets.j2')
    elif request.method == 'POST':
        db_connection = db.db_connection
        query = 'INSERT INTO Pets(type, name, img, breed, age, size, gender, goodWithKids, goodWithDogs, goodWithCats, mustBeLeashed, availability) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        type = request.form['type']
        name = request.form['name']
        img = request.files['img'].read()
        breed = request.form['breed']
        age = request.form['age']
        size = request.form['size']
        gender = request.form['gender']
        goodWithKids = request.form['goodWithKids']
        goodWithDogs = request.form['goodWithDogs']
        goodWithCats = request.form['goodWithCats']
        mustBeLeashed = request.form['mustBeLeashed']
        availability = request.form['availability']

        data = (type, name, img, breed, age, size, gender, goodWithKids, goodWithDogs, goodWithCats, mustBeLeashed, availability)
        db.execute_query(db.db_connection, query, data)
        
        # return redirect(url_for('admin_new_pets'))
        return redirect(url_for('admin_add_new_pet_result'))