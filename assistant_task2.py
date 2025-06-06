import json
import os

class Assistant:
    def __init__(self, filename='notes.json'):
        self.filename = filename
        self.notes = self.load_notes()

    def load_notes(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []

    def save_notes(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.notes, f, indent=2, ensure_ascii=False)

    def add_note(self, note: str):
        self.notes.append(note)
        self.save_notes()

    def list_notes(self):
        return self.notes

    def search_notes(self, keyword: str):
        return [note for note in self.notes if keyword.lower() in note.lower()]
