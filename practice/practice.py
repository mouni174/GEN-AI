import chromadb

client = chromadb.PersistentClient(path="./chroma_data")

collection = client.get_or_create_collection(
    name="practice_collection"
)

# Add 5 documents
collection.add(
    ids=["1", "2", "3", "4", "5"],
    documents=[
        "Java",
        "Python",
        "SQL",
        "JavaScript",
        "MongoDB"
    ]
)

print("Before upsert:", collection.count())

# Exercise 1: upsert
collection.upsert(
    ids=["1", "3", "6"],
    documents=[
        "Advanced Java",
        "Advanced SQL",
        "Python Collections"
    ]
)

print("After upsert:", collection.count())