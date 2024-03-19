import os
from flask import Flask, jsonify, request
import pandas as pd
from flask_cors import CORS
from newCSV import delCSV, restart
import glob

app = Flask(__name__)
CORS(app)

@app.route('/read-csv')
def read_csv():
    base_dir = os.path.dirname(__file__)
    csv_files = glob.glob(os.path.join(base_dir, 'bin', '*.csv'))
    csv_files.sort(key=os.path.getmtime, reverse=True)
    latest_csv_path = csv_files[0]
    data = pd.read_csv(latest_csv_path, delimiter='\t')
    return jsonify(data.to_dict(orient='records'))

@app.route('/get-klassen')
def get_klassen():
    base_dir = os.path.dirname(__file__)
    csv_files = glob.glob(os.path.join(base_dir, 'bin', '*.csv'))
    csv_files.sort(key=os.path.getmtime, reverse=True)
    latest_csv_path = csv_files[0]
    data = pd.read_csv(latest_csv_path, delimiter='\t')
    klassen = data['Klasse'].unique()
    return jsonify(klassen.tolist())

@app.route('/get-langnames', methods=['GET'])
def get_langnames():
    selected_klasse = request.args.get('klasse')
    base_dir = os.path.dirname(__file__)
    csv_files = glob.glob(os.path.join(base_dir, 'bin', '*.csv'))
    csv_files.sort(key=os.path.getmtime, reverse=True)
    latest_csv_path = csv_files[0]
    data = pd.read_csv(latest_csv_path, delimiter='\t')
    langnames = data[data['Klasse'] == selected_klasse]['Langname'].unique()
    return jsonify(langnames.tolist())


@app.route('/get-class-absences', methods=['GET'])
def get_all_absences():
   selected_klasse = request.args.get('klasse')
   base_dir = os.path.dirname(__file__)
   csv_files = glob.glob(os.path.join(base_dir, 'bin', '*.csv'))
   csv_files.sort(key=os.path.getmtime, reverse=True)
   latest_csv_path = csv_files[0]
   data = pd.read_csv(latest_csv_path, delimiter='\t')

   # Filtern der Daten für die ausgewählte Klasse
   class_data = data[data['Klasse'] == selected_klasse]

   print(f"Selected class: {selected_klasse}, Number of records found: {len(class_data)}")

   class_absences = class_data[['Langname', 'Beginndatum', 'Enddatum', 'Abwesenheitsgrund']].to_dict(orient='records')
   return jsonify(class_absences)



@app.route('/get-absences', methods=['GET'])
def get_absences():
    selected_langname = request.args.get('langname')
    base_dir = os.path.dirname(__file__)
    csv_files = glob.glob(os.path.join(base_dir, 'bin', '*.csv'))
    csv_files.sort(key=os.path.getmtime, reverse=True)
    latest_csv_path = csv_files[0]
    data = pd.read_csv(latest_csv_path, delimiter='\t')
    absences = data[data['Langname'] == selected_langname][['Beginndatum', 'Enddatum', 'Abwesenheitsgrund']]
    return jsonify(absences.to_dict(orient='records'))

@app.route('/upload-csv', methods=['POST'])
def upload_csv():
    file = request.files['file']
    base_dir = os.path.dirname(__file__)

    # delete old csv file
    delCSV()

    file_path = os.path.join(base_dir, 'bin', file.filename)
    file.save(file_path)
    return jsonify({'message': 'File uploaded successfully'})

@app.route('/restart', methods=['POST'])
def restart_csv():
    restart()
    return jsonify({'message': 'CSV file restarted successfully'})

if __name__ == '__main__':
    app.run(debug=True)

