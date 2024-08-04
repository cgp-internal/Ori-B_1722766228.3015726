import csv
import os

class Notes:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.read_csv()

    def read_csv(self):
        try:
            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # skip header
                return list(reader)
        except FileNotFoundError:
            return []

    def write_csv(self, data):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["title", "content"])  # header
            writer.writerows(data)

    def create_note(self, title, content):
        new_note = [title, content]
        self.data.append(new_note)
        self.write_csv(self.data)

    def read_note(self, title):
        for note in self.data:
            if note[0] == title:
                return note
        return None

    def update_note(self, title, new_title, new_content):
        for i, note in enumerate(self.data):
            if note[0] == title:
                self.data[i] = [new_title, new_content]
                self.write_csv(self.data)
                return
        return None

    def delete_note(self, title):
        for i, note in enumerate(self.data):
            if note[0] == title:
                del self.data[i]
                self.write_csv(self.data)
                return
        return None