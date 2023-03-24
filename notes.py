import json
import datetime

NOTES_FILE = 'notes.json'

def read_notes():
    """Read notes from file"""
    try:
        with open(NOTES_FILE, 'r') as f:
            notes = json.load(f)
    except FileNotFoundError:
        notes = []
    return notes

def save_notes(notes):
    """Save notes to file"""
    with open(NOTES_FILE, 'w') as f:
        json.dump(notes, f, indent=4)

def add_note():
    """Add a new note"""
    title = input('Title: ')
    body = input('Body: ')
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    note = {
        'id': len(notes) + 1,
        'title': title,
        'body': body,
        'timestamp': timestamp
    }
    notes.append(note)
    save_notes(notes)
    print('Note added successfully!')

def view_notes():
    """View all notes"""
    if not notes:
        print('No notes found!')
    else:
        for note in notes:
            print(f"{note['id']}: {note['title']} ({note['timestamp']})")
            print(note['body'])
            print()

def edit_note():
    """Edit an existing note"""
    note_id = int(input('Note ID: '))
    for note in notes:
        if note['id'] == note_id:
            title = input('Title: ')
            body = input('Body: ')
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            note['title'] = title
            note['body'] = body
            note['timestamp'] = timestamp
            save_notes(notes)
            print('Note edited successfully!')
            break
    else:
        print('Note not found!')

def delete_note():
    """Delete an existing note"""
    note_id = int(input('Note ID: '))
    for i, note in enumerate(notes):
        if note['id'] == note_id:
            del notes[i]
            save_notes(notes)
            print('Note deleted successfully!')
            break
    else:
        print('Note not found!')

# Main loop
notes = read_notes()
while True:
    print()
    print('1. Add a new note')
    print('2. View all notes')
    print('3. Edit an existing note')
    print('4. Delete an existing note')
    print('5. Exit')
    choice = input('Enter your choice: ')
    if choice == '1':
        add_note()
    elif choice == '2':
        view_notes()
    elif choice == '3':
        edit_note()
    elif choice == '4':
        delete_note()
    elif choice == '5':
        break
    else:
        print('Invalid choice. Try again.')
