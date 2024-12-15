print("Welcome to the PY General Knowledge Quizeria!")
name = input("What is your name?\n")
score = 0

#Question 1
question1 = print("Which is the longest river in the world?\nA) Amazon, B) Nile, C) Yangtze, D) Mississippi")
answer1 = input("Choose the right option?\n").lower()
if answer1 == "b" or answer1 == "nile":
  score += 1
else:
  score += 0

# Question 2
question2 = print("Who was the first President of the United States?\nA) George Washington, B) Thomas Jefferson, C) Abraham Lincoln, D) John Adams")
answer2 = input("Choose the right option?\n").lower()
if answer2 == "a" or answer2 == "george washington":
  score += 1
else:
  score += 0

#Question 3
question3 = print("What is the chemical symbol for gold?\nA) Au, B) Ag, C) Pb, D) Fe")
answer3 = input("choose the correct option?\n").lower()
if answer3 == "a" or answer3 == "au":
  score += 1
else:
  score += 0

#Question 4
question4 = print("Who wrote \"Romeo and Juliet\"?\nA) Charles Dickens, B) Mark Twain, C) William Shakespeare, D) Jane Austen")
answer4 = input("Choose the correct option?\n").lower()
if answer4 == "c" or answer4 == "william shakespeare":
  score += 1
else:
  score += 0

#Question 5
question5 = print("Which country hosted the 2016 Summer Olympics?\nA) China, B) Brazil, C) United Kingdom, D) Russia")
answer5 = input("Choose the right option?\n").lower()
if answer5 == "b" or answer5 == "brazil":
  score += 1
else:
  score += 0

#Result
print(f"Hello {name} your final score for the quizz is: {score}")