import os
import tempfile
import unittest
from notes.manager import NotesManager
from notes.exceptions import EmptyTitleError, NonExistentNoteError, NonPositiveIDError, WhiteSpaceTitleError

class TestNotesManager(unittest.TestCase):
    def setUp(self):
        self.db_fd, self.db_path = tempfile.mkstemp(suffix=".db")
        self.manager= NotesManager(db_path=self.db_path)
        
    def tearDown(self):
        os.close(self.db_fd)
        os.remove(self.db_path)
        
    def test_add_note_empty_title(self):        
        with self.assertRaises(EmptyTitleError):
            self.manager.add_note("", "Empty title test")
            
    def test_add_note_whitespace_title(self):        
        with self.assertRaises(WhiteSpaceTitleError):
            self.manager.add_note(" ", "Empty title test")
            
    def test_add_note(self):
        expected_title = "Meeting"
        expected_content = "Discuss Q3 budget"
        self.manager.add_note(expected_title, expected_content)
        
        notes = self.manager.get_all_notes()
  
        self.assertEqual(len(notes), 1)
        self.assertEqual(notes[0].title, expected_title)
        self.assertEqual(notes[0].content, expected_content)
        
    def test_get_all_notes(self):
        expected_title_1 = "Meeting"
        expected_content_1 = "Discuss Q3 budget" 
        self.manager.add_note(expected_title_1, expected_content_1)
        
        expected_title_2 = "Lunch"
        expected_content_2 = "Have fun and eat with colleagues"
        self.manager.add_note(expected_title_2, expected_content_2)
        
        notes = self.manager.get_all_notes()
        
        self.assertEqual(len(notes), 2)
        self.assertEqual(notes[0].title, expected_title_1)
        self.assertEqual(notes[0].content, expected_content_1)
        self.assertEqual(notes[1].title, expected_title_2)
        self.assertEqual(notes[1].content, expected_content_2)
        
    def test_get_note_by_non_positive_id(self):
        with self.assertRaises(NonPositiveIDError):
            self.manager.get_note(-50)
            
    def test_get_note_by_non_existent_id(self):
        with self.assertRaises(NonExistentNoteError):
            self.manager.get_note(999)
            
    def test_get_note_valid_id(self):
        expected_title = "Meeting"
        expected_content = "Discuss Q3 budget"
        self.manager.add_note(expected_title, expected_content)
        
        note = self.manager.get_note(1)
        
        self.assertEqual(note.title, expected_title)
        self.assertEqual(note.content, expected_content)
        
    def test_delete_note_valid_id(self):
        expected_title = "Meeting"
        expected_content = "Discuss Q3 budget"
        self.manager.add_note(expected_title, expected_content)
        
        self.manager.delete_note(1)
        notes = self.manager.storage.get_all_notes()
        
        self.assertEqual(len(notes), 0)                        
