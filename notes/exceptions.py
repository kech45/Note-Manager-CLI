class NoteError(Exception):
    """Base class for note exceptions."""
    pass

class EmptyTitleError(NoteError):
    pass

class WhiteSpaceTitleError(NoteError):
    pass

class NonPositiveIDError(NoteError):
    pass

class NonExistentNoteError(NoteError):
    pass