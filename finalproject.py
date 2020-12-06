import time
import turtle
turtle.screensize(canvwidth=100,canvheight=100, bg='cyan')
turtle.penup()
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(225)
turtle.write('This game is created to learn logical connectives', move=False, font=20)
turtle.left(90)
turtle.forward(21)
turtle.write('You will be given a prompt and asked what logical connective will give a True response', move=False, font=20)
turtle.forward(21)
turtle.write('If you answer incorrectly the game will stop and you lose', move=False, font=20)
turtle.forward(21)
turtle.write('If you answer correctly the game will continue', move=False, font=20)
turtle.forward(21)
turtle.write('There are 10 questions', move=False, font=20)
turtle.forward(21)
turtle.write('Good luck!', move=False, font=20)
turtle.forward(21)
turtle.write('Fastest time win', move=False, font=20)
print('If x=6,')
print('x>5 [blank] x<4: ')
x=input()
start_time=time.time()
if x=='or':
    print('If x=5,')
    print('x==5 [blank] x>1: ')
    x=input()
    if x=='and':
        print('If x=3,')
        print('[blank] (x>5 and x<1)')
        x=input()
        if x=='not':
            print('If x=11,')
            print('x>10 [blank] x<5')
            x=input()
            if x=='or':
                print('If x=15,')
                print('x>10 [blank] x==15')
                x=input()
                if x=='and':
                    print('If x=1,')
                    print('x<2 [blank] x>3')
                    x=input()
                    if x=='or':
                        print('If x=2')
                        print('[blank] (x>3 and x==5)')
                        x=input()
                        if x=='not':
                            print('If x=5,')
                            print('x<=5 [blank] x>6')
                            x=input()
                            if x=='or':
                                print('If x=10,')
                                print('x>4 [blank] x<1')
                                x=input()
                                if x=='or':
                                    print('If x=1,')
                                    print('x==1 [blank] x<4')
                                    x=input()
                                    if x=='and':
                                        final_time=time.time()
                                        y=final_time-start_time
                                        turtle.reset()
                                        turtle.screensize(canvwidth=100,canvheight=100, bg='green')
                                        turtle.left(180)
                                        turtle.penup()
                                        turtle.forward(10)
                                        turtle.write('You won!', move=False, font=45)
                                        turtle.left(90)
                                        turtle.forward(46)
                                        turtle.write('Your time in seconds was', move=False, font=45)
                                        turtle.forward(46)
                                        turtle.write(y, move=False, font=45)
                                    else:
                                        turtle.reset()
                                        turtle.screensize(canvwidth=100,canvheight=100, bg='red')
                                        turtle.left(180)
                                        turtle.penup()
                                        turtle.forward(10)
                                        turtle.write('You lost!', move=False, font=30)
                                        turtle.left(90)
                                        turtle.forward(31)
                                        turtle.write('You got 9 questions right', move=False, font=30)
                                else:
                                    turtle.reset()
                                    turtle.screensize(canvwidth=100,canvheight=100, bg='red')
                                    turtle.left(180)
                                    turtle.penup()
                                    turtle.forward(10)
                                    turtle.write('You lost!', move=False, font=30)
                                    turtle.left(90)
                                    turtle.forward(31)
                                    turtle.write('You got 8 questions right', move=False, font=30)
                            else:
                                turtle.reset()
                                turtle.screensize(canvwidth=100,canvheight=100, bg='red')
                                turtle.left(180)
                                turtle.penup()
                                turtle.forward(10)
                                turtle.write('You lost!', move=False, font=30)
                                turtle.left(90)
                                turtle.forward(31)
                                turtle.write('You got 7 questions right', move=False, font=30)
                        else:
                            turtle.reset()
                            turtle.screensize(canvwidth=100,canvheight=100, bg='red')
                            turtle.left(180)
                            turtle.penup()
                            turtle.forward(10)
                            turtle.write('You lost!', move=False, font=30)
                            turtle.left(90)
                            turtle.forward(31)
                            turtle.write('You got 6 questions right', move=False, font=30)
                    else:
                        turtle.reset()
                        turtle.screensize(canvwidth=100,canvheight=100, bg='red')
                        turtle.left(180)
                        turtle.penup()
                        turtle.forward(10)
                        turtle.write('You lost!', move=False, font=30)
                        turtle.left(90)
                        turtle.forward(31)
                        turtle.write('You got 5 questions right', move=False, font=30)
                else:
                    turtle.reset()
                    turtle.screensize(canvwidth=100,canvheight=100, bg='red')
                    turtle.left(180)
                    turtle.penup()
                    turtle.forward(10)
                    turtle.write('You lost!', move=False, font=30)
                    turtle.left(90)
                    turtle.forward(31)
                    turtle.write('You got 4 questions right', move=False, font=30)
            else:
                turtle.reset()
                turtle.screensize(canvwidth=100,canvheight=100, bg='red')
                turtle.left(180)
                turtle.penup()
                turtle.forward(10)
                turtle.write('You lost!', move=False, font=30)
                turtle.left(90)
                turtle.forward(31)
                turtle.write('You got 3 questions right', move=False, font=30)
        else:
            turtle.reset()
            turtle.screensize(canvwidth=100,canvheight=100, bg='red')
            turtle.left(180)
            turtle.penup()
            turtle.forward(10)
            turtle.write('You lost!', move=False, font=30)
            turtle.left(90)
            turtle.forward(31)
            turtle.write('You got 2 questions right', move=False, font=30)
    else:
        turtle.reset()
        turtle.screensize(canvwidth=100,canvheight=100, bg='red')
        turtle.left(180)
        turtle.penup()
        turtle.forward(10)
        turtle.write('You lost!', move=False, font=30)
        turtle.left(90)
        turtle.forward(31)
        turtle.write('You got 1 question right', move=False, font=30)
else:
    turtle.reset()
    turtle.screensize(canvwidth=100,canvheight=100, bg='red')
    turtle.left(180)
    turtle.penup()
    turtle.forward(10)
    turtle.write('You lost!', move=False, font=30)
    turtle.left(90)
    turtle.forward(31)
    turtle.write('You got 0 questions right', move=False, font=30)


