import sys
import traceback
import argparse
from notes.manager import NotesManager


def main():
    manager = NotesManager()
    parser = argparse.ArgumentParser(description="A simple command-line note manager")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("list", help="List all notes")

    add_cmd = subparsers.add_parser("add", help="Add a new note")
    add_cmd.add_argument("title", help="Title of the note to be added")
    add_cmd.add_argument("content", help="Content of the note to be added")

    show_cmd = subparsers.add_parser("show", help="Show a note with given ID")
    show_cmd.add_argument("id", type=int, help="ID of the note to be shown")

    delete_cmd = subparsers.add_parser("delete", help="Delete a note with given ID")
    delete_cmd.add_argument("id", type=int, help="ID of the note to be deleted")

    args = parser.parse_args()

    try:
        if args.command == "add":
            manager.add_note(args.title, args.content)
            print("Note added successfully!")

        elif args.command == "list":
            notes = manager.get_all_notes()
            for note in notes:
                print(f"{note.id} - {note.title}")

        elif args.command == "show":
            note = manager.get_note(args.id)
            print(note)

        elif args.command == "delete":
            manager.delete_note(args.id)
            print("Note deleted successfully!")
        else:
            parser.print_help()
    except Exception as e:
        print("Unexpected error")
        traceback.print_exc()
        sys.exit(1)
