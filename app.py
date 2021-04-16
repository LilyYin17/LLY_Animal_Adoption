from flask import Flask, render_template, session
from flask import request, redirect, url_for
from flaskext.mysql import MySQL
import os
import database.db_connector as db

#Configuration
app = Flask(__name__)
app.secret_key = 'your secret key'

#Routes
#Landing page
@app.route('/')
def root():
    return render_template('landing_page.j2')

#Adopter home page
@app.route('/adopter_home')
def adpoter_home():
    #check is user is logged in
    if 'adopter_loggedin' in session:
        return render_template('adopter_home.j2', username=session['username'])
    #user is not logged in
    return render_template('adopter_login.j2') 

#Shelter home page
@app.route('/shelter_home')
def shelter_home():
    #check is user is logged in
    if 'shelter_loggedin' in session:
        return render_template('shelter_home.j2', username=session['username'])
    #user is not logged in
    return render_template('shelter_login.j2') 

#Shelter log in page
@app.route('/shelter_login', methods=['GET', 'POST'])
def shelter_login():
    if request.method == 'GET':
        return render_template('shelter_login.j2')
    elif request.method == 'POST':
        db_connection = db.db_connection
        #Check if account exists 
        query = 'SELECT * FROM Customers WHERE email = %s AND password = %s'
        email = request.form['email']
        psw = request.form['password']
        data = (email, psw)
        cursor = db.execute_query(db_connection, query, data)
        results = cursor.fetchall()
        if results:
            #Successful loggedin
            session['username'] = email
            if email == 'admin@oregonstate.edu': #If user is admin
                session['shelter_loggedin'] = True
                return redirect(url_for('shelter_home', variable=session['username']))
            else: #If user is regular customer
                return render_template('shelter_login_error.j2')
        else:
            #Account does not exist or username/password incorrect
            return render_template('shelter_login_error.j2')

#Adopter log in page
@app.route('/adopter_login', methods=['GET', 'POST'])
def adopter_login():
    if request.method == 'GET':
        return render_template('adopter_login.j2')
    elif request.method == 'POST':
        db_connection = db.db_connection
        #Check if account exists 
        query = 'SELECT * FROM Customers WHERE email = %s AND password = %s'
        email = request.form['email']
        psw = request.form['password']
        data = (email, psw)
        cursor = db.execute_query(db_connection, query, data)
        results = cursor.fetchall()
        if results:
            #Successful loggedin
            session['username'] = email
            if email == 'admin@oregonstate.edu': #If user is admin
                return render_template('adopter_login_error.j2')
            else: #If user is regular customer
                session['adopter_loggedin'] = True
                return redirect(url_for('adpoter_home', variable=session['username']))
        else:
            #Account does not exist or username/password incorrect
            return render_template('adopter_login_error.j2')

#Log out
@app.route('/logout')
def logout():
    #Remove session data
    session.pop('shelter_loggedin', None)
    session.pop('adopter_loggedin', None)
    session.pop('username', None)
    return redirect(url_for('root'))

#Sign up page
@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup_page.j2')
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
            return redirect(url_for('adopter_login'))

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