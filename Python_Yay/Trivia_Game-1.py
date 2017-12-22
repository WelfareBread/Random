'''
Created on Dec 14, 2017

@author: andrussblack
'''
import time

class Question:
    
    def __init__(self, Question, Answer_1, Answer_2, Answer_3, Answer_4, Correct_Answer):
        
        self.question = Question
        self.option1 = Answer_1
        self.option2 = Answer_2
        self.option3 = Answer_3
        self.option4 = Answer_4
        self.CORRECT = Correct_Answer
        
    def get_info(self):
        return self.question, self.option1, self.option2, self.option3, self.option4, self.CORRECT
    def get_Question(self):
        return self.question
    def get_option1(self):
        return self.option1
    def get_option2(self):
        return self.option2
    def get_option3(self):
        return self.option3
    def get_option4(self):
        return self.option4
    def get_Correct(self):
        return self.CORRECT
    
Question1 = Question("How many feet are in a mile?", 100, 200, 300, 5280, 5280)                                             #Int
Question2 = Question("What country is above South Korea?", "North Korea", "Russia", "China", "Japan", "North Korea")        #String
Question3 = Question("How many cm are in an inch?", 3, 5, 2.54, 2.44, 2.54)                                                 #Int
Question4 = Question("How many pedals are in a Formula One car?", 3, 2, 1, 4, 3)                                            #Int
Question5 = Question("What kind of tree do we buy on Christmas?", "Pine", "Oak", "Starfish", "Evergreen", "Evergreen")      #String
Question6 = Question("10 Minutes of JumpRoping are equivalent to how many minutes of jogging?", 5, 10, 20, 30, 30)
Question7 = Question("Who is the Formula One World Champion for 2017", "Raikkonen", "Vettel", "Hamilton", "Magnussen", "Hamilton")
Question8 = Question("What is the life expectancy in the US", 80, 78.7, 75.5, 83.4, 78.7)
Question9 = Question("How many states are in the US", 49, 100, 50, 51, 50)
Question10 = Question("Who is the 17th President of the US","Andrew Johnson", "Abraham Lincoln", "Andrew Jackson","Martin Van Buren", "Andrew Johnson")

QuestionList = [Question1,Question2,Question3,Question4,Question5,Question6,Question7,Question8,Question9,Question10]

a = 1
def main():
    print("Player One get ready")
    time.sleep(3)
    player1List = []
    player2List = []
    
    for j in range(2):
        if j == 0:
            for i in range(5):
                if i == 0:
                    print(Question1.get_Question())
                    print(Question1.get_option1(), Question1.get_option2(), Question1.get_option3(), Question1.get_option4())
                    answer = raw_input("Choose your answer:")
                    if isinstance(Question1.get_Correct(), int):
                        player1List.append(int(answer))             
                    else:
                        player1List.append(answer)

                if i == 1:
                    print(Question2.get_Question())
                    print(Question2.get_option1(), Question2.get_option2(), Question2.get_option3(), Question2.get_option4())
                    answer = raw_input("Choose your answer:")
                    if isinstance(Question2.get_Correct(), int):
                        player1List.append(int(answer))
                    else:
                        player1List.append(answer)

                if i == 2:
                    print(Question3.get_Question())
                    print(Question3.get_option1(), Question3.get_option2(), Question3.get_option3(), Question3.get_option4())
                    answer = raw_input("Choose your answer:")
                    if isinstance(Question3.get_Correct(), float):                #Not Working
                        player1List.append(float(answer))             
                    else:
                        player1List.append(answer)
                if i == 3:
                    print(Question4.get_Question())
                    print(Question4.get_option1(), Question4.get_option2(), Question4.get_option3(), Question4.get_option4())
                    answer = raw_input("Choose your answer:")
                    if isinstance(Question4.get_Correct(), int):
                        player1List.append(int(answer))             
                    else:
                        player1List.append(answer)
                if i == 4:
                    print(Question5.get_Question())
                    print(Question5.get_option1(), Question5.get_option2(), Question5.get_option3(), Question5.get_option4())
                    answer = raw_input("Choose your answer:")
                    if isinstance(Question5.get_Correct(), int):
                        player1List.append(int(answer))             
                    else:
                        player1List.append(answer)
            
        if j == 1:
            print("Player two get ready")
            time.sleep(3)
            for i in range(5):
                if i == 0:
                    print(Question6.get_Question())
                    print(Question6.get_option1(), Question6.get_option2(), Question6.get_option3(), Question6.get_option4())
                    answer = raw_input("Choose your answer:")
                    if isinstance(Question6.get_Correct(), int):
                        player2List.append(int(answer))             
                    else:
                        player2List.append(answer)
                if i == 1:
                    print(Question7.get_Question())
                    print(Question7.get_option1(), Question7.get_option2(), Question7.get_option3(), Question7.get_option4())
                    answer = raw_input("Choose your answer:")
                    if isinstance(Question7.get_Correct(), int):
                        player2List.append(int(answer))             
                    else:
                        player2List.append(answer)
                if i == 2:
                    print(Question8.get_Question())
                    print(Question8.get_option1(), Question8.get_option2(), Question8.get_option3(), Question8.get_option4())
                    answer = raw_input("Choose your answer:")
                    if isinstance(Question8.get_Correct(), float):
                        player2List.append(float(answer))             
                    else:
                        player2List.append(answer)
                if i == 3:
                    print(Question9.get_Question())
                    print(Question9.get_option1(), Question9.get_option2(), Question9.get_option3(), Question9.get_option4())
                    answer = raw_input("Choose your answer:")
                    if isinstance(Question9.get_Correct(), int):            #Not Working
                        player2List.append(int(answer))             
                    else:
                        player2List.append(answer)
                if i == 4:
                    print(Question10.get_Question())
                    print(Question10.get_option1(), Question10.get_option2(), Question10.get_option3(), Question10.get_option4())
                    answer = raw_input("Choose your answer:")
                    if isinstance(Question10.get_Correct(), int):
                        player2List.append(int(answer))             
                    else:
                        player2List.append(answer)
                    
                    
    print("player 1 score")
    
    score1 = 0
    
    if player1List.__getitem__(0) == Question1.get_Correct():
        print("Correct")
        score1 = score1 + 1
    else:
        print("Wrong")
    if player1List.__getitem__(1) == Question2.get_Correct():
        print("Correct")
        score1 = score1 + 1
    else:
        print("Wrong")
    if player1List.__getitem__(2) == Question3.get_Correct():
        print("Correct")
        score1 = score1 + 1
    else:
        print("Wrong")
    if player1List.__getitem__(3) == Question4.get_Correct():
        print("Correct")
        score1 = score1 + 1
    else:
        print("Wrong")
    if player1List.__getitem__(4) == Question5.get_Correct():
        print("Correct")
        score1 = score1 + 1
    else:
        print("Wrong")
    
    print(player1List)
    print(score1)
    
    print("-------------")
    
    
    score2 = 0
    
    print("player 2 score")
    
    if player2List.__getitem__(0) == Question6.get_Correct():
        print("Correct")
        score2 = score2 + 1
    else:
        print("Wrong")
    if player2List.__getitem__(1) == Question7.get_Correct():
        print("Correct")
        score2 = score2 + 1
    else:
        print("Wrong")
    if player2List.__getitem__(2) == Question8.get_Correct():
        print("Correct")
        score2 = score2 + 1
    else:
        print("Wrong")
    if player2List.__getitem__(3) == Question9.get_Correct():
        print("Correct")
        score2 = score2 + 1
    else:
        print("Wrong")
    if player2List.__getitem__(4) == Question10.get_Correct():
        print("Correct")
        score2 = score2 + 1
    else:
        print("Wrong")
    
    print(player2List)
    print(score2)
    
        
        
        
   

   
    
main()

        
        
        
        
        
        
        
        
    