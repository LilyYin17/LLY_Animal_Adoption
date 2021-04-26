from flask import Flask, render_template, session
from flask import request, redirect, url_for
from flaskext.mysql import MySQL
from flask import Blueprint
import database.db_connector as db
import base64

import os  #debug

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
        img = request.form['img']
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
        
        return redirect(url_for('admin_add_new_pet_result'))

#Admin find a pet page
@crud_api.route('/admin_find_your_pet', methods=['GET', 'POST'])
def admin_find_your_pet():
    if request.method == 'GET':
        return render_template('admin_find_your_pet.j2')

    elif request.method == 'POST':
        db_connection = db.db_connection

        base_query = 'SELECT * FROM Pets WHERE type = "%s"' % (request.form['type'])

      #   if request.form['name'].strip():  #check the name, todo
      #      base_query = base_query + ' AND name LIKE "% + request.form['name'].strip() + %" '


        if request.form['name'].strip():  #check the name
           base_query = base_query + ' AND name =  "%s" ' % request.form['name'].strip()

        if request.form['breed'].strip(): #check the breed
           base_query = base_query + ' AND breed =  "%s" ' % request.form['breed'].strip()

        if request.form['age'].strip(): #check the age
           base_query = base_query + ' AND age =  %s ' % ((request.form['age']))
        
        if request.form['size'].strip(): #check the size
           base_query = base_query + ' AND size =  "%s" ' % (request.form['size'].strip())
        
        if request.form['gender'].strip(): #check the gender
           base_query = base_query + ' AND gender =  "%s" ' % (request.form['gender'].strip())
        
        if request.form['goodWithKids'].strip(): #check if good with kids
           base_query = base_query + ' AND goodWithKids =  %s ' % (request.form['goodWithKids'].strip())
        
        if request.form['goodWithDogs'].strip(): #check the good with dogs
           base_query = base_query + ' AND goodWithDogs =  %s ' % (request.form['goodWithDogs'].strip())
        
        if request.form['goodWithCats'].strip(): #check if good with cats
           base_query = base_query + ' AND goodWithCats =  %s ' % (request.form['goodWithCats'].strip())

        if request.form['mustBeLeashed'].strip(): #check if must be leashed
           base_query = base_query + ' AND mustBeLeashed =  %s ' % (request.form['mustBeLeashed'].strip())
          
        if request.form['availability'].strip(): #check if availability
           base_query = base_query + ' AND availability =  "%s" ' % (request.form['availability'].strip())

        base_query + ";"
        cursor = db.execute_query(db_connection, base_query)
        results = cursor.fetchall()
        return render_template('admin_detailed_find_your_pet.j2', pets=results, base64=base64)


      