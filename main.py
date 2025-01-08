import pypdf
from utils.read import read_pdf
from utils.utils import Generate_MCQ

class MCQ_Generator():
    def __init__(self,path):
        self.path = path

    def read_pdf(self):
        return pypdf.PdfReader(self.path)
    
    def Question_mcqs_generator(self,input_text, num_questions=2):
        response = Generate_MCQ(input_text,num_questions)
        return response

    def get_mcq_collection(self):
        text = self.read_pdf()
        sections = self.split_text_by_word_count(text, word_limit=300)
        questions = []
        for i, section in enumerate(sections):
            print(f"Processing section {i + 1} of {len(sections)}")
            section_questions = self.Question_mcqs_generator(section)
            questions.append({"section": i + 1, "questions": section_questions})
            
        return questions


data = read_pdf("/Users/vasudevan/Downloads/929845055557901607_2nd__pu_english_notes_by_prasha_250104_115040.pdf")
vector = get_vector_embedding(data)