"""A collection of function for doing my project."""

#https://www.youtube.com/watch?v=myJ36xIR7Yg - I used this youtube video to help me write the basic structure of how I should write out my code, although I did modify it and add some more things as well to make it look how I wanted. The input and print statements for the questions are similar to the code that I used to guide me, the way I did the score calculation is different, and I also added another function. So basically I just used the source to see the basic set up of how to make the questions pop up because I didn't know how.

#https://ozzmaker.com/add-colour-to-text-in-python/ - I used this website to figure out how to add color to my texts. I modified it and only used certain colors. This was something new for me so looking at the website really helped.


def questions():
    """https://www.youtube.com/watch?v=myJ36xIR7Yg - This is where I looked to be guided throughout this project. Specifically for questions() but I added more things and modified it to be my own, I only used it as a reference/guide because I didn't know how to make the code show up."""
#This function has all of the questions for my quiz, including the adding points everytime they get it right and the print statements of what it's going to say everytime.
    
    score = 0
    
    print('\033[1;33m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    """https://ozzmaker.com/add-colour-to-text-in-python/ - I used this website to figure out how to add the color to my texts. I modified it and made it my own."""
    
    
#first question
    first_Q = input ("Question 1: Who is the manager in the beginning of the show The Office? \nA. Andrew Bernard \nB. Robert California \nC. Michael Scott \n \nAnswer: ")
    
    if first_Q == 'C' or first_Q == 'c' or first_Q == 'Michael Scott' or first_Q == 'michael scott':
        score += 1 
        print('That is correct!')
        print('Your score is: ', score)
        print('\n')
    else:
        print('That is not correct. The correct answer is Michael Scott.')
        print('Your score is: ', score)
        print('\n')
    print('\n \033[1;35m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
       
        
#second question
    second_Q = input ("Question 2: What is the name of the branch that the show takes place in? \nA. Buffalo \nB. Dunder Mifflin \nC. Utica \n \nAnswer: ")

    if second_Q == 'B' or second_Q == 'b' or second_Q == 'Dunder Mifflin' or second_Q == 'dunder mifflin':
        score += 1 
        print('That is correct!')
        print('Your score is: ', score)
        print('\n')
    else:
        print('That is not correct. The correct answer is Dunder Mifflin.')
        print('Your score is: ', score)
        print('\n')
    print('\n \033[1;33m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
       
        
#third question        
    third_Q = input ("Question 3: Who has a beet farm? \nA. Dwight K. Schrute \nB. Ryan Howard \nC. Kevin Malone \n \nAnswer: ")

    if third_Q == 'A' or third_Q == 'a' or third_Q == 'Dwight K. Schrute' or third_Q == 'dwight k. schrute':
        score += 1 
        print('That is correct!')
        print('Your score is: ', score)
        print('\n')
    else:
        print('That is not correct. The correct answer is Dwight K. Schrute.')
        print('Your score is: ', score)
        print('\n')
        
    print('\n \033[1;35m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        
    
#fourth question
    fourth_Q = input ("Question 4: Which of the following is NOT one of Michael Scott's characters? \nA. Date Mike \nB. Model Mike \nC. Prison Mike \n \nAnswer: ")
    if fourth_Q == 'B' or fourth_Q == 'b' or fourth_Q == 'Model Mike' or fourth_Q == 'model mike':
        score += 1 
        print('That is correct!')
        print('Your score is: ', score)
        print('\n')
    else:
        print('That is not correct. The correct answer is Model Mike.')
        print('Your score is: ', score)
        print('\n')
    print('\n \033[1;33m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
       

#fifth question
    fifth_Q = input ("Question 5: Who does Pam end up OFFICIALLY marrying ? \nA. Jim \nB. Roy \nC. Toby \n \nAnswer: ")
    if fifth_Q == 'A' or fifth_Q == 'a' or fifth_Q == 'Jim' or fifth_Q == 'jim':
        score += 1 
        print('That is correct!')
        print('Your score is: ', score)
        print('\n')
    else:
        print('That is not correct. The correct answer is Jim.')
        print('Your score is: ', score)
        print('\n')
    print('\n \033[1;35m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        
        
#sixth question 
    sixth_Q = input ("Question 6: Who wanted to be an artist? \nA. Kelly \nB. Erin \nC. Pam \n \nAnswer: ")
    if sixth_Q == 'C' or sixth_Q == 'c' or sixth_Q == 'Pam' or sixth_Q == 'pam':
        score += 1 
        print('That is correct!')
        print('Your score is: ', score)
        print('\n')
    else:
        print('That is not correct. The correct answer is Pam.')
        print('Your score is: ', score)
        print('\n')
    print('\n \033[1;33m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        
    
#seventh question
    seventh_Q = input ("Question 7: Who has the most toxic relationship in the show? \nA. Ryan and Kelly \nB. Ryan and Erin \nC. Ryan and Angela \n \nAnswer: ")
    if seventh_Q == 'A' or seventh_Q == 'a' or seventh_Q == 'Ryan and Kelly' or seventh_Q == 'ryan and kelly':
        score += 1 
        print('That is correct!')
        print('Your score is: ', score)
        print('\n')
    else:
        print('That is not correct. The correct answer is Ryan and Kelly.')
        print('Your score is: ', score)
        print('\n')
    print('\n \033[1;35m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    
    
#eighth question
    eighth_Q = input ("Question 8: What is Dunder Mifflin? \nA. A muffin company \nB. A paper company \nC. A mattress company \n \nAnswer: ")
    if eighth_Q == 'B' or eighth_Q == 'b' or eighth_Q == 'A paper company' or eighth_Q == 'a paper company':
        score += 1
        print('That is correct!')
        print('Your score is: ', score)
        print('\n')
    else:
        print('That is not correct. The correct answer is A paper company.')
        print('Your score is: ', score)
        print('\n')
    print('\n \033[1;33m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
       
    
#ninth question
    ninth_Q = input ("Question 9: Which of the following is NOT a character in The Office? \nA. Oscar \nB. Chandler \nC. Stanley \n \nAnswer: ")
    if ninth_Q == 'B' or ninth_Q == 'b' or ninth_Q == 'Chandler' or ninth_Q == 'chandler':
        score += 1
        print('That is correct!')
        print('Your score is: ', score)
        print('\n')
    else:
        print('That is not correct. The correct answer is Chandler. This ain\'t Friends.')
        print('Your score is: ', score)
        print('\n')
    print('\n \033[1;35m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    
        
#last question
    last_Q = input ("Question 10: Which character did Michael Scott absolutely hate? \nA. Toby \nB. Pam \nC. Ryan \n \nAnswer: ")
    if last_Q == 'A' or last_Q == 'a' or last_Q == 'Toby' or last_Q == 'toby':
        score += 1
        print('That is correct!')
        print('Your score is: ', score)
        print('\n')
    else:
        print('That is not correct. The correct answer is Toby.')
        print('Your score is: ', score)
        print('\n')
    print('\n \033[1;36m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')   
    scoring_system(score)
    p_or_f(score)


def scoring_system(score):
    if score <= 6:
        score = score * 10 
        print('Total Score: ' + str(score) + '%')
    else:
        score = score * 10
        print('Total Score: '+ str(score) + '%')
    return score
#This multiplies the score by 10 to get a final percentage.

def p_or_f(score):
    if score < 7:
        print('\n')
        print('I\'m sorry to say but you failed. If you would like to retake the test, go ahead.')
    else:
        print('\n')
        print('I\'m happy to say that you passed! This is the end of the test!')
#This determines whether or not they got a passing score.
      

    

    
    

       
    

    

