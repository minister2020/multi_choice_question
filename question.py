
from questions import question


question_prompt =[
    "1. what colour are apples? \n(a) Red \n (b) Purple\n (c) Yello\n\n",
    "2. what colour are Banana/ \n (a) Green \n (b) White \n (c) Blue\n\n",
    "3. what colur are Mango? \n (a) Green \n (b) Yello \n (c) Pink\n\n",
    "4. what colur are watermelon? \n (a) White \n(b) Blue \n (c) Green\n\n",
    "5. who is the head of the family? \n (a) father \n(b) mother \n (c) sister\n\n",
    "6. who is the Governor of lagos state? \n(a) Tinube\n (b)Fashola \n (c) Sanwo-olu\n\n"
    "7. who is the Governor of Oyo state? \n(a) Makinde \n (b)Abasha \n (c) Buhari\n\n",
    "8. when did Nigeria got her independent?\n (a)1990\n (b)2004 \n (c)1960\n\n",
    "9. a  is greather than b? \n (a) yes\n (b)No\n\n"


]

questions = [
    question(question_prompt[0], "a"),
    question(question_prompt[1], "a"),
    question(question_prompt[2], "b"),
    question(question_prompt[3], "c"),
    question(question_prompt[4], "a"),
    question(question_prompt[5], "c"),
    question(question_prompt[6], "a"),
    question(question_prompt[7], "c"),
  
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print( "you got" + str(score)+ "/" + str(len(questions)) +  "correct") 



run_test(questions)   