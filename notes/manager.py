from notes import storage
class Note:
    def __init__(self, id, title : str, content : str, created_at):
        self.id = id
        self.title = title
        self.content = content
        self.created_at = created_at
        
    def __repr__(self):
        return (f"ID: {self.id}\n"
                f"Title: {self.title}\n"
                f"Content: {self.content}\n"
                f"Created at: {self.created_at}\n"
        )
        
def add_note(title : str, content : str):
    if not title.strip():
        raise ValueError("Title cannot be empty!")
    storage.add_note(title, content)
    
def get_all_notes():
    notes = []
    for note in storage.get_all_notes():
        notes.append(Note(note[0], note[1], note[2], note[3]))
    return notes

def get_note(note_id : int):
    note = storage.get_note_by_given_id(note_id)
    if note is None:
        raise ValueError("Note with given ID doesn't exist")
    return Note(note[0], note[1], note[2], note[3])

def delete_note(note_id : int):
    get_note(note_id)
    storage.delete_note_by_given_id(note_id)
    
    