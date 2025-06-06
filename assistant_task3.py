import json
import os
from threading import Lock

class Assistant:
    def __init__(self, filename='notes.json'):
        self.filename = filename
        self.lock = Lock()
        self.notes = self.load_notes()

    def load_notes(self):
        with self.lock:
            if not os.path.exists(self.filename):
                self.save_notes([])
                return []
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                self.save_notes([])
                return []

    def save_notes(self, notes=None):
        with self.lock:
            if notes is not None:
                self.notes = notes
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(self.notes, f, indent=2, ensure_ascii=False)

    def add_note(self, note: str):
        with self.lock:
            self.notes.append(note)
            self.save_notes()

    def list_notes(self):
        return self.notes

    def search_notes(self, keyword: str):
        return [note for note in self.notes if keyword.lower() in note.lower()]
