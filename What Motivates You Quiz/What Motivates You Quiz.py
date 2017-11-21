# Becky Mai
# November 20, 2017
#
# Title: "Why did you choose to attend university?"
# Description: A (intrinsic vs. extrinsic) motivation quiz.
# A file handling exercise.
#
# Sources:
# "What Motivates You?" Workshop
#
#####################################

quiz = open('what_motivates_you_quiz.txt')

# Variables
internal_to_self = [2, 4, 5, 9, 10, 12]
external_to_self = [1, 3, 6, 7, 8, 11]
valid_answers = [1, 2, 3, 4, 5]
question_num = 0
int_score, ext_score = [], []

for line in quiz:
    if "Question" not in line:
        print(line)
    else:
        question_num += 1
        question_num_as_str = "Question " + str(question_num) + ". "
        query = line.lstrip(question_num_as_str)
        answer = 0
        
        while answer not in valid_answers:
            print(query)
            answer = int(input("Rate correspondence from 1 to 5: "))
            print('\n\n')
        
        if question_num in internal_to_self:
            int_score.append(answer)
        elif question_num in external_to_self:
            ext_score.append(answer)
        else:
            "This question relates to neither intrinsic or extrinsic motivation."
            
print("The quiz has been completed!")
print("Your 'internal to self' score is: " + str(sum(int_score)))
print("Your 'external to self' score is: " + str(sum(ext_score)))