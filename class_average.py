

"""

Input: the test score
Initiate a iterator and accumulator and set it to zero
loop through list
ass all the test scores
increment the counter by one
once the loop ends, there are no more scores to add
divide the output to the user
output:  print the average of the class scores
"""

"""

scores 
iterator, accumulator = 0
loop through
    accumulator = accumulator + score
    iterator = iterator + 1
output = accumulator / total score
print output

"""


total = 100 + 80 + 90 + 70 + 50 + 95
print("total:", total)


def calculate_average(scores):
    iterator = 0
    accumulator = 0
    student_count = len(scores)
    while iterator < len(scores):
        accumulator = accumulator + scores[iterator]
        iterator = iterator + 1
    average = accumulator / student_count
    return average


output = calculate_average(
    [50, 0, 100, 80, 90, 70, 50, 95, 60, 90, 50, 100, 70, 90])
print("The average of total scores in the class is: ", output)
