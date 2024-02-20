questions=("who was know as the father of india?",
           "who was the first prime minister of india?",
           "who is the first president of india?",
           "who is the first woman prime minister of india?",
           "who is the first woman president of india?"
          )
options=(("A.mahatma gandhi","B.jawaharal nehru","C.sardar","D.None of these"),
         ("A.rajendra prasad","B.Jawaharlal nehru","C.narendra modi","D.none of these"),
         ("A.dr.rajendra prasad","B.dr.mamta banerjee","C.abdul kalam","D.none of these"),
         ("A.indira gandhi","B.sonia gandhi","C.sushma swaraj","D.none of these"),
         ("A.indira gandhi","B.sonia gandhi","C.pratibha patil","D.none of these"))
answers=("A","B","A","A","C")
guesses=[]
score=0
question_num=0
for question in questions:
  print("########################")
  print(question)
  for option in options[question_num]:
    print(option)
  guess=input("enter the options A,B,C,D:").upper()
  guesses.append(guess)
  if guess==answers[question_num]:
    score+=1
    print("CORRECT")
  else:
    print("INCORRECT")
    print(f"{answers[question_num]} is the correct answer")
  question_num+=1
print("     Results    ")
print("answers: ",end="")
for answer in answers:
  print(answer,end=" ")
print()
print("guesses: ",end="")
for guess in guesses:
  print(guess,end=" ")
print()
score=int(score/len(questions)*100)
print(f"your score is:{score}%")
print("Do you want to play again?")
