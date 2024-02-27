import os
from flask import Flask, jsonify, request
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/read-csv')
def read_csv():
    # Construct the path relative to the current script
    base_dir = os.path.dirname(__file__)
    csv_path = os.path.join(base_dir, 'bin', 'AbsenceList_20231115_1157.csv')
    data = pd.read_csv(csv_path, delimiter='\t')
    # Filter or process data as needed
    return jsonify(data.to_dict(orient='records'))

@app.route('/get-klassen')
def get_klassen():
    base_dir = os.path.dirname(__file__)
    csv_path = os.path.join(base_dir, 'bin', 'AbsenceList_20231115_1157.csv')
    data = pd.read_csv(csv_path, delimiter='\t')
    klassen = data['Klasse'].unique()  # Assuming 'Klasse' is the column name
    return jsonify(klassen.tolist())

@app.route('/get-langnames', methods=['GET'])  # Define a new route '/get-langnames'
def get_langnames():
    selected_klasse = request.args.get('klasse')
    base_dir = os.path.dirname(__file__)
    csv_path = os.path.join(base_dir, 'bin', 'AbsenceList_20231115_1157.csv')
    data = pd.read_csv(csv_path, delimiter='\t')
    langnames = data[data['Klasse'] == selected_klasse]['Langname'].unique()
    return jsonify(langnames.tolist())

@app.route('/get-absences', methods=['GET'])
def get_absences():
    selected_langname = request.args.get('langname')
    base_dir = os.path.dirname(__file__)
    csv_path = os.path.join(base_dir, 'bin', 'AbsenceList_20231115_1157.csv')
    data = pd.read_csv(csv_path, delimiter='\t')
    absences = data[data['Langname'] == selected_langname][['Beginndatum', 'Enddatum', 'Abwesenheitsgrund']]
    return jsonify(absences.to_dict(orient='records'))


if __name__ == '__main__':
    app.run(debug=True)

