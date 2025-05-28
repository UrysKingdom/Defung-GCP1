from flask import Flask, request, jsonify

app = Flask(__name__)
notes = []

@app.route('/')
def home():
    return "Welcome to the Notes App!"

@app.route('/notes', methods=['GET', 'POST'])
def manage_notes():
    if request.method == 'POST':
        note = request.json.get('note')
        if note:
            notes.append(note)
            return jsonify({"message": "Note added", "notes": notes}), 201
        return jsonify({"error": "No note provided"}), 400
    return jsonify(notes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)