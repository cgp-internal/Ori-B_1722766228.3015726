from models.notes_model import Notes

class NotesApi:
    def __init__(self, filename):
        self.notes = Notes(filename)

    def create_note(self, title, content):
        self.notes.create_note(title, content)

    def read_note(self, title):
        return self.notes.read_note(title)

    def update_note(self, title, new_title, new_content):
        return self.notes.update_note(title, new_title, new_content)

    def delete_note(self, title):
        return self.notes.delete_note(title)

    def read_all_notes(self):
        return self.notes.data