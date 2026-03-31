from notes.storage import Storage
from notes.exceptions import EmptyTitleError, NonExistentNoteError, WhiteSpaceTitleError, NonPositiveIDError
class Note:
    
    def __init__(self, id, title : str, content : str, created_at):
        self.id = id
        self.title = title
        self.content = content
        self.created_at = created_at
        
    def __str__(self):
        return (f"ID: {self.id}\n"
                f"Title: {self.title}\n"
                f"Content: {self.content}\n"
                f"Created at: {self.created_at}\n"
        )

class NotesManager:
    
    def __init__(self, db_path="data/note_manager.db"):
        self.storage = Storage(db_path)
               
    def add_note(self, title : str, content : str):
        """
        Add a new note to the database.

        Args:
            title (string): Title of the note.
            content (string): Content of the note.

        Raises:
            EmptyTitleError: If the title is empty.
            WhiteSpaceTitleError: If the title contains only whitespaces.
        """
        if not title:
            raise EmptyTitleError("Title cannot be empty")
        if title.isspace():
            raise WhiteSpaceTitleError("Title contains only whitespaces")
        self.storage.add_note(title, content)
        
    def get_all_notes(self):
        """
        Retrieve all notes from the database.
        
        Returns:
            A list of Note objects.
        """
        notes = []
        for note in self.storage.get_all_notes():
            notes.append(Note(note[0], note[1], note[2], note[3]))
        return notes

    def get_note(self, note_id : int):
        """
        Retrieve a note from the database.

        Args:
            note_id (int): Id of the note to be retrieved.

        Raises:
            NonPositiveIDError: If the ID is zero or negative.
            NonExistentNoteError: If no note with the given ID exists.

        Returns:
            A Note object matching the given ID.
        """
        if note_id <= 0:
            raise NonPositiveIDError("ID must be a positive number")
        note = self.storage.get_note_by_given_id(note_id)
        if note is None:
            raise NonExistentNoteError("Note with given ID doesn't exist")
        return Note(note[0], note[1], note[2], note[3])

    def delete_note(self, note_id : int):
        """
        Delete a note from the database.

        Args:
            note_id (int): Id of the note to be deleted.

        Raises:
            NonPositiveIDError: If the ID is zero or negative.
            NonExistentNoteError: If no note with the given ID exists.
        """
        self.get_note(note_id)
        self.storage.delete_note_by_given_id(note_id)