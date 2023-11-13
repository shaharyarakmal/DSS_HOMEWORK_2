import random


def function_random_integer(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)


def function_random_math_operator():
    """
     returns random operators among +,_,*
    """
    return random.choice(['+', '-', '*'])


def function_generate_random_mathproblem(n1, n2, o):
    """
    takes three paramters, first two as integer, and third as an operator.
    generates and returns problem and answer of a mathematical operation as defined

    """
    p = f"{n1} {o} {n2}" # string to print the problem generated from using function A and B
    if o == '+': a = n1+n2 #addition logic was corrected it was defined to do subtraction initially
    elif o == '-': a = n1 - n2 # subtraction logic was defined as addition so corrected
    else: a = n1 * n2
    return p, a

def math_quiz():
    s = 0
    t_q = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for i in range(int(t_q)): #means this loop would run 3 times i-e we will be asked 3 maths questions'
        n1 = function_random_integer(1, 10); n2 = function_random_integer(1,  int(5.5)); o = function_random_math_operator()#n1, n2 select random integers, and o selects a operators defind in function_C'

        PROBLEM, ANSWER = function_generate_random_mathproblem(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}") #problem is printed as a string which was returned by function_C
        useranswer = input("Your answer: ")
        useranswer = int(useranswer) #since all the variables are integer so we are just type casting user's answers into integer for beter comparison

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s+= 1 #was initially s += -(-1) which is also the same and does s= s+1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{int(t_q)}") #type casted t_q bcz to we earn integer points from answers so total points should be integer

if __name__ == "__main__":
    math_quiz()
