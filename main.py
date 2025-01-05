import pypdf
class MCQ_Generator():
    def __init__(self,path):
        self.path = path

    def read_pdf(self):
        return pypdf.PdfReader(self.path)
    
    def Question_mcqs_generator(self,input_text, num_questions=2):
        prompt = f"""
        You are an AI assistant helping the user generate multiple-choice questions (MCQs) based on the following text:
        '{input_text}'
        Please generate {num_questions} MCQs from the text. Each question should have:
        - A clear question
        - Four answer options (labeled A, B, C, D)
        - The correct answer clearly indicated
        Format:
        ## MCQ
        Question: [question]
        A) [option A]
        B) [option B]
        C) [option C]
        D) [option D]
        Correct Answer: [correct option]
        """
        response = model.generate_content(prompt).text.strip()
        return response
    
    def split_text_by_word_count(self,text, word_limit=300):
        words = text.split()
        sections = [' '.join(words[i:i + word_limit]) for i in range(0, len(words), word_limit)]
        return sections

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