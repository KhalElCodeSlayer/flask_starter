"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""
import os
from app import app
from flask import render_template, request, redirect, send_from_directory, url_for, flash, session, abort
from werkzeug.utils import secure_filename
from app import db
from app.models import Property
from .forms import PropertyForm
import psycopg2


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Khalid Williams")


@app.route('/properties/create',methods=["GET","POST"])
def pForm():
    form = PropertyForm()
    if request.method == 'POST' and  form.validate_on_submit():
        image = form.photo.data
        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        db.session.add(Property(form.title.data, form.description.data, form.rooms.data, form.bathrooms.data, form.price.data, form.type.data, form.location.data, filename))
        db.session.commit()
        
        flash('Property Added', 'success')
        return redirect(url_for('properties'))
    return render_template("property.html", form=form)

@app.route("/properties")
def properties():
    properties = Property.query.all()
    return render_template("properties.html", properties = properties)

@app.route("/property/<propertyid>")
def viewproperty(propertyid):
    property = Property.query.filter_by(property_id=propertyid).first()
    return render_template('viewproperty.html', property=property)

@app.route('/uploads/<filename>')
def getimage(filename):
    rootdir = os.getcwd()
    return  send_from_directory(os.path.join(rootdir,app.config['UPLOAD_FOLDER']),filename)
###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
