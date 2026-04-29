from flask import Flask , render_template , request , abort , jsonify

app = Flask(__name__)

CITIES = {
    "Gauteng": {
        "city": "Johannesburg",
        "population": 5635127
    },
    "Western Cape": {
        "city": "Cape Town",
        "population": 4618000
    },
    "KwaZulu-Natal": {
        "city": "Durban",
        "population": 3720000
    },
    "Gauteng (Pretoria)": {
        "city": "Pretoria",
        "population": 2921488
    },
    "Eastern Cape (Port Elizabeth)": {
        "city": "Port Elizabeth",
        "population": 1274000
    },
    "Free State": {
        "city": "Bloemfontein",
        "population": 759251
    },
    "Eastern Cape (East London)": {
        "city": "East London",
        "population": 478676
    },
    "Mpumalanga": {
        "city": "Nelspruit",
        "population": 322422
    },
    "Limpopo": {
        "city": "Polokwane",
        "population": 728000
    },
    "Northern Cape": {
        "city": "Kimberley",
        "population": 249446
    }
}

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/provinces')
def provinces():
    return render_template('provinces.html',provinces=CITIES)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    errors = []
    name = ""
    email = ""
    message = ""

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        if not name:
            errors.append("Name is required.")
        if not email:
            errors.append("Email is required.")
        if not message:
            errors.append("Message is required.")
        if not errors:
            return f"Worked! Name: {name}, Email: {email}, Message: {message}"
    return render_template('contact.html', errors=errors)

if __name__ == '__main__':
    app.run(debug=True)