import os
from phi.agent import Agent
from phi.model.mistral import MistralChat

API_KEY = os.getenv("API_KEY")

def Generate_MCQ(input_text,num_questions,level="Medium"):
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
    prompt = f"""
        You are an AI assistant helping the user generate multiple-choice questions (MCQs) based on the following text:
        '{input_text}'
        Please generate {num_questions} with Category like Easy,Medium and Hard kindly use {level} category to generate MCQs from the text. Each question should have:
        - A clear question
        - Four answer options (labeled A, B, C, D)
        - The correct answer clearly indicated
        Expexted output json format:        
        """+"""[{"1":{"mcq":{"Question":"Actual Question;A)Option;B)Option;C)Option;D)Option"},{"Answer":"*)Option"}}}] """
    agent.print_response(prompt)
    output = eval(agent.get_chat_history())
    output = eval(output[1]["content"].strip("`").strip("json").strip("\n"))
    return output


## Example for Generate_MCQ
# input_text = """William Shakespeare is an English playwright and poet, widely regarded as the greatest writer in the English Language and the world’s pre-eminent dramatist. He is well-known to the world through his timeless characters that are universal in their appeal. The themes that he deals with also touch the human lives across the globe. The extracts from William Shakespeare’s play “Romeo and Juliet “express the implicit feelings of Romeo and and Juliet for each other.
# He compares Juliet’s beauty to nature. Romeo says that even the bright light of a torch would look dull before the brightness of Juliet. It looks like she hangs on the cheek of night. Romeo says that the beauty of Juliet is like a jewel which is hung in the ear of an African woman.
# """
# num_questions=2

# output_response = Generate_MCQ(input_text,num_questions)

# print(output_response)


def Generate_QA_1(input_text,num_questions,level="Medium"):
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
    prompt = f"""
        You are an AI assistant helping the user generate questions & answer with two to three sentences each from the given text:
        '{input_text}'
        Please generate {num_questions} with Category like Easy,Medium and Hard kindly use {level} category to generate Questioon and answer with 2-3 Sentences from the text. Each question should have:
        - A clear question
        - A clear answer with 2-3 sentences
        Expexted output json format:        
        """+"""[{"1":"Question":"Actual Question},{"Answer":"Actual Answer"}}}] """
    agent.print_response(prompt)
    output = eval(agent.get_chat_history())
    output = eval(output[1]["content"].strip("`").strip("json").strip("\n"))
    return output


# # Example for Generate_MCQ
# input_text = """William Shakespeare is an English playwright and poet, widely regarded as the greatest writer in the English Language and the world’s pre-eminent dramatist. He is well-known to the world through his timeless characters that are universal in their appeal. The themes that he deals with also touch the human lives across the globe. The extracts from William Shakespeare’s play “Romeo and Juliet “express the implicit feelings of Romeo and and Juliet for each other.
# He compares Juliet’s beauty to nature. Romeo says that even the bright light of a torch would look dull before the brightness of Juliet. It looks like she hangs on the cheek of night. Romeo says that the beauty of Juliet is like a jewel which is hung in the ear of an African woman.
# """
# num_questions=2

# output_response = Generate_QA_1(input_text,num_questions,"hard")

# print(output_response)



