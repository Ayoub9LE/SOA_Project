from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/soa'  # Replace with your MySQL database URI
db = SQLAlchemy(app)

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    prenom = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    role = db.Column(db.String(50))
    demande_mission = db.relationship('demande_mission', backref='users_demande_mission', lazy=True)
    demande_remboursement = db.relationship('demande_remboursement', backref='users_demande_remboursement', lazy=True)

class demande_mission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_professeur = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
    destination = db.Column(db.String(255))
    description = db.Column(db.Text)
    dateDepartPrevu = db.Column(db.Date)
    dateRetourPrevu = db.Column(db.Date)
    dateDepartReel = db.Column(db.Date)
    dateRetourReel = db.Column(db.Date)
    statut = db.Column(db.String(50))
    statut_remboursement = db.Column(db.String(50))

class demande_remboursement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code_mission = db.Column(db.Integer, db.ForeignKey('demande_mission.id'), unique=True)
    id_demandeur = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
    frais = db.Column(db.DECIMAL(10, 2))
    budgetInitial = db.Column(db.DECIMAL(10, 2))
    montantRembourse = db.Column(db.DECIMAL(10, 2))
    validationFrais = db.Column(db.Boolean)
    validation = db.Column(db.Boolean)
    statut = db.Column(db.String(50))

# Additional tables and models for transport, insertMission, and others can be added similarly.

# API Endpoints

# Insert a new demande_mission
@app.route('/insertdemande_mission', methods=['POST'])
def insert_demande_mission():
    data = request.json
    new_demande_mission = demande_mission(**data)
    db.session.add(new_demande_mission)
    db.session.commit()
    return jsonify({'message': 'Demande Mission inserted successfully'})

# Insert a new demande_remboursement
@app.route('/Insertdemande_remboursement', methods=['POST'])
def insert_demande_remboursement():
    data = request.json
    new_demande_remboursement = demande_remboursement(**data)
    db.session.add(new_demande_remboursement)
    db.session.commit()
    return jsonify({'message': 'Demande Remboursement inserted successfully'})

@app.route('/updateEtatDemande/<int:demande_id>', methods=['PUT'])
def update_etat_demande(demande_id):
    data = request.json
    demande = demande_mission.query.get(demande_id)

    if not demande:
        return jsonify({'error': 'demande_mission not found'}), 404

    demande.statut = data.get('new_status', demande.statut)
    db.session.commit()

    return jsonify({'message': 'demande_mission updated successfully'})


# Update the dateRetourReel of a specific demande_mission
@app.route('/updateDateHeureRetourEffectiveMission/<int:demande_id>', methods=['PUT'])
def update_date_heure_retour_effective_mission(demande_id):
    data = request.json
    demande = demande_mission.query.get(demande_id)

    if not demande:
        return jsonify({'error': 'demande_mission not found'}), 404

    demande.dateRetourReel = data.get('new_date', demande.dateRetourReel)
    db.session.commit()

    return jsonify({'message': 'demande_mission updated successfully'})


# Update the statut of a specific demande_remboursement
@app.route('/updateEtatRemboursement/<int:remboursement_id>', methods=['PUT'])
def update_etat_remboursement(remboursement_id):
    data = request.json
    remboursement = demande_remboursement.query.get(remboursement_id)

    if not remboursement:
        return jsonify({'error': 'demande_remboursement not found'}), 404

    remboursement.statut = data.get('new_status', remboursement.statut)
    db.session.commit()

    return jsonify({'message': 'demande_remboursement updated successfully'})


if __name__ == '__main__':
    app.run(debug=True)
