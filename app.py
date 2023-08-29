import os
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
property_listing = []


@app.route('/property_list')
def property_list():
    return render_template('property_list.html', properties=property_listing)


@app.route('/submit_property', methods=['POST'])
def submit_property():
    property_type = request.form['propertyType']
    location = request.form['location']
    address = request.form['address']
    price = float(request.form['price'])
    description = request.form['description']

    image = request.files['image']
    if image:
        filename = secure_filename(image.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(image_path)
        image_url = '/' + image_path
    else:
        image_url = None

    property_listing.append({
        'property_type': property_type,
        'location': location,
        'address': address,
        'price': price,
        'description': description,
        'image_url': image_url
    })

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
