from flask import Flask, render_template
import os

#Configuration
app = Flask(__name__)

#Routes
@app.route('/')
def root():
    return render_template('landing_page.j2')

#Listener
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 1234))
    app.run(port=port, debug=True, host='0.0.0.0')