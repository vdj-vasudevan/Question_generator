from phi.knowledge.pdf import PDFKnowledgeBase, PDFReader
from phi.vectordb.pgvector import PgVector
from phi.agent import Agent
from phi.model.mistral import MistralChat
import os

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
API_KEY = os.getenv("API_KEY")

pdf_knowledge_base = PDFKnowledgeBase(
    path="/Users/vasudevan/Downloads/Digital_Fluency_Module3_asd.pdf",
    # Table name: ai.pdf_documents
    vector_db=PgVector(
        table_name="pdf_documents",
        db_url="postgresql+psycopg://ai:ai@localhost:5532/ai",
    ),
    reader=PDFReader(chunk=True),
)

pdf_knowledge_base.load()

agent = Agent(
        model=MistralChat(
            id="mistral-large-latest",
            api_key=API_KEY,
            # show_tool_calls=True,
            # markdown=True,
            # instructions=["Only Use the Given input text,Dont go out of the input"],
            # debug_mode=True,
        ),
        knowledge_base=pdf_knowledge_base,
        markdown=True
    )
agent.knowledge.load(recreate=False)

agent.print_response("Ask me about something from the Digital_Fluency_Module3_asd which is a pdf document")

print("done")
