import pypdf
from utils.read import read_pdf
from utils.utils import Generate_MCQ
from utils.vector_db import get_vector_embedding,Get_data_by_topic,Get_knowledge_base

class MCQ_Generator():
    def __init__(self,path=None):
        self.data = read_pdf(path)
        self.vector = None
        self.availble_questions = []

    def Question_mcqs_generator(self,input_text,pdf_knowledge_base, num_questions=1,):
        response = Generate_MCQ(input_text,num_questions,self.availble_questions,pdf_knowledge_base)
        return response

    # def get_mcq_collection(self,topics):
    #     # data = read_pdf(self.path)
    #     self.vector = get_vector_embedding(self.data)
    #     sections_df = Get_data_by_topic(self.data,self.vector,topics)
    #     sections = sections_df["text"].tolist()
    #     # sections = self.split_text_by_word_count(text, word_limit=300)
    #     questions = []
    #     for i, section in enumerate(sections):
    #         print(f"Processing section {i + 1} of {len(sections)}")
    #         section_questions = self.Question_mcqs_generator(section)
    #         questions.extend(section_questions)
    #         self.availble_questions.extend([i["Question"] for i in section_questions])
            
    #     return questions
    


path = "/Users/vasudevan/Downloads/929845055557901607_2nd__pu_english_notes_by_prasha_250104_115040.pdf"
mcq = MCQ_Generator(path)
# pdf_path="/Users/vasudevan/Downloads/Digital_Fluency_Module3_asd.pdf"
topics=["Romeo","Juliet","william shakespeare"]

input_text = "Topic related to "+  " ,".join(topics[:-1])+ " and " + topics[-1] if len(topics)>1 else topics[0]
pdf_knowledge_base = Get_knowledge_base(path)
Questions = mcq.Question_mcqs_generator(input_text,pdf_knowledge_base, num_questions=15)

print(Questions)

print("Done")
