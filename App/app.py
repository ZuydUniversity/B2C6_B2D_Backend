from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/patients', methods=['POST'])
def create_patient():
    patient = request.json
    # Hier zou je logica staan om de patiënt op te slaan in een database
    print(f"Patient created: {patient}")

    # Als het opslaan van de patiënt succesvol is, voer je de unit tests uit
    try:
        result = subprocess.run(['python', 'test_script.py'], capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(f'Tests failed: {result.stderr}')
        return jsonify({"message": "Patient created and tests passed", "test_output": result.stdout}), 201
    except Exception as e:
        return jsonify({"message": "Patient created but tests failed", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
