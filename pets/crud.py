from flask import Flask, render_template, session
from flask import request, redirect, url_for
from flaskext.mysql import MySQL
from flask import Blueprint
import database.db_connector as db
import base64

import os  #debug

crud_api = Blueprint('crud_api', __name__)

# Routes
# Admin protocol
# Admin add new pet page
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
        
        return redirect(url_for('admin_add_new_pet_result'))


# Admin find a dog page
@crud_api.route('/admin_find_a_dog', methods=['GET', 'POST'])
def admin_find_a_dog():

   # get all existing dog's breeds from database
   if request.method == 'GET':
      db_connection = db.db_connection
      query = 'SELECT breed FROM Pets WHERE type = "%s"' % ("dog")
      cursor = db.execute_query(db_connection, query)
      results = cursor.fetchall()
       
      breeds = [result['breed'] for result in results]
      # print("query result: %s" % breeds)
      return render_template('admin_find_a_dog.j2', breeds = breeds)

   elif request.method == 'POST':
        db_connection = db.db_connection

        base_query = 'SELECT * FROM Pets WHERE type = "%s"' % ("dog")

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
        return render_template('admin_detailed_find_your_dog.j2', dogs=results, base64=base64)

# Admin find a cat page
@crud_api.route('/admin_find_a_cat', methods=['GET', 'POST'])
def admin_find_a_cat():

   # get all existing cat's breeds from database
   if request.method == 'GET':
      db_connection = db.db_connection
      query = 'SELECT breed FROM Pets WHERE type = "%s"' % ("cat")
      cursor = db.execute_query(db_connection, query)
      results = cursor.fetchall()
       
      breeds = [result['breed'] for result in results]
      # print("query result: %s" % breeds)
      return render_template('admin_find_a_cat.j2', breeds = breeds)

   elif request.method == 'POST':
        db_connection = db.db_connection

        base_query = 'SELECT * FROM Pets WHERE type = "%s"' % ("cat")

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
        return render_template('admin_detailed_find_your_cat.j2', cats=results, base64=base64)


# Admin find other pet page
@crud_api.route('/admin_find_other_pet', methods=['GET', 'POST'])
def admin_find_other_pet():

   # get all existing cat's breeds from database
   if request.method == 'GET':
      db_connection = db.db_connection
      query = 'SELECT breed FROM Pets WHERE type = "%s"' % ("others")
      cursor = db.execute_query(db_connection, query)
      results = cursor.fetchall()
       
      breeds = [result['breed'] for result in results]
      # print("query result: %s" % breeds)
      return render_template('admin_find_other_pet.j2', breeds = breeds)

   elif request.method == 'POST':
        db_connection = db.db_connection

        base_query = 'SELECT * FROM Pets WHERE type = "%s"' % ("others")

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
        return render_template('admin_detailed_find_other_pet.j2', others=results, base64=base64)


# @crud_api.route('/admin_add_new_pet_result', methods=['GET', 'POST'])
# def admin_add_new_pet_result():
#     return render_template('admin_add_new_pet_result.j2')

# View pets details, give id is petsID in Pets table
@crud_api.route('/admin_view_details/<int:id>')
def view_details(id):
   db_connection = db.db_connection
   query = 'SELECT * FROM Pets WHERE petsID = %d;' % (id)
   cursor = db.execute_query(db_connection, query)
   results = cursor.fetchall()
   return render_template('admin_view_details.j2', dogs=results, base64=base64)

# Update pets details, give id is petsID in Pets table
@crud_api.route('/admin_update_details/<int:id>', methods=['POST', 'GET'])
def update_details(id):
   petsID = id
   db_connection = db.db_connection
   query = 'SELECT * FROM Pets WHERE petsID = %d;' % (id)
   cursor = db.execute_query(db_connection, query)
   results = cursor.fetchall()
   if request.method == 'GET':
      return render_template('admin_update_pets.j2', dogs=results, value=petsID)
   elif request.method == 'POST':
      type = request.form['type']
      name = request.form['name']
      breed = request.form['breed']
      age = request.form['age']
      size = request.form['size']
      gender = request.form['gender']
      goodWithKids = request.form['goodWithKids']
      goodWithDogs = request.form['goodWithDogs']
      goodWithCats = request.form['goodWithCats']
      mustBeLeashed = request.form['mustBeLeashed']
      availability = request.form['availability']
      query = "UPDATE Pets SET type='%s', name='%s', breed='%s', age='%s', size='%s', gender='%s', goodWithKids='%s', goodWithDogs='%s', goodWithCats='%s', mustBeLeashed='%s', availability='%s' WHERE petsID=%d;" % (type, name, breed, age, size, gender, goodWithKids, goodWithDogs, goodWithCats, mustBeLeashed, availability, petsID)
      db.execute_query(db.db_connection, query)
      query = 'SELECT * FROM Pets WHERE petsID = %d;' % (petsID)
      cursor = db.execute_query(db_connection, query)
      results = cursor.fetchall()
      return render_template('admin_view_details.j2', dogs=results, base64=base64)

# Adopter protocol
# Adopter browsw pet details, give id is petsID
@crud_api.route('/browse_details/<int:id>', methods=['POST', 'GET'])
def browse_detail(id):
   db_connection = db.db_connection
   if request.method == 'GET':
      query = 'SELECT * FROM Pets WHERE petsID = %d;' % (id)
      cursor = db.execute_query(db_connection, query)
      results = cursor.fetchall()
      return render_template('customer_browse_details.j2', pets=results, base64=base64)
   elif request.method == 'POST':
      # Customer click "adopt" button, pet becomes "pending"
      query = "UPDATE Pets SET availability='pending' WHERE petsID=%d;" % (id)
      db.execute_query(db.db_connection, query)
      return render_template('customer_request_ok.j2', userID=session['userID'])
