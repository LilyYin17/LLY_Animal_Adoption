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
            cursor = db.execute_query(db_connection, query, data)
            query = 'INSERT INTO Customers(email) VALUES (%s)'
            db.execute_query(db_connection, query, data)
            return render_template('landing_page.j2')

#Listener
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 1234))
    app.run(port=port, debug=True, host='0.0.0.0')