import os
from flask import Flask, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/read-csv')
def read_csv():
    # Construct the path relative to the current script
    base_dir = os.path.dirname(__file__)
    csv_path = os.path.join(base_dir, 'bin', 'AbsenceList_20231115_1157.csv')
    data = pd.read_csv(csv_path)
    # Filter or process data as needed
    return jsonify(data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)

