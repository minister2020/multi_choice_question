
from questions import question


question_prompt =[
    "what colour are apples? \n(a) Red \n (b) Purple\n (c) Yello\n\n",
    "what colour is Banana/ \n (a) Green \n (b) White \n (c) Blue\n\n",
    "what colur are Mango? \n (a) Green \n (b) Yello \n (c) Pink\n\n"
]

questions = [
    question(question_prompt[0], "a"),
    question(question_prompt[1], "a"),
    question(question_prompt[2], "b")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print( "you got" + str(score)+ "/" + str(len(questions)) +  "correct") 



run_test(questions)   