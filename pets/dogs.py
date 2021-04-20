from flask import Flask, render_template, session
from flask import request, redirect, url_for
from flask import Blueprint

dogs_api = Blueprint('dogs_api', __name__)

#Routes
#Landing page
@dogs_api.route('/browse_dogs')
def browse_dogs():
    return render_template('browse_dogs.j2')