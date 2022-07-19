# print("1")
# print(5)
#
#
# def getAnswer(answerNumber):
#     if answerNumber == 1:
#         return 'You are happy'
#     elif answerNumber == 2:
#         return 'You are unhappy'
#     elif answerNumber == 3:
#         return 'You are good'
#
# print('input you digit from 1 to 3')
# r = int(input())
# fortune = getAnswer(r)
# print(fortune)
#
# def spam ():
#     eggs = 1555
#     print(eggs)
#
# spam()

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: invalid argument')


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))