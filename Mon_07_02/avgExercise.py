# avgExercise.py
# calculate the average of 3 exam scores

def main():
    print('This program computes the average of three exam scores')
    print()
    score1, score2, score3 = eval(input('Enter three scores seperated by comma: '))
    avg = (score1 + score2 + score3)/3
    print('The average of the scores is:', avg)
    
main()