from flask import Flask, render_template, session
from flask import request, redirect, url_for
from flask import Blueprint

crud_api = Blueprint('crud_api', __name__)

#Routes
@crud_api.route('/add_new_pets')
def add_new_pets():
    return render_template('add_new_pets.j2')