import app
from flask import Response, render_template


@app.Flask.route('/ladar')
def show_ladar():
    return render_template('ladar.html')
