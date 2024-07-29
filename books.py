import json

books = [
    {
        "nume": "Pride and Prejudice",
        "autor": "Jane Austen"
    },
    {
        "nume": "To Kill a Mockingbird",
        "autor": "Harper Lee"
    },
    {
        "nume": "1984",
        "autor": "George Orwell"
    },
    {
        "nume": "The Great Gatsby",
        "autor": "F. Scott Fitzgerald"
    },
    {
        "nume": "Moby-Dick",
        "autor": "Herman Melville"
    }
]

with open('books.json', 'w') as f:
    json.dump(books, f, indent=4)
