from flask import Flask, render_template, session
from flask import request, redirect
from flaskext.mysql import MySQL
import os
import database.db_connector as db

#Configuration
app = Flask(__name__)

#Routes
#Landing page
@app.route('/')
def root():
    return render_template('landing_page.j2')

#sign up page
@app.route('/signup', methods=['GET','POST'])
def signup_post():
    if request.method == 'GET':
        return render_template('signup_form_page.j2')
    elif request.method == 'POST':
        db_connection = db.db_connection
        query = 'SELECT * FROM Customers WHERE email = %s'
        email = request.form['email']
        data = (email)
        cursor = db.execute_query(db_connection, query, data)
        results = cursor.fetchall()
        #Check if account exists using MySQL
        if results:
            return render_template('user_already_exists_page.j2')
        else:
            query = 'INSERT INTO Customers(email, password) VALUES (%s, %s)'
            email = request.form['email']
            psw = request.form['psw']
            data = (email, psw)
            db.execute_query(db_connection, query, data)
            return render_template('landing_page.j2')

#log in page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login_page.j2')
    elif request.method == 'POST':
        return render_template('login_page.j2')

@app.route('/findPetAdmin', methods=['GET', 'POST'])
def findPetAdmin():
    return render_template('admin_Find_your_pet.j2')

@app.route('/otherPets', methods=['GET', 'POST'])
def otherPets():
    return render_template('other_animal.j2')


@app.route('/findPetCustomer', methods=['GET', 'POST'])
def findPetCustomer():
    return render_template('customer_Find_your_pet.j2')

@app.route('/petDetail', methods=['GET', 'POST'])
def petDetail():
    return render_template('detailed_Find_your_pet.j2')

@app.route('/addNewPet', methods=['GET', 'POST'])
def addNewPet():
    return render_template('new_pets.j2')

#Listener
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 1234))
    app.run(port=port, debug=True, host='0.0.0.0')