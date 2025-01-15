import numpy as np
import pandas as pd
from langchain.embeddings import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
_embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
from phi.knowledge.pdf import PDFKnowledgeBase, PDFReader
from phi.vectordb.pgvector import PgVector

# topic = "Romeo"
def get_vector_embedding(data):
    return _embeddings.embed_documents(data)


def Get_data_by_topic(data,vector,topics=[])->pd.DataFrame:
    topic = " ,".join(topics[:-1])+ " and " + topics[-1] if len(topics)>1 else topics[0]
    query = f"Find details about {topic}"
    query_vector = _embeddings.embed_query(query)
    query_vector_reshaped = np.array(query_vector).reshape(1, -1)
    # Compute cosine similarity
    similarities = cosine_similarity(query_vector_reshaped, vector)

    # Flatten similarities and print
    similarities = similarities.flatten()
    similar_data = []
    for i, similarity in enumerate(similarities):
        if similarity > 0.5:
            document_text = data[i]  # Replace with actual data you want to retrieve
            similar_data.append({"similarity": similarity, "text": document_text})

    sutable_data_df = pd.DataFrame(similar_data)
    sutable_data_df = sutable_data_df.sort_values(by="similarity",ascending=False)
    return sutable_data_df.head()

def Get_knowledge_base(pdf_path,db_url="postgresql+psycopg://ai:ai@localhost:5532/ai"):
    pdf_knowledge_base = PDFKnowledgeBase(
        path=pdf_path,
        # Table name: ai.pdf_documents
        vector_db=PgVector(
            table_name="pdf_documents",
            db_url=db_url,
        ),
        reader=PDFReader(chunk=True),
    )

    pdf_knowledge_base.load()
    return pdf_knowledge_base