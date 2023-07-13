import json
import datetime

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def update_content(self, new_content):
        self.content = new_content
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        return {
            'title': self.title,
            'content': self.content,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class NotesManager:
    def __init__(self):
        self.notes = []

    def load_notes_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                notes_data = json.load(file)
                self.notes = [self._create_note_from_dict(note_data) for note_data in notes_data]
        except FileNotFoundError:
            self.notes = []

    def save_notes_to_file(self, filename):
        notes_data = [note.to_dict() for note in self.notes]
        with open(filename, 'w') as file:
            json.dump(notes_data, file)

    def create_note(self, title, content):
        note = Note(title, content)
        self.notes.append(note)

    def edit_note_content(self, note_index, new_content):
        if note_index >= 0 and note_index < len(self.notes):
            note = self.notes[note_index]
            note.update_content(new_content)

    def delete_note(self, note_index):
        if note_index >= 0 and note_index < len(self.notes):
            del self.notes[note_index]

    def get_note_by_index(self, note_index):
        if note_index >= 0 and note_index < len(self.notes):
            return self.notes[note_index]
        return None

    def get_all_notes(self):
        return self.notes

    def _create_note_from_dict(self, note_data):
        note = Note(note_data['title'], note_data['content'])
        note.created_at = datetime.datetime.fromisoformat(note_data['created_at'])
        note.updated_at = datetime.datetime.fromisoformat(note_data['updated_at'])
        return note

def print_note_details(note):
    print(f"Title: {note.title}")
    print(f"Content: {note.content}")
    print(f"Created At: {note.created_at}")
    print(f"Updated At: {note.updated_at}")

def print_all_notes(notes):
    if not notes:
        print("No notes found.")
    else:
        for i, note in enumerate(notes):
            print(f"Note {i+1}:")
            print_note_details(note)
            print()

def main():
    notes_manager = NotesManager()
    notes_manager.load_notes_from_file('notes.json')

    while True:
        print("1. Create a new note")
        print("2. Edit a note")
        print("3. Delete a note")
        print("4. View all notes")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            notes_manager.create_note(title, content)
            notes_manager.save_notes_to_file('notes.json')
            print("Note created successfully.")
        elif choice == '2':
            note_index = int(input("Enter note index: ")) - 1
            new_content = input("Enter new note content: ")
            notes_manager.edit_note_content(note_index, new_content)
            notes_manager.save_notes_to_file('notes.json')
            print("Note updated successfully.")
        elif choice == '3':
            note_index = int(input("Enter note index: ")) - 1
            notes_manager.delete_note(note_index)
            notes_manager.save_notes_to_file('notes.json')
            print("Note deleted successfully.")
        elif choice == '4':
            notes = notes_manager.get_all_notes()
            print_all_notes(notes)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
