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

#Home page
@app.route('/home')
def home():
    #check is user is logged in
    if 'loggedin' in session:
        return render_template('home_page.j2', username=session['username'])
    #user is not logged in
    return render_template('login_page.j2') 

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
            return redirect(url_for('login'))

#Log in page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login_page.j2')
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
            session['loggedin'] = True
            session['username'] = email
            return redirect(url_for('home', variable=session['username']))
        else:
            #Account does not exist or username/password incorrect
            return render_template('login_error.j2')

#Log out
@app.route('/logout')
def logout():
    #Remove session data
    session.pop('loggedin', None)
    session.pop('username', None)
    return redirect(url_for('root'))

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