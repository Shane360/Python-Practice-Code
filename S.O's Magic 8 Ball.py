import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply unclear, try again'
    elif answerNumber == 5:
        return 'Concentrate and ask again'
    elif answerNumber == 6:
        return 'No'
    elif answerNumber == 7:
        return 'Ask again later'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'
    
print('Hi Friend, think of a yes/no question, and press enter to see the magic 8 ball response')
input()

print(getAnswer(random.randint(1, 9)))
