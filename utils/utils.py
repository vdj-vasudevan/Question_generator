import os
from phi.agent import Agent
from phi.model.mistral import MistralChat

API_KEY = os.getenv("API_KEY")

def Generate_content(prompt):
    agent = Agent(
        model=MistralChat(
            id="mistral-large-latest",
            api_key=API_KEY,
            # show_tool_calls=True,
            # markdown=True,
            instructions=["Only Use the Given input text,Dont go out of the input"],
            # debug_mode=True,
        ),
        markdown=True
    )
    agent.print_response(prompt)
    return eval(agent.get_chat_history())
input_text = """William Shakespeare is an English playwright and poet, widely regarded as the greatest writer in the English Language and the world’s pre-eminent dramatist. He is well-known to the world through his timeless characters that are universal in their appeal. The themes that he deals with also touch the human lives across the globe. The extracts from William Shakespeare’s play “Romeo and Juliet “express the implicit feelings of Romeo and and Juliet for each other.
# He compares Juliet’s beauty to nature. Romeo says that even the bright light of a torch would look dull before the brightness of Juliet. It looks like she hangs on the cheek of night. Romeo says that the beauty of Juliet is like a jewel which is hung in the ear of an African woman.
# """
num_questions=2
prompt= f"""
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

output_response = Generate_content(prompt)

print(output_response)
