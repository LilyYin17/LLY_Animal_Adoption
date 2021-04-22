from flask import Flask, render_template, session
from flask import request, redirect, url_for
from flask import Blueprint

crud_api = Blueprint('crud_api', __name__)

#Routes
@crud_api.route('/add_new_pets', methods=['GET', 'POST'])
def add_new_pets():
    if request.method == 'GET':
        return render_template('add_new_pets.j2')
    elif request.method == 'POST':
        db_connection = db.db_connection
        return render_template('browse_dogs.j2')