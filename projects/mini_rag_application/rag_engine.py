import numpy as np

class MiniRag:
    def __init__(self, filepath:str):
        self.filepath = filepath
        self.chunks = []
        self.load_and_chunk()

    def load_and_chunk(self):
        """This is step 1 and 2, reading the text fie and splitting into chunks"""
        print("[INFO] Loading document corpus....")
        with open(self.filepath, 'r', encoding="utf-8") as f:
            content = f.read()

        # Split into chunks by double newlines
        raw_chunks = content.split("\n\n")
        self.chunks = [chunk.strip() for chunk in raw_chunks if chunk.strip()]
        print(f"[INFO] Succesfully created {len(self.chunks)} document chunks.")

    def mock_embed(self, text:str) -> np.ndarray:
        """
        Simulating an embedded model 
        In real apps, you'd use OpenAi embeddings or sentence transformers.
        Here, we create a psuedo-embedding based on keyword presence to demonstrate math search.
        """
        # Vector space layout : [remote_work, pto_vacation, travel_expense]
        vector = np.zeros(3, dtype=float)
        text_lower = text.lower()

        if "remote" in text_lower or "hours" in text_lower:
            vector[0] += 1.0
        if "pto" in text_lower or "vacation" in text_lower:
            vector[1] += 1.0
        if "expense" in text_lower or "travel" in text_lower or "hotel" in text_lower:
            vector[2] += 1.0

        # Add a tiny random noise to simulate high dimensional dense embeddings
        np.random.seed(len(text))
        vector += np.random.uniform(0.0, 0.1, size=3)

        # Normalize vector (L2 norm = 1)
        norm = np.linalg.norm(vector)
        if norm > 0:
            vector = vector / norm
        return norm

    def retrieve(self, query:str, top_k:int = 1) -> list[str]:
        """Step 4: Semantic Retrieval using Cosine Similarity ."""
        print(f"\n[QUERY] Searching for :'{query}'")
        query_vector = self.mock_embed(query)

        similarities = []
        for chunk in self.chunks:
            chunk_vector = self.mock_embed(chunk)
            # Compute Cosine Similarity (dot product of normalized vectors)
            sim = np.dot(query_vector, chunk_vector)
            similarities.append((sim, chunk))

        # Sort by highest similarity score
        similarities.sort(key=lambda x: x[0], reverse=True)

        # Return top-k chunks
        top_results = [chunk for sim, chunk in similarities[:top_k]]
        return top_results

if __name__ == "__main__":
    rag = MiniRag("cropus.txt")

    # Test query targeting the travel expense section
    query = "How much I can spend on hotel rooms during business travel"
    retrieved_chunks = rag.retrieve(query, top_k=1)

    print("\n---RETREIEVED CONTEXT---")
    for i, context in enumerate(retrieved_chunks):
        print(f"Chunk {i+1}:\n{context}")







        

