"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash
from .forms import PropertyForm
from werkzeug.utils import secure_filename
from .models import Properties

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
    return render_template('about.html', name="Mary Jane")


@app.route('/property', methods=['POST', 'GET'])
def add_property():
    """Render the website's add property form."""
    form = PropertyForm()

    if request.method == 'POST' and form.validate_on_submit():
        title = form.title.data
        bedrooms = form.bedrooms.data
        bathrooms = form.bathrooms.data
        location = form.location.data
        price = form.price.data
        property_type = form.property_type.data
        description = form.description.data
        photo = form.photo.data
        
        filename = secure_filename(photo.filename)
        
        new_property = Properties(title, bedrooms, bathrooms, location, price, property_type, description, filename)
        db.session.add(new_property)
        db.session.commit()

        photo.save(os.path.join(
            app.config['UPLOAD_FOLDER'], filename
        ))
        
        flash('The new property has been successfully added.', 'success')
        return redirect(url_for('display_properties'))

    # flash("There was an error submitting your form.", 'danger')
    return render_template('property.html', form=form, template="form-template")

@app.route('/properties')
def display_properties():
    """Render the website's properties page."""
    properties = Properties.query.all()
    
    return render_template('properties.html', properties=properties)


@app.route('/property/<propertyid>', methods=['POST', 'GET'])
def view_property(propertyid):
    """Displays information on individual properties."""
    if request.method == 'GET':
        listing = Properties.query.get(int(propertyid))

        return render_template('view_property.html', listing=listing)
    return redirect(url_for('properties'))

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
