from Question_class import Questions
question_prompts =[
    "What color does Alex hate?\n (a) blue \n (b) green \n (c) red \n\n",
    "Which Cat is a bastard? \n (a) Salem \n (b) Abbadon \n (c) Azazel \n\n",
    "Which is the best name for a company? \n (a) Crime Design \n (b) Beacon engineering \n (c) Fresh Roast & Dragons \n\n"
]

questions = [
    Questions(question_prompts[0],"b"),
    Questions(question_prompts[1],"c"),
    Questions(question_prompts[2],"a"),

]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
run_test(questions)

