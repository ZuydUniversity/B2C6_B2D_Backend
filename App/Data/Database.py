from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost:3306/db2"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/db2"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Initialize the database
db = SQLAlchemy(app)

# Import models
from .DatabaseModels import Patient

# Route to get all patients
@app.route('/api/patients', methods=['GET'])
def get_patients():
    patients = Patient.query.all()
    return jsonify([{
        'id': patient.id,
        'name': patient.name,
        'address': patient.address,
        'postalZip': patient.postalZip,
        'phone': patient.phone,
        'email': patient.email
    } for patient in patients])

# Route to create a new patient
@app.route('/api/patients', methods=['POST'])
def create_patient():
    data = request.get_json()
    new_patient = Patient(
        name=data['name'],
        address=data['address'],
        postalZip=data['postalZip'],
        phone=data['phone'],
        email=data['email']
    )
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({
        'id': new_patient.id,
        'name': new_patient.name,
        'address': new_patient.address,
        'postalZip': new_patient.postalZip,
        'phone': new_patient.phone,
        'email': new_patient.email
    }), 201

# Route to get a specific patient by ID
@app.route('/api/patients/<int:id>', methods=['GET'])
def get_patient(id):
    patient = Patient.query.get(id)
    if patient is None:
        return jsonify({'error': 'Patient not found'}), 404
    return jsonify({
        'id': patient.id,
        'name': patient.name,
        'address': patient.address,
        'postalZip': patient.postalZip,
        'phone': patient.phone,
        'email': patient.email
    })

# Route to update a patient by ID
@app.route('/api/patients/<int:id>', methods=['PUT'])
def update_patient(id):
    data = request.get_json()
    patient = Patient.query.get(id)
    if patient is None:
        return jsonify({'error': 'Patient not found'}), 404

    patient.name = data.get('name', patient.name)
    patient.address = data.get('address', patient.address)
    patient.postalZip = data.get('postalZip', patient.postalZip)
    patient.phone = data.get('phone', patient.phone)
    patient.email = data.get('email', patient.email)
    db.session.commit()
    return jsonify({
        'id': patient.id,
        'name': patient.name,
        'address': patient.address,
        'postalZip': patient.postalZip,
        'phone': patient.phone,
        'email': patient.email
    })

# Route to delete a patient by ID
@app.route('/api/patients/<int:id>', methods=['DELETE'])
def delete_patient(id):
    patient = Patient.query.get(id)
    if patient is None:
        return jsonify({'error': 'Patient not found'}), 404

    db.session.delete(patient)
    db.session.commit()
    return jsonify({'message': 'Patient deleted'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
