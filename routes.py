from flask import Flask, request, jsonify
from controllers.notes_controller import NotesApi

app = Flask(__name__)

notes_api = NotesApi('data.csv')

@app.route('/notes', methods=['POST'])
def create_note():
    title = request.json['title']
    content = request.json['content']
    notes_api.create_note(title, content)
    return jsonify({'message': 'Note created successfully'}), 201

@app.route('/notes', methods=['GET'])
def read_all_notes():
    return jsonify(notes_api.read_all_notes()), 200

@app.route('/notes/<string:title>', methods=['GET'])
def read_note(title):
    note = notes_api.read_note(title)
    if note:
        return jsonify(note), 200
    else:
        return jsonify({'message': 'Note not found'}), 404

@app.route('/notes/<string:title>', methods=['PUT'])
def update_note(title):
    new_title = request.json['title']
    new_content = request.json['content']
    if notes_api.update_note(title, new_title, new_content):
        return jsonify({'message': 'Note updated successfully'}), 200
    else:
        return jsonify({'message': 'Note not found'}), 404

@app.route('/notes/<string:title>', methods=['DELETE'])
def delete_note(title):
    if notes_api.delete_note(title):
        return jsonify({'message': 'Note deleted successfully'}), 200
    else:
        return jsonify({'message': 'Note not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)