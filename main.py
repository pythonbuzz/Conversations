import time
import sys

def typing_effect(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)  
    print()  

def conversation_with_default(person1_question, person2_answer):
    typing_effect(f"Person1: {person1_question}")
    time.sleep(1)  
    typing_effect(f"Person2: {person2_answer}")
    print()

conversation_with_default("Where is Riya?" ,"Who is Riya?")
conversation_with_default("Domini daughter","Who is Domini?")
conversation_with_default("Riya mother","Who are those both?")
conversation_with_default("Mother and daughter","I don't know both of them")

