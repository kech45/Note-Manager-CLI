import os
import tempfile
import unittest
from notes.manager import NotesManager
from notes.manager import Note

class TestNotesManager(unittest.TestCase):
    def setUp(self):
        self.db_fd, self.db_path = tempfile.mkstemp(suffix=".db")
        self.manager= NotesManager(db_path=self.db_path)
        
    def test_add_note_empty_title(self):        
        with self.assertRaises(ValueError):
            self.manager.add_note("", "Empty title test")
            
    def test_add_note(self):
        self.manager.add_note("Meeting", "Discuss Q3 budget")
        
        noteTuples = self.manager.storage.get_all_notes()
        notes = []
        
        for noteTuple in noteTuples:
            notes.append(Note(noteTuple[0],noteTuple[1], noteTuple[2], noteTuple[3]))
            
        self.assertEqual(len(notes), 1)
        self.assertEqual(notes[0].title, "Meeting", "The title doesn't match")
        
    def test_get_all_notes(self):
        self.manager.storage.add_note("Meeting", "Discuss Q3 budget")
        self.manager.storage.add_note("Lunch", "Have fun and eat with colleagues")
        
        notes = self.manager.get_all_notes()
        
        self.assertEqual(len(notes), 2)
        self.assertEqual(notes[0].title, "Meeting", "The title doesn't match")
        self.assertEqual(notes[1].content, "Have fun and eat with colleagues", "The content doesn't match")
        
    def test_get_note_by_non_positive_id(self):
        with self.assertRaises(ValueError):
            self.manager.get_note(-50)
            
    def test_get_note_by_non_existent_id(self):
        with self.assertRaises(ValueError):
            self.manager.get_note(999)
            
    def test_get_note_valid_id(self):
        self.manager.storage.add_note("Meeting", "Discuss Q3 budget")
        
        note = self.manager.get_note(1)
        
        self.assertEqual(note.title, "Meeting", "The title doesn't match")
        self.assertEqual(note.content, "Discuss Q3 budget", "The content doesn't match")
        
    def test_delete_note_valid_id(self):
        self.manager.storage.add_note("Meeting", "Discuss Q3 budget")
        self.manager.delete_note(1)
        
        notes = self.manager.storage.get_all_notes()
        
        self.assertEqual(len(notes), 0)
         
    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(self.db_path)
    
    
