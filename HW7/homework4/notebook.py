class Notebook:
    """
    Class representing a collection of notes that can be modified.
    """
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        """Add a note to the notebook."""
        if not isinstance(note, str):
            raise TypeError("Note must be a string")
        self.notes.append(note)

    def get_note(self, index):
        """Retrieve a note by its index."""
        if index >= len(self.notes) or index < 0:
            raise IndexError("Note index out of range")
        return self.notes[index]

    def total_notes(self):
        """Return the total number of notes."""
        return len(self.notes)

    def remove_note(self, index):
        """Remove a note by its index."""
        if index >= len(self.notes) or index < 0:
            raise IndexError("Note index out of range")
        self.notes.pop(index)

    def clear(self):
        """Remove all notes."""
        self.notes = []

    def find(self, word):
        """Find all notes containing a given word."""
        if not isinstance(word, str):
            raise TypeError("Word must be a string")
        matching_notes = []
        for note in self.notes:
            if word in note:
                matching_notes.append(note)
        return matching_notes

    def __eq__(self, other):
        """Check equality based on notes."""
        if isinstance(other, Notebook):
            return self.notes == other.notes
        return False

    def __str__(self):
        """String representation."""
        return "\n".join(self.notes)

    def save_to_file(self, filename):
        """Save notes to a file."""
        with open(filename, 'w') as f:
            for note in self.notes:
                f.write(note + "\n")

    def load_from_file(self, filename):
        """Load notes from a file."""
        with open(filename, 'r') as f:
            self.notes = f.read().splitlines()
