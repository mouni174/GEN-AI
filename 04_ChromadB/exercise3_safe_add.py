import chromadb

client = chromadb.PersistentClient(path="./chroma_data")

collection = client.get_or_create_collection(
    name="safe_add_practice"
)
def safe_add(collection, id, text):
    collection.upsert(
        ids=[id],
        documents=[text]
    )
safe_add(collection, "1", "Java")
safe_add(collection, "2", "Python")
safe_add(collection, "1", "Advanced Java")
print(collection.get())