from notebook import Notebook

def main():
    """
    Driver function for the program.
    """
    n = Notebook()
    n.add_note("Hello world")
    n.add_note("Hello again")
    n.add_note("Goodbye")
    print(n)
    print(n.total_notes())
    print(n.get_note(1))
    n.remove_note(1)
    print(n)
    print(n.find("Hello"))
    n.save_to_file("notes.txt")
    n.clear()
    print(n)
    n.load_from_file("notes.txt")
    print(n)


if __name__ == "__main__":
    main()
