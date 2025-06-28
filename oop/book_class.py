class Book:
    def __init__(self, title, author, year):
        """Initialize a new Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Called when the book instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Human-readable string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Unambiguous string representation to recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
