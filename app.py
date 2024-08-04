from flask import Flask, request, jsonify
from controllers.notes_controller import NotesApi

app = Flask(__name__)

notes_filename = 'data.csv'
notes_api = NotesApi(notes_filename)

@app.route('/notes', methods=['POST'])
def create_note():
    data = request.get_json()
    notes_api.create_note(data['title'], data['content'])
    return jsonify({'message': 'Note created successfully'})

@app.route('/notes', methods=['GET'])
def read_all_notes():
    return jsonify([{'title': note[0], 'content': note[1]} for note in notes_api.read_all_notes()])

@app.route('/notes/<title>', methods=['GET'])
def read_note(title):
    note = notes_api.read_note(title)
    if note:
        return jsonify({'title': note[0], 'content': note[1]})
    else:
        return jsonify({'message': 'Note not found'}), 404

@app.route('/notes/<title>', methods=['PUT'])
def update_note(title):
    data = request.get_json()
    notes_api.update_note(title, data['title'], data['content'])
    return jsonify({'message': 'Note updated successfully'})

@app.route('/notes/<title>', methods=['DELETE'])
def delete_note(title):
    notes_api.delete_note(title)
    return jsonify({'message': 'Note deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)