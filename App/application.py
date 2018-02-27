from flask import Flask, render_template, request, redirect, url_for, flash
from msiapp import application, db
from msiapp.models import Track

from sklearn.externals import joblib


@application.route('/')
def index():
    """Main view that lists songs

    Create view into index page that uses data queried from Track database and
    inserts it into the msiapp/templates/index.html template

    :return: rendered html template

    """

    return render_template('index.html', tracks=Track.query.all())

# @application.route('/add', methods=['POST'])
# def add_entry():
#     """View that process a POST with new song input

#     :return: redirect to index page
#     """

#     track1 = Track(artist=request.form['artist'], album=request.form['album'], title=request.form['title'])
#     db.session.add(track1)
#     db.session.commit()

#     return redirect(url_for('index'))
@app.route('/predict', methods=['POST'])
def make_prediction():
    if request.method=='POST':
        return render_template('index.html', label="3")

if __name__ == "__main__":
    model = joblib.load('model.pkl')
    application.run(host=‘0.0.0.0’,debug=True)
