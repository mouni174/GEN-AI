import chromadb

client = chromadb.PersistentClient(path="./chroma_data")

collection = client.get_or_create_collection(
    name="delete_practice"
)
collection.add(
    ids=["1", "2", "3", "4"],
    documents=[
        "Java",
        "Python",
        "SQL",
        "MongoDB"
    ],
    metadatas=[
        {"category": "programming"},
        {"category": "programming"},
        {"category": "database"},
        {"category": "database"}
    ]
)
collection.delete(
    where={"category": "database"}
)
print(collection.count())