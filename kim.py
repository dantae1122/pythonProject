# # 숫자
# # a = 10
# # b = 20
# # print(a+b)
# #
# # 문자
# # a = "안녕"
# # b = "하세요"
# # print(a+b)
# #
# # 문자와 숫자의 조합
# # a = 10
# # b = "문자"
# # print(str(a)+b)
# #
# # a = "문자"
# # b = 10
# # print(a+str(b))
# #
# # import  turtle
# # t = turtle.Turtle()
# # s = turtle.Screen()
# #
# # for i in range(4):
# #     t.forward(100)
# #     t.right(360/4)
# # t.penup()
# # t.setposition(-100,100)
# # t.pendown()
# # for i in range(4):
# #     t.forward(100)
# #     t.right(360/4)
# # t.penup()
# # t.setposition(0,100)
# # t.pendown()
# # for i in range(4):
# #     t.forward(100)
# #     t.right(360/4)
# # t.penup()
# # t.setposition(-100,-100)
# # t.pendown()
# # for i in range(4):
# #     t.forward(100)
# #     t.left(360/4)
# #
# # t.circle(50)
# # t.penup()
# # t.setposition(-50,-100)
# # t.pendown()
# # for i in range(4):
# #     t.forward(100)
# #     t.left(90)
# # t.penup()
# # t.setposition(0,-200)
# # t.pendown()
# # t.circle(50)
# # t.penup()
# # t.setposition(-50,-300)
# # t.pendown()
# # for i in range(4):
# #     t.forward(100)
# #     t.left(90)
# #
# #
# # import  turtle
# # t = turtle.Turtle()
# # s = turtle.Screen()
# #
# # t.speed(0)
# # draw_list = []
# #
# # for i in range(4):
# #     t.forward(300)
# #     t.right(90)
# #
# # t.penup()
# # t.setposition(30,0)
# # t.pendown()
# # t.right(90)
# # t.forward(300)
# #
# # for i in range(4):
# #     t.left(90)
# #     t.forward(30)
# #     t.left(90)
# #     t.forward(300)
# #     t.right(90)
# #     t.forward(30)
# #     t.right(90)
# #     t.forward(300)
# #
# # for i in range(2):
# #     t.left(90)
# #     t.forward(30)
# #
# # for i in range(4):
# #     t.left(90)
# #     t.forward(300)
# #     t.right(90)
# #     t.forward(30)
# #     t.right(90)
# #     t.forward(300)
# #     t.left(90)
# #     t.forward(30)
# #
# # t.left(90)
# # t.forward(300)
# # t.right(90)
# # t.forward(30)
# # t.right(90)
# # t.forward(300)
# # t.left(90)
# # t.setposition(0,-29)
# #
# #
# # list_square = []
# # x = 0
# # y = 0
# # for j in range(10):
# #     for x in range(0,300,30):
# #         list_square.append([x,y])
# #         x += 30
# #     y -= 30
# #
# # draw = turtle.Turtle()
# # draw.speed(0)
# # draw.penup()
# #
# # draw_list.append([int(t.xcor()),int(t.ycor())])
# #
# # color_list = []
# # def coloring(x,y):
# #     t.penup()
# #     t.setposition(x+1,y-1)
# #     t.begin_fill()
# #     if t.fillcolor() == 'red':
# #         t.fillcolor('white')
# #     else:
# #         t.fillcolor('red')
# #         color_list.append([x,y])
# #     for i in range(4):
# #         t.forward(29)
# #         t.right(90)
# #     t.end_fill()
# #
# # def cl(x,y):
# #     print(x,y)
# #     draw.setposition(x,y)
# #     for i in list_square:
# #         if i[0] < int(draw.xcor()) and i[0] + 30 > int(draw.xcor()) and i[1] > int(draw.ycor()) and i[1]-30 < int(draw.ycor()):
# #             print("이내")
# #             coloring(i[0],i[1])
# #
# # s.onclick(cl)
# # print(len(list_square))
# #
# # s.mainloop()
# #
# #
# #
# # a = input("숫자를 입력 ")
# # b = 20
# # print(int(a)+b)
# #
# # 입력을 받다..
# # a = input("입력하세요 ")
# # if int(a) < 10:
# #     print("a는 10보다 작다")
# # elif int(a) < 15:
# #     print("a는 15보다 작다")
# #
# #  숫자 한개를 입력 받고 그 숫자가 양수인지 음수인지 판정하라.
# # a = input("숫자를 입력하시오")
# # if int(a) > 0:
# #     print("a는 양수이다")
# # elif int(a) < 0:
# #     print("a는 음수이다")
# #
# # 숫자 한개를 입력받고 그 숫자가 짝수인지 홀수 인지 판정하라.
# # a = input("숫자를 입력하시오")
# # if int(a)%2 == 0:
# #     print("a는 짝수입니다")
# # else:
# #     print("a는 홀수입니다")
# #
# #
# # 반복문을 이용하여 0부터 9까지 출력하라.
# # 짝수만 출력
# # for i in range(10):
# #     if i%2==0:
# #         print(i)
# # for i in range(10):
# #     if i%2!=0:
# #         print(i)
# # 짝수번째는 '짝수' 로 출력
# #
# # for i in range(10):
# #     if i%2==0:
# #         print("짝수")
# #     else:
# #         print(i)
# #
# #
# #
# # 자판기
# # coin = input("금액을 지불하십시오")
# # 거스름돈 = int(coin)
# # while True:
# #     print("1.콜라(3000)  2.사이다(2000)  3.커피(5000)  4.환타(3000)")
# #     a = input("메뉴를 고르시오")
# #     if int(a) == 1:
# #         if int(coin) >= 3000:
# #             print("콜라를 선택하셨습니다")
# #             거스름돈 = 거스름돈 - 3000
# #         else:
# #             print("금액이 부족합니다")
# #             exit()
# #     elif int(a) == 2:
# #         if int(coin) >= 2000:
# #             print("사이다를 선택하셨습니다")
# #             거스름돈 = 거스름돈 - 2000
# #         else:
# #             print("금액이 부족합니다")
# #             exit()
# #     elif int(a) == 3:
# #         if int(coin) >= 5000:
# #             print("커피를 선택하셨습니다")
# #             거스름돈 = 거스름돈 - 5000
# #         else:
# #             print("금액이 부족합니다")
# #             exit()
# #     elif int(a) == 4:
# #         if int(coin) >= 3000:
# #             print("환타를 선택하셨습니다")
# #             거스름돈 = 거스름돈 - 3000
# #         else:
# #             print("금액이 부족합니다")
# #             exit()
# #     print("거스름돈은", 거스름돈, "원 입니다")
# #     if 거스름돈 < 2000:
# #         break
# #
# # 1 자판기///
# #
# # a = 0
# # while True:
# #     a += 1
# #     print(a)
# #     if a > 10:
# #         break
# # a = 0
# # while a < 10:
# #     a += 1
# #     print(a)
# #
# #
# # for 문으로 1부터 100까지 출력
# # for i in range(1,101):
# #     print(i)
# # while 문으로 1부터 100까지 출력
# #
# # a=0
# # while a < 100:
# #     a += 1
# #     print(a)
# #
# # a = 0
# # while True:
# #     a += 1
# #     print(a)
# #     if a > 99:
# #         break
# #
# #
# # 거스름돈 = 1000
# # for i in range(10):
# #     print("메뉴", i, "번째", 거스름돈 ,"금액")
# #     거스름돈 = 거스름돈 - i
# #
# # print(a)
# #
# # import random
# #
# # com = random.randint(1,100)
# # # print(com)
# # count = 0
# # while True:
# #     user = input("숫자를 입력하라")
# #     count = count + 1
# #     if int(user) < com:
# #         print("Up")
# #     elif int(user) > com:
# #         print("Down")
# #     else:
# #         print("정답", count, "번 만에 맞춤")
# #         break
# #
# # 리스트..변수
# #
# # a = [10,20,30,40,50,60]
# # for i in range(6):
# #     print(a[i])
# #
# # for i in a:
# #     print(i)
# #
# #
# # 학생 점수 리스트
# #
# # 첫번째 수학,국어,과학,영어
# # 김철수 = [100,80,70,50]
# # 김영희 = [100,100,100,100]
# # print(sum(김철수)/4)
# #
# # 키리스트 = [150,160,155,178,180,140,167]
# # 키리스트.sort()
# # print(키리스트)
# #
# #
# # 리스트변수 a를 만들고 값을 출력 (4개)
# #
# # a = [100, 120, 166, 187]
# #
# # print(sum(a)/4)
# #
# #
# # import turtle
# # import random
# # s = turtle.Screen()
# # player_1 = turtle.Turtle()
# # player_1.shapesize(3)
# # player_1.color("red")
# # player_1.shape("turtle")
# # player_1.penup()
# # player_1.setposition(-300,200)
# #
# # player_2 = turtle.Turtle()
# # player_2.shapesize(3)
# # player_2.color("blue")
# # player_2.shape("turtle")
# # player_2.penup()
# # player_2.setposition(-300,0)
# #
# # bet = s.textinput("입력", "배팅할 색상을 선택(red or blue)")
# # print(bet)
# #
# # for i in range(200):
# #     player_1.forward(random.randint(1,5))
# #     player_2.forward(random.randint(1,5))
# # write = turtle.Turtle()
# # write.hideturtle()
# #
# # if player_1.xcor() > player_2.xcor() and bet == "red":
# #     write.write("레드 승리 배팅 성공", font=("굴림체" ,30,"bold"))
# # elif player_1.xcor() < player_2.xcor() and bet == "blue":
# #     write.write("블루 승리 배팅 성공", font=("굴림체" ,30,"bold"))
# # elif player_1.xcor() > player_2.xcor() and bet == "blue":
# #     write.write("레드 승리 배팅 실패", font=("굴림체" ,30,"bold"))
# # elif player_1.xcor() < player_2.xcor() and bet == "red":
# #     write.write("블루 승리 배팅 실패", font=("굴림체" ,30,"bold"))
# #
# # s.mainloop()
# #
# # t.pensize(3)
# # t.pencolor("red")
# #
# #
# # import turtle
# # s = turtle.Screen()
# # t = turtle.Turtle()
# # t.pensize(3)
# # t.penup()
# # t.setposition(200,0)
# # t.pendown()
# #
# # t.pencolor("blue")
# # t.left(120)
# # t.forward(50)
# # t.pencolor("green")
# # t.left(120)
# # t.forward(50)
# #
# # for i in range(3):
# #     t.pencolor("blue")
# #     t.right(120)
# #     t.forward(50)
# #     t.pencolor("green")
# #     t.left(120)
# #     t.forward(50)
# # t.pencolor("red")
# # t.left(120)
# # t.forward(200)
# #
# # s.mainloop()
# #
# # import turtle
# # s = turtle.Screen()
# # t = turtle.Turtle()
# #
# #
# # def triangle(lenth):
# #     t.right(60)
# #     for i in range(3):
# #         t.forward(lenth)
# #         t.right(120)
# # t.speed(0)
# # def triangle(lenth):
# #     for i in range(3):
# #         t.forward(lenth)
# #         t.left(120)
# # triangle(50)
# # t.right(90)
# # for i in range(4):
# #     t.forward(50)
# #     t.left(90)
# #
# # for i in range(3):
# #     t.penup()
# #     t.forward(100)
# #     t.pendown()
# #     t.left(90)
# #     triangle(50)
# #     t.right(90)
# #     for j in range(4):
# #         t.forward(50)
# #         t.left(90)
# #
# #
# # for i in range(36):
# #     t.circle(10)
# #     t.penup()
# #     t.left(10)
# #     t.forward(20)
# #     t.pendown()
# #
# # for i in range(36):
# #     t.begin_fill()
# #     if i % 3 == 0:
# #         t.fillcolor("red")
# #     elif  i % 2 == 0:
# #         t.fillcolor("blue")
# #     else:
# #         t.fillcolor("green")
# #     t.circle(10)
# #     t.end_fill()
# #     t.penup()
# #     t.left(10)
# #     t.forward(20)
# #     t.pendown()
# #
# # t.penup()
# # t.setposition(-300,300)
# # t.pendown()
# # for i in range(10):
# #     t.forward(50)
# #     t.right(90)
# #     t.forward(50)
# #     t.left(90)
# #
# #
# #
# # s.mainloop()
# #
# #
# # 1번
# # a = input("수를 입력하시오")
# # b = input("다른 수를 입력하시오")
# # print(int(a)+int(b))
# #
# # 2번
# # a = int(input("수를 입력하시오"))
# # b = int(input("다른 수를 입력하시오"))
# # c = input("수식을 입력하시오")
# #
# # if c == "+":
# #     print(a, "+", b,"=", a + b)
# # elif c == "-":
# #     print(a, "-", b,"=", a - b)
# # elif c == "*":
# #     print(a, "*", b,"=", a * b)
# # else:
# #     print(a, "/", b,"=", a / b)
# #
# # 3번
# # a = int(input("숫자를 입력하시오"))
# # sum = 0
# # for i in range(a+1):
# #     sum = sum + i
# # print(sum)
# #
# # 4번
# # a = input("숫자를 입력하시오")
# # if int(a)%2 == 0:
# #     print("짝수입니다")
# # else:
# #     print("홀수입니다")
# #
# # 5번
# # a = int(input("숫자를 입력하시오"))
# # for i in range(1,10):
# #     print(a, "X", i ,"=", a*i)
# #
# # 6번
# # count_odd = 0
# # count_even = 0
# # while True:
# #     user = int(input("숫자 입력"))
# #     if user % 2 == 0:
# #         count_even += 1
# #     elif user % 2 != 0:
# #         count_odd +=1
# #     if user == 0:
# #         print("짝수의 개수", cout_even, "홀수의 개수", count_odd)
# #         break
# #
# # 7번
# # count = 0
# # while True:
# #     user = int(input("숫자 입력"))
# #     sum = user + user
# #     count += 1
# #     if user > 100:
# #         print(sum,sum/user)
# #         break
# #
# #  8번
# # while True:
# #     user = int(input("숫자 입력"))
# #     if user == 0:
# #
# # import turtle
# # import random
# #
# # s = turtle.Screen()
# #
# # player1 = turtle.Turtle()
# # player1.shapesize(3)
# # player1.color('red')
# # player1.shape('turtle')
# # player1.penup()
# # player1.setposition(-300,300)
# #
# # player2 = turtle.Turtle()
# # player2.shapesize(3)
# # player2.color("blue")
# # player2.shape("turtle")
# # player2.penup()
# # player2.setposition(-300,0)
# #
# # player3 = turtle.Turtle()
# # player3.shapesize(3)
# # player3.color("green")
# # player3.shape("turtle")
# # player3.penup()
# # player3.setposition(-300,-300)
# #
# # bet = s.textinput("입력", "배팅할 색상을 선택(red or blue or green)")
# # print(bet)
# #
# # for i in range(200):
# #     player1.forward(random.randint(1,5))
# #     player2.forward(random.randint(1,5))
# #     player3.forward(random.randint(1,5))
# # write = turtle.Turtle()
# # write.hideturtle()
# #
# # if bet == "red":
# #     if player1.xcor() > player2.xcor() and player1.xcor() > player3.xcor():
# #         write.write("배팅 성공", font=("굴림체", 30, "bold"))
# #     elif player1.xcor() < player2.xcor() and player1.xcor() < player3.xcor():
# #         write.write("배팅 실패", font=("굴림체", 30, "bold"))
# #     elif player1.xcor() < player2.xcor() and player1.xcor() > player3.xcor():
# #         write.write("배팅 실패", font=("굴림체", 30, "bold"))
# #     elif player1.xcor() > player2.xcor() and player1.xcor() < player3.xcor():
# #         write.write("배팅 실패", font=("굴림체", 30, "bold"))
# #
# # elif bet == "blue":
# #     if player1.xcor() < player2.xcor() and player2.xcor() > player3.xcor():
# #         write.write("배팅 성공", font=("굴림체", 30, "bold"))
# #     elif player1.xcor() > player2.xcor() and player1.xcor() > player3.xcor():
# #         write.write("배팅 실패", font=("굴림체", 30, "bold"))
# #     elif player1.xcor() > player2.xcor() and player1.xcor() < player3.xcor():
# #         write.write("배팅 실패", font=("굴림체", 30, "bold"))
# #     elif player1.xcor() < player2.xcor() and player2.xcor() > player3.xcor():
# #         write.write("배팅 실패", font=("굴림체", 30, "bold"))
# #
# # elif bet == "green":
# #     if player2.xcor() < player3.xcor() and player1.xcor() < player3.xcor():
# #         write.write("배팅 성공", font=("굴림체", 30, "bold"))
# #     elif player2.xcor() > player3.xcor() and player1.xcor() > player3.xcor():
# #         write.write("배팅 실패", font=("굴림체", 30, "bold"))
# #     elif player3.xcor() < player2.xcor() and player1.xcor() > player3.xcor():
# #         write.write("배팅 실패", font=("굴림체", 30, "bold"))
# #     elif player1.xcor() > player3.xcor() and player2.xcor() < player3.xcor():
# #         write.write("배팅 실패", font=("굴림체", 30, "bold"))
# #
# # s.mainloop()
# #
# # import turtle
# # import random
# # t = turtle.Turtle()
# # s = turtle.Screen()
# # colors = ['red','blue','green','orange','black','violet']
# # t.speed(0)
# #
# # for i in range(100):
# #     x = random.randint(-300,300)
# #     y = random.randint(-300,300)
# #     t.color(random.choice(colors))
# #     t.pensize(random.randint(1,10))
# #     for j in range(4):
# #         t.forward(100)
# #         t.right(90)
# #     t.penup()
# #     t.setposition(x,y)
# #     t.pendown()
# #
# # s.mainloop()
# #
# # 심심해서 만든 졸라맨 코드
# # import turtle
# # t = turtle.Turtle()
# # s = turtle.Screen()
# #
# # t.circle(50)
# # t.right(90)
# # t.forward(150)
# # t.penup()
# # t.setposition(0,0)
# # t.pendown()
# # t.right(45)
# # t.forward(90)
# # t.penup()
# # t.setposition(0,0)
# # t.pendown()
# # t.left(90)
# # t.forward(90)
# # t.penup()
# # t.setposition(0,-150)
# # t.pendown()
# # t.right(80)
# # t.forward(120)
# # t.penup()
# # t.setposition(0,-150)
# # t.pendown()
# # t.left(70)
# # t.forward(120)
# #
# #
# # s.mainloop()
# #
# # import turtle
# # import random
# # import time
# # t = turtle.Turtle()
# # t.shape('turtle')
# # t.shapesize(3)
# # t.color('blue')
# # s = turtle.Screen()
# #
# # playing = True
# #
# # t.up()
# # def up():
# #     t.setheading(90)
# # def down():
# #     t.setheading(270)
# # def left():
# #     t.setheading(180)
# # def right():
# #     t.setheading(0)
# # def space():
# #     global playing
# #     if playing == True:
# #         playing = False
# #     else:
# #         playing = True
# #         # s.clear()
# #         s.reset()
# #         play()
# #
# # s.listen()
# # s.onkeypress(up,"Up")
# # s.onkeypress(down,"Down")
# # s.onkeypress(left,"Left")
# # s.onkeypress(right,"Right")
# # s.onkeypress(space,"space")
# #
# # score = turtle.Turtle()
# # p = turtle.Turtle()
# # p.shape('turtle')
# # p.shapesize(3)
# # p.color('red')
# # p.penup()
# # p.setposition(78,-340)
# # b = turtle.Turtle()
# # b.shape('circle')
# # b.shapesize(1)
# # b.color('green')
# # b.penup()
# # x = random.randint(-300, 300)
# # y = random.randint(-300, 300)
# # b.setposition(x,y)
# # write = turtle.Turtle()
# # write.hideturtle()
# # wall = turtle.Turtle()
# # wall.hideturtle()
# # wall.speed(0)
# # wall.penup()
# # wall.setposition(-480,-400)
# # wall.pendown()
# # wall.pensize(25)
# # wall.left(90)
# # score.hideturtle()
# # score.penup()
# # count = 0
# # score.setposition(400,-330)
# # score.write(count, font=("굴림체", 30, "bold"))
# # t.speed(7)
# # b.speed(0)
# # p.speed(5)
# # score.speed(0)
# # speed_up = turtle.Turtle()
# # speed_up.shape('circle')
# # speed_up.color('aqua')
# # speed_up.hideturtle()
# # speed_up.penup()
# # x2 = random.randint(-300, 300)
# # y2 = random.randint(-300, 300)
# # speed_up.setposition(x2,y2)
# # smaller = turtle.Turtle()
# # smaller.shape('circle')
# # smaller.shapesize(1)
# # smaller.color('black')
# # smaller.hideturtle()
# # smaller.penup()
# # x3 = random.randint(-300, 300)
# # y3 = random.randint(-300, 300)
# # smaller.setposition(x3,y3)
# #
# # sm = random.randint(1,8)
# # while True:
# #     sm = random.randint(1,8)
# #     if sm == 1:
# #         print("test")
# #         smaller.showturtle()
# #         break
# #
# # while True:
# #     u = random.randint(1, 5)
# #     if u == 1:
# #         print("test")
# #         speed_up.showturtle()
# #         break
# # for i in range(2):
# #     wall.forward(800)
# #     wall.right(90)
# #     wall.forward(950)
# #     wall.right(90)
# # eat = 0
# # ate = 0
# # def play():
# #     global playing, count,eat,ate
# #     if eat == 0:
# #         t.forward(7)
# #     else:
# #         for i in range(30):
# #             t.forward(10)
# #
# #     if ate == 0:
# #         t.shapesize(3)
# #     else:
# #         t.shapesize(1)
# #         for i in range(30):
# #             t.forward(7)
# #
# #
# #     t.forward(10)
# #     ang = p.towards(t.pos())
# #     num = random.randint(1, 10)
# #     if num == 1:
# #         p.setheading(ang)
# #     p.forward(10)
# #     if t.distance(p) < 57:
# #         write.write("충돌", font=("굴림체", 30, "bold"))
# #         # time.sleep(5)
# #         playing = False
# #     # print(playing)
# #     b.speed(0)
# #     if t.distance(b) < 60:
# #         x = random.randint(-300, 300)
# #         y = random.randint(-300, 300)
# #         b.setposition(x,y)
# #         count += 1
# #         score.clear()
# #         score.write(count, font=("굴림체", 30, "bold"))
# #     if t.distance(speed_up) < 60:
# #         speed_up.hideturtle()
# #         x2 = random.randint(-300, 300)
# #         y2 = random.randint(-300, 300)
# #         speed_up.setposition(x2,y2)
# #         eat = 1
# #         while True:
# #             u = random.randint(1, 5)
# #             if u == 1:
# #                 print("test")
# #                 speed_up.showturtle()
# #                 break
# #     if t.distance(smaller) < 60:
# #         smaller.hideturtle()
# #         x3 = random.randint(-300, 300)
# #         y3 = random.randint(-300, 300)
# #         smaller.setposition(x3, y3)
# #         ate = 1
# #         sm = random.randint(1, 8)
# #         while True:
# #             sm = random.randint(1, 8)
# #             if sm == 1:
# #                 print("test")
# #                 smaller.showturtle()
# #                 break
# #
# #
# #     if playing:
# #         s.ontimer(play,100)
# #     if t.xcor() > 420:
# #         t.backward(10)
# #         t.right(180)
# #     elif t.xcor() < -420:
# #         t.backward(10)
# #         t.right(180)
# #     elif t.ycor() > 360:
# #         t.backward(10)
# #         t.right(180)
# #     elif t.ycor() < -360:
# #         t.backward(10)
# #         t.right(180)
# #
# #     if p.xcor() > 420:
# #         p.backward(10)
# #         p.right(180)
# #     elif p.xcor() < -420:
# #         p.backward(10)
# #         p.right(180)
# #     elif p.ycor() > 360:
# #         p.backward(10)
# #         p.right(180)
# #     elif p.ycor() < -360:
# #         p.backward(10)
# #         p.right(180)
# # play()
# # s.mainloop()
# # while playing:
# #
# # from flask import Flask
# # app = Flask(__name__)
# # @app.route('/')
# # def home():
# #     return '제발 홍수나서 학교 안 가게 해주세요 제발 홍수나서 학교 안 가게 해주세요 제발 홍수나서 학교 안 가게 해주세요 제발 홍수나서 학교 안 가게 해주세요 제발 홍수나서 학교 안 가게 해주세요 제발 홍수나서 학교 안 가게 해주세요'
# #
# # @app.route('/a')
# # def a():
# #     return 'hi'
# #
# # if __name__ == '__main__':
# #     app.run(debug=True , host = "192.168.0.109", port = "5000")
# #
# # from flask import Flask, render_template
# # app = Flask(__name__)
# # student_data = {
# #     1: {"name": "슈퍼맨", "score": {"국어": 90, "영어": 70, "수학": 65, "과학": 40}},
# #     2: {"name": "배트맨", "score": {"국어": 75, "영어": 80, "수학": 75, "과학": 90}},
# #     3: {"name": "김우찬", "score": {"국어": 90, "영어": 98, "수학": 95, "과학": 100}},
# #     4: {"name": "변예은", "score": {"국어": 95, "영어": 90, "수학": 85, "과학": 95}}
# # }
# # @app.route('/')
# # def index():
# #     return render_template("index.html",
# #             template_students = student_data)
# # @app.route("/student/<int:id>")
# # def student(id):
# #     return render_template("student.html",
# #             template_name=student_data[id]["name"],
# #             template_score=student_data[id]["score"])
# # if __name__ == '__main__':
# #     app.run(debug=True, host = "192.168.0.109")
# #
# #
# # 1번
# # for i in range(1,16):
# #     print(i)
# #
# # 2번
# # a = int(input("100 이하의 숫자를 입력하세요"))
# # i = 1
# # sum = 0
# # while True:
# #     if i == a:
# #         print(sum)
# #         break
# #     # print(i)
# #     i = i + 1
# #     sum = sum + i
# #
# # while i <= a:
# #     # print(i)
# #     sum = sum + i
# #     i = i + 1
# # print(sum)
# #
# # 3번
# # while True:
# #     a = int(input("숫자를 입력하세요"))
# #     if a > 0:
# #         print("이 수는 양수입니다")
# #     if a < 0:
# #         print("이 수는 음수입니다")
# #     if a == 0:
# #         print("프로그램을 종료합니다")
# #         break
# #
# # 4번
# # count = 0
# # sum = 0
# # while True:
# #     a = int(input("숫자를 입력하세요"))
# #     if a >= 100:
# #         print('합계 :',sum, '평균 :', sum/count)
# #         break
# #     count +=1
# #     sum = sum+a
# #
# #
# # 5번
# # a = int(input("숫자를 입력하시오"))
# # for i in range(1,a+1):
# #     print(i)
# #
# # 6번
# # count_even = 0
# # count_odd = 0
# # while True:
# #     a = int(input("숫자를 입력하세요"))
# #     if a ==0:
# #         print("지금까지 입력된 수 중 짝수는",count_even,"개, 홀수는",count_odd,"개입니다")
# #         break
# #     if a % 2 ==0:
# #         count_even += 1
# #     if a % 2 !=0:
# #         count_odd += 1
# #
# # 7번
# # count = 0
# # sum = 0
# # while True:
# #     a = int(input("숫자를 입력하세요"))
# #     if a > 100:
# #         print(sum/count)
# #         break
# #     count+=1
# #     sum = sum + a
# #
# #
# # 8번
# # count = 0
# # while True:
# #     a = int(input("숫자를 입력하세요"))
# #     if a == 0:
# #         print("3과 5의 배수를 제외한 나머지 정수들의 수는",count,"개입니다")
# #     count+=1
# #     if a%3==0 or a%5==0:
# #         count-=1
# #
# # 9번
# # Y = 0
# # y = 0
# #
# # while True:
# #     hight = int(input("높이를 입력하세요"))
# #     base = int(input("밑변의 길이를 입력하세요"))
# #     print("이 삼각형의 넓이는",hight*base/2,"입니다")
# #     con = input("continue?")
# #     if con == 'Y' or con == 'y' or con == 'continue':
# #         pass
# #     else:
# #         break
# #
# # import turtle
# # import time
# # t = turtle.Turtle()
# # s = turtle.Screen()
# # red = turtle.Turtle()
# # blue = turtle.Turtle()
# # timer = turtle.Turtle()
# # timer.hideturtle()
# # red.shape('turtle')
# # blue.shape('turtle')
# # red.shapesize(3)
# # blue.shapesize(3)
# # t.pensize(3)
# # t.hideturtle()
# # t.speed(0)
# # timer.speed(0)
# # timer.penup()
# # red.speed(4)
# # blue.speed(4)
# # red.color('red')
# # blue.color('blue')
# # red.penup()
# # blue.penup()
# # t.penup()
# # red.setposition(-200,300)
# # blue.setposition(-200,-300)
# # t.setposition(300,350)
# # timer.setposition(-440,-75)
# # t.pendown()
# # t.right(90)
# # t.forward(700)
# # t.penup()
# # t.setposition(-100,0)
# #
# # start_red = time.time()
# # start_blue = time.time()
# #
# #
# # def move(x,y):
# #     if blue.xcor()  <= 250 and red.xcor() <= 250:
# #         blue.forward(15)
# #
# #
# #
# # while True:
# #     if red.xcor()>250:
# #         pass
# #     if blue.xcor()>250:
# #         pass
# #     else:
# #         red.forward(1.2)
# #     s.onclick(move)
# #     if blue.xcor()>250:
# #         pass
# #
# #     if red.xcor() > 250:
# #         if red.xcor() > blue.xcor():
# #             t.write("레드 승리", font=("굴림체", 30, "bold"))
# #             end_red = time.time()
# #             timer.write(f"레드가 결승점을  통과하기까지 걸린 시간은 변수 {round(end_red - start_red, 2)} 초 입니다", font=("굴림체", 20, "bold"))
# #             break
# #
# #     if blue.xcor() > 250:
# #         if red.xcor() < blue.xcor():
# #             t.write("블루 승리", font=("굴림체", 30, "bold"))
# #             end_blue = time.time()
# #             timer.write(f"블루가 결승점을  통과하기까지 걸린 시간은 변수 {round(end_blue - start_blue, 2)} 초 입니다", font=("굴림체", 20, "bold"))
# #             break
# # s.mainloop()
# #
# # count_right=0
# # count_wrong=0
# # import random
# # import time
# # start = time.time()
# # for i in range(5):
# #     a=random.randint(1,20)
# #     b=random.randint(1,20)
# #     while True:
# #         answer = input(f"{a} + {b} = ")
# #         if str(answer).isdigit() is False:
# #             print("숫지만 입력할 수 있습니다")
# #             continue
# #         else:
# #             break
# #     if answer==a+b:
# #         print("정답")
# #         count_right+=1
# #     else:
# #         print("오답")
# #         count_wrong+=1
# # end = time.time()
# # print("맞은 개수:",count_right)
# # print("틀린 개수:",count_wrong)
# # print(round(end-start,2),"초 걸림")
# # print("정답률:",count_right*20,"%")
# #
# # a = {}
# #
# # while True:
# #     user = input("과일종류 입력:")
# #     if user == "exit":
# #         print(a)
# #         break
# #     user_1 = input("일개수 입력")
# #     a[user] = user_1
# #
# # while True:
# #     try:
# #         user = input("과일재고 조회",)
# #         print(a[user],"개 있습니다")
# #         if user == "stop":
# #             break
# #     except:
# #         print("제대로 입력해주세요")
# #         pass
# #
# #
# #
# # import turtle
# #
# #
# # s = turtle.Screen()
# #
# # mover = turtle.Turtle()
# # mover.shapesize(3)
# # mover.penup()
# # mover.speed(0)
# # mover.hideturtle()
# #
# # t = turtle.Turtle()
# # t.shapesize(3)
# # t.penup()
# # t.hideturtle()
# #
# # circle = turtle.Turtle()
# # circle.shape("circle")
# # circle.shapesize(3)
# # circle.penup()
# # circle.color('blue')
# # circle.setposition(0,-200)
# #
# #
# # square = turtle.Turtle()
# # square.shape("square")
# # square.shapesize(3)
# # square.penup()
# # square.color('red')
# # square.setposition(300,-200)
# #
# # triangle = turtle.Turtle()
# # triangle.shape("triangle")
# # triangle.shapesize(3)
# # triangle.penup()
# # triangle.color('yellow')
# # triangle.setposition(-300,-200)
# #
# # count_drawing = 0
# # count_filling = 0
# #
# # def move(x,y):
# #     global count_drawing,count_filling
# #     mover.penup()
# #     mover.setposition(x,y)
# #     mover.pendown()
# #     if count_drawing == 0:
# #         if mover.distance(circle) < 20:
# #             count_drawing = 1
# #             t.clear()
# #             t.penup()
# #             t.setposition(0,-100)
# #             t.pencolor('blue')
# #             t.pendown()
# #             t.circle(100)
# #         if -100 < mover.xcor() < 100:
# #             if -100 < mover.ycor() < 100:
# #                 count_filling+=1
# #                 if count_filling%2 != 0:
# #                     t.clear()
# #                     t.pencolor('blue')
# #                     t.begin_fill()
# #                     t.circle(100)
# #                     t.fillcolor('blue')
# #                     t.end_fill()
# #                 if count_filling%2 == 0:
# #                     count_filling += 1
# #                     t.clear()
# #                     t.pencolor('blue')
# #                     t.begin_fill()
# #                     t.circle(100)
# #                     t.fillcolor('white')
# #                     t.end_fill()
# #         count_drawing = 0
# #         if mover.distance(square) < 20:
# #             count_drawing = 1
# #             t.clear()
# #             t.penup()
# #             t.pencolor('red')
# #             t.setposition(100,-100)
# #             t.pendown()
# #             for i in range(4):
# #                 t.left(90)
# #                 t.forward(200)
# #             count_drawing = 0
# #         if mover.distance(triangle) < 20:
# #             count_drawing = 1
# #             t.clear()
# #             t.penup()
# #             t.pencolor('yellow')
# #             t.setposition(-100,-100)
# #             t.pendown()
# #             for i in range(3):
# #                 t.forward(200)
# #                 t.left(120)
# #             count_drawing = 0
# #
# #
# # s.onclick(move)
# #
# #
# #
# #
# # s.mainloop()
# #
# # for i in range(1,9):
# #     print("*" * (6 - i))
# #     if i <= 6:
# #         print("*" * (i - 5))
# #
# # for i in range(1,6):
# #     print(" " * (6 - i) + "*" * i)
# #
# # for i in range(1,9):
# #     if i < 6:
# #         print(" " * (6 - i) + "*" * i)
# #     if i >= 6:
# #         print(" " * (i -4) + "*" * (10 - i))
#
# # a = int(input("숫자를 입력하시오"))
# # value = 0
# # for i in range(1,a):
# #     value = value + i
# #     if value > a:
# #         print(value)
# #         break
# #
# #
# # a = int(input("숫자를 입력하세요"))
# # count_even=0
# # for i in range(1,a+1):
# #     if i % 2 == 0:
# #         count_even += 1
# # print(count_even)
# #
# # for i in range(1,7):
# #     a = []
# #     for j in range(1,7):
# #         a.append([i,j])
# #     print(a)
# #
# # import turtle
# # import random
# # import time
# #
# # t = turtle.Turtle()
# # runer = turtle.Turtle()
# # s = turtle.Screen()
# # count_running = 0
# # t.shapesize(1)
# # runer.shapesize(5)
# # runer.shape('circle')
# # t.speed(0)
# # t.penup()
# # t.setposition(-176,64)
# # runer.penup()
# # runer.speed(0)
# # start = time.time()
# # def move(x,y):
# #     global count_running
# #     t.setposition(x,y)
# #     if t.distance(runer) < 70:
# #         x1 = random.randint(-300, 300)
# #         y1 = random.randint(-300, 300)
# #         runer.setposition(x1, y1)
# #         count_running += 1
# #     if count_running == 5:
# #         end = time.time()
# #         t.write(round(end - start, 2),font=("굴림체",20, "bold"))
# #
# # s.onclick(move)
# #
# # s.mainloop()
# #
# # 1번
# # m = int(input("테이프의 총 길이를 정하세요"))
# # n = int(input("자를 테이프의 길이를 정하세요"))
# #
# # print(m//n,"개","  ",m%n,"cm")
# #
# # for i in range(40):
# #
# #     if str(i)[-1] == "3" or str(i)[-1] == "6" or str(i)[-1] == "9":
# #         if i < 10:
# #             print("x")
# #         if str(i)[0] == "1":
# #             print("1x")
# #         if str(i)[0] == "2":
# #             print("2x")
# #         if str(i)[0] == "3":
# #             print("xx")
# #     else:
# #         print(str(i))
# #
# # a = int(input("지불할 돈을 값을 입력하세요"))
# # b = int(input("살 물건의 값을 입력하세요"))
# # c = a-b
# # d = c//1000
# # e = c-d*1000
# # f = e//500
# # g = e-f*500
# # h = g//100
# # i = g-h*100
# # j = i//50
# # k = i-j*50
# # l = k//10
# # print(d,f,h,j,l)
# #
# # 1번
# # for i in range(1,16):
# #     print(i)
# #
# # 2번
# # a = int(input("100 이하의 숫자를 입력하세요"))
# # i = 0
# # sum = 0
# # while True:
# #     if i == a:
# #         print(sum)
# #         break
# #     i = i + 1
# #     sum = sum + i
# #
# # 3번
# # while True:
# #     a = int(input("숫자를 입력하세요"))
# #     if a > 0:
# #         print("양수입니다")
# #     if a < 0:
# #         print("음수입니다")
# #     if a == 0:
# #         print("프로그램을 종료합니다")
# #         break
# #
# # import turtle
# # t = turtle.Turtle()
# # s = turtle.Screen()
# #
# # t.speed(0)
# #
# # def square(x):
# #     for i in range(4):
# #         t.forward(x)
# #         t.right(90)
# #
# # for i in range(36):
# #     square(300)
# #     t.left(10)
# #
# # s.mainloop()
# #
# # import turtle
# # t = turtle.Turtle()
# # s = turtle.Screen()
# #
# # t.speed(0)
# # t.shape('circle')
# # t.penup()
# #
# # def stamp():
# #     for i in range(5):
# #         t.stamp()
# #         t.forward(50)
# #
# # for j in range(7):
# #     t.setposition(0,-50*j)
# #     stamp()
# # t.forward(-50)
# # s.mainloop()
# #
# # import turtle
# # import time
# # t = turtle.Turtle()
# # second_1 = turtle.Turtle()
# # minute = turtle.Turtle()
# # hour = turtle.Turtle()
# # s = turtle.Screen()
# #
# # second_1.hideturtle()
# # minute.hideturtle()
# # t.speed(0)
# # t.penup()
# #
# # for i in range(0,13):
# #     t.setheading(30*i)
# #     t.forward(200)
# #     t.pendown()
# #     t.forward(75)
# #     t.penup()
# #     t.forward(25)
# #     if i > 2:
# #         t.write(15-i)
# #     if i < 3:
# #         t.write(3-i)
# #     t.setposition(0,0)
# #     if i == 11:
# #         t.setheading(0)
# #         break
# #
# # s.tracer(0)
# # second_head = -271
# # minute_head = -270
# # hour_head = -270
# # minute.setheading(-270)
# # minute.forward(175)
# # minute.setposition(0,0)
# # hour.setheading(-270)
# # hour.forward(90)
# # hour.setposition(0,0)
# # count_c = 0
# # count_m = 0
# # count_round = 0
# #
# # def clock():
# #     global second_head,count_c, minute_head, count_m, hour_head
# #     t.setheading(second_head)
# #     second_1.setheading(second_head)
# #     second_1.forward(175)
# #     second_1.up()
# #     second_1.backward(175)
# #     second_1.down()
# #     s.update()
# #     second_1.clear()
# #     time.sleep(1)
# #     second_head -= 6
# #     count_c += 1
# #     if count_c == 60:
# #         minute_head -= 6
# #         count_c = 0
# #         minute.clear()
# #         minute.setheading(minute_head)
# #         minute.forward(175)
# #         minute.up()
# #         minute.backward(175)
# #         minute.down()
# #         count_m += 1
# #         if count_m == 60:
# #             count_m = 0
# #             hour_head -= 30
# #             hour.clear()
# #             hour.setheading(hour_head)
# #             hour.forward(90)
# #             hour.up()
# #             hour.backward(90)
# #             hour.down()
# #
# #
# # while True:
# #     clock()
# #
# # import turtle
# # import random
# # import time
# #
# # s = turtle.Screen()
# # grid_list = [[x,y] for x in range(-150,150,50) for y in range(-150,150,50)]
# #
# # dict_list = {}
# # level = 1
# # click_count = 0
# # playing = 0
# # selcet_list = []
# # grid_t = turtle.Turtle()
# # grid_t.shape('square')
# # grid_t.speed(0)
# # grid_t.penup()
# # grid_t.shapesize(2.2)
# # point_t = turtle.Turtle()
# # point_t.shape('square')
# # point_t.speed(0)
# # point_t.penup()
# # point_t.shapesize(2.2)
# # write_t = turtle.Turtle()
# # write_t.hideturtle()
# # write_t.penup()
# # write_t.setposition(-200,200)
# #
# # def make_grid():
# #     grid_t.color("black")
# #     for i in grid_list:
# #         grid_t.setposition(i[0],i[1])
# #         grid_t.stamp()
# #
# # def level_up(level):
# #     global selcet_list,dict_list
# #     selcet_list = random.sample(grid_list,level)
# #     for j,i in enumerate(selcet_list):
# #         print(selcet_list)
# #         grid_t.setposition(i[0], i[1])
# #         grid_t.color('yellow')
# #         grid_t.stamp()
# #         dict_list[j] = [i[0],i[1]]
# #
# #
# #
# #
# # def cl_t(x,y):
# #     global click_count,selcet_list,start,playing
# #     point_t.setposition(x,y)
# #     for i in selcet_list:
# #         if int(x) > i[0]-22 and int(x) < i[0]+22 and int(y) > i[1]-22 and int(y) < i[1]+22:
# #             print(i[0],i[1],"명중")
# #             point_t.setposition(i[0],i[1])
# #             point_t.stamp()
# #             click_count += 1
# #             print(click_count)
# #         if click_count == 15:
# #             end = time.time()
# #             write_t.write(round(end - start, 2),font=("굴림체",20, "bold"))
# #
# #
# #
# # make_grid()
# # level_up(15)
# # start = time.time()
# # s.onclick(cl_t)
# #
# #
# #
# #
# # s.mainloop()
# #
# # import turtle
# # import time
# # import random
# #
# # s = turtle.Screen()
# # s.delay(0)
# # grid_list = [[x,y] for x in range(-200,200,100) for y in range(-100,300,100)]
# # grid_t = turtle.Turtle()
# # grid_t.hideturtle()
# # grid_t.speed(0)
# # player_t = turtle.Turtle()
# # player_t.shape('circle')
# # player_t.shapesize(4)
# # player_t.color('green')
# # player_t.penup()
# # player_t.speed(0)
# # write_t = turtle.Turtle()
# # write_t.hideturtle()
# # write_t.penup()
# # write_t.setposition(-250,250)
# # bomb1_t = turtle.Turtle()
# # bomb1_t.shape('circle')
# # bomb1_t.shapesize(4)
# # bomb1_t.penup()
# # bomb2_t = turtle.Turtle()
# # bomb2_t.shape('circle')
# # bomb2_t.shapesize(4)
# # bomb2_t.penup()
# # dodge = 0
# # life = 0
# # grid_t.penup()
# # grid_t.setposition(-200,200)
# # grid_t.pendown()
# # for j in grid_list:
# #     grid_t.penup()
# #     grid_t.setposition(j[0],j[1])
# #     grid_t.pendown()
# #     for j in range(4):
# #         grid_t.forward(100)
# #         grid_t.right(90)
# #
# # x = -150
# # y = 150
# # player_t.setposition(x,y)
# # def left():
# #     global x
# #     x-=100
# #     if x < - 200:
# #         x+=100
# #     player_t.setx(x)
# #     print(x)
# # def right():
# #     global x
# #     x+=100
# #     if x > 200:
# #         x-=100
# #     player_t.setx(x)
# #     print(x)
# # def up():
# #     global y
# #     y += 100
# #     if y > 200:
# #         y-=100
# #     player_t.sety(y)
# #     print(y)
# # def down():
# #     global y
# #     y -= 100
# #     if y < -200:
# #         y+=100
# #     player_t.sety(y)
# #     print(y)
# #
# # def text():
# #     write_t.clear()
# #     write_t.write(dodge, font=("굴림체", 30, "bold"), align="center")
# #
# # bomb1_t.setposition(-500,random.choice([-150,-50,50,150]))
# # bomb2_t.right(90)
# # bomb2_t.setposition(random.choice([-150, -50, 50,150]),300)
# #
# #
# # s.onkeypress(left,"Left")
# # s.onkeypress(right,"Right")
# # s.onkeypress(up,"Up")
# # s.onkeypress(down,"Down")
# # s.listen()
# # s.tracer(0)
# #
# # playing = True
# # while True:
# #
# #     if bomb1_t.xcor() > 400:
# #         bomb1_t.setposition(-500,random.choice([-150,-50,50,150]))
# #         dodge += 1
# #         text()
# #     if bomb2_t.ycor() < -400:
# #         bomb2_t.setposition(random.choice([-150, -50, 50,150]),300)
# #         dodge += 1
# #         text()
# #
# #     if bomb1_t.distance(player_t) < 70 or bomb2_t.distance(player_t) < 70:
# #         life += 1
# #         if life == 1:
# #             player_t.color('yellow')
# #         if life == 2:
# #             player_t.color('orange')
# #         if life == 3:
# #             player_t.color('red')
# #         if life == 4:
# #             write_t.clear()
# #             write_t.write("D지셨습니다", font=("굴림체", 30, "bold"), align="center")
# #             bomb1_t.clear()
# #             bomb2_t.clear()
# #             playing=False
# #
# #
# #         x = -150
# #         y = 150
# #
# #         bomb1_t.setposition(-500, random.choice([-150, -50, 50, 150]))
# #         bomb2_t.setposition(random.choice([-150, -50, 50, 150]), 300)
# #         player_t.setposition(-150,150)
# #
# #     if playing is True:
# #         bomb1_t.forward(7)
# #         bomb2_t.forward(7)
# #
# #     time.sleep(0.01)
# #     s.update()
# #
# #
# #
# # a = [1,2,3,4,5,6,234,324,324,534,5435,6,456,54,657,65,7865,756,756,74,553,45,3454,7,567,68,678,678,56,634,534,5,476,587,68,768,67,8678,46,456,456,45,645,645,645]
# # b = []
# # def f_a(a):
# #     for i in range(0,len(a)-1):
# #         if a[i] % 2 == 0:
# #             b.append(a[i])
# # f_a(a)
# #
# # print(b)
# #
# # l = []
# # def make_list(a):
# #     for i in range(0,len(a)):
# #         l.append(a[i])
# # make_list("abcd")
# # print(l)
# #
# # def make_url(a):
# #     print("www."+a+".com")
# #
# # make_url("naver")
# #
# # def print_reverse(a):
# #     print(a[-1::-1])
# #
# # print_reverse("python")
# #
# # import turtle
# # t = turtle.Turtle()
# # s = turtle.Screen()
# #
# # 1번
# # t.speed(0)
# # t.penup()
# # t.setposition(0,300)
# # def circle():
# #     t.right(90)
# #     t.forward(100)
# #     t.pendown()
# #     t.left(90)
# #     t.circle(25)
# #
# # def square():
# #     t.forward(25)
# #     t.right(90)
# #     for i in range(3):
# #         t.forward(50)
# #         t.right(90)
# #     t.forward(25)
# #     t.penup()
# #
# #
# # for i in range(4):
# #     circle()
# #     square()
# #
# #
# # s.mainloop()
# #
# # 2번
# # t.speed(0)
# # for i in range(36):
# #     t.circle(10)
# #     t.penup()
# #     t.left(10)
# #     t.forward(20)
# #     t.pendown()
# #
# # s.mainloop()
# #
# # 3번
# # t.speed(0)
# # for i in range(36):
# #     t.begin_fill()
# #     if i % 3 == 0:
# #         t.fillcolor("red")
# #     elif  i % 2 == 0:
# #         t.fillcolor("green")
# #     else:
# #         t.fillcolor("blue")
# #     t.circle(10)
# #     t.end_fill()
# #     t.penup()
# #     t.left(10)
# #     t.forward(20)
# #     t.pendown()
# #
# # s.mainloop()
# #
# # 4번
# # t.speed(0)
# # t.penup()
# # t.setposition(0,100)
# # t.left(120)
# # t.pensize(5)
# # t.pendown()
# # for i in range(8):
# #     if i%2==0:
# #         t.color("blue")
# #     else:
# #         t.color("green")
# #     t.forward(50)
# #     if i%2==0:
# #         t.left(120)
# #     else:
# #         t.right(120)
# # t.left(240)
# # t.color("red")
# # t.forward(200)
# #
# # s.mainloop()
# #
# # 1번
# # for i in range(1,16):
# #     print(i)
# #
# # 2번
# # while True:
# #     num = 0
# #     a = int(input("100이하의 숫자를 입력하세요"))
# #     for i in range(1,a+1):
# #         num = num+i
# #     print(num)
# #     break
# #
# # 3번
# # while True:
# #     a = int(input("숫자를 입력하시오"))
# #     if a == 0:
# #         break
# #
# #     if a%2 == 0:
# #         print("양수입니다")
# #     else:
# #         print("음수입니다")
# #
# # 4번
# # num = 0
# # count = 0
# # while True:
# #     a = int(input("숫자를 입력하시오"))
# #     count+=1
# #     num = num+a
# #     if a >= 100:
# #         result = num/count
# #         print(num)
# #         print(result)
# #         break
# #
# # 5번
# # a = int(input("숫자를 입력하시오"))
# # for i in range(1,a+1):
# #     print(i)
# #
# # 6번
# # count_even = 0
# # count_odd = 0
# # while True:
# #     a = int(input("숫자를 입력하시오"))
# #     if a == 0:
# #         print(count_odd)
# #         print(count_even)
# #         break
# #     if a%2 == 0:
# #         count_even+=1
# #     else:
# #         count_odd+=1
# #
# # 7번
# # num = 0
# # count = 0
# # while True:
# #     a = int(input("숫자를 입력하시오"))
# #     if a < 0 or a > 100:
# #         print(num)
# #         print(num/count)
# #         break
# #     count += 1
# #     num = num + a
# #
# # 8번
# # count = 0
# # while True:
# #     a = int(input("숫자를 입력하시오"))
# #     if a == 0:
# #         print(count)
# #         break
# #     if a%3==0 or a%5==0:
# #         pass
# #     else:
# #         count+=1
# #
# # 9번
# # while True:
# #     a = int(input("삼각형의 밑변의 길이를 입력하시오"))
# #     b = int(input("삼각형의 높이를 입력하시오"))
# #     print(a*b/2)
# #     c = input("Continue?")
# #     if c == "Y" or "y":
# #         pass
# #     if c != "Y" or "y":
# #         break
# #
# # 1번
# # n = int(input("숫자를 입력하시오"))
# # for i in range(1, n + 1):
# #     for j in range(1, i + 1):
# #         print(j, end ='')
# #     print("")
# #
# # 2번
# # n = int(input("숫자 입력를 입력하시오"))
# # for i in range(n, -1, -1):
# #     print(i)
# #
# # 3번
# # a = input("숫자를 입력하시오")
# # b = 0
# # for i in range(0,len(a)):
# #     b = b + int(a[i])
# # print(b)
# #
# # 4번
# # a = int(input("숫자를 입력하시오"))
# # b = int(input("숫자를 입력하시오"))
# # c = int(input("숫자를 입력하시오"))
# # print(a+b+c)
# #
# # 5번
# # a = input("글자를 입력해주시오")
# # b = input("글자를 입력해주시오")
# # c = input("글자를 입력해주시오")
# #
# # print(c)
# # print(b)
# # print(a)
# #
# # 6번
# # n = int(input("숫자를 입력하시오"))
# # for i in range(1,2*n):
# #     if i > n:
# #         print("*"*((2*n)-i))
# #     else:
# #         print("*"*i)
# #
# # import turtle
# # import random
# #
# # s = turtle.Screen()
# #
# # player1 = turtle.Turtle()
# # player1.shapesize(3)
# # player1.color('red')
# # player1.shape('turtle')
# # player1.penup()
# # player1.speed(0)
# # player1.setposition(-300,300)
# #
# # player2 = turtle.Turtle()
# # player2.shapesize(3)
# # player2.color("blue")
# # player2.shape("turtle")
# # player2.penup()
# # player2.speed(0)
# # player2.setposition(-300,100)
# #
# # player3 = turtle.Turtle()
# # player3.shapesize(3)
# # player3.color("green")
# # player3.shape("turtle")
# # player3.penup()
# # player3.speed(0)
# # player3.setposition(-300,-100)
# #
# # player4 = turtle.Turtle()
# # player4.shapesize(3)
# # player4.color("yellow")
# # player4.shape("turtle")
# # player4.penup()
# # player4.speed(0)
# # player4.setposition(-300,-300)
# #
# # end_line = turtle.Turtle()
# # end_line.hideturtle()
# # end_line.speed(0)
# # end_line.penup()
# # end_line.setposition(350,-500)
# # end_line.left(90)
# # end_line.pensize(10)
# # end_line.pendown()
# # end_line.forward(1200)
# #
# # write = turtle.Turtle()
# # write.hideturtle()
# # write.speed(0)
# # winner = turtle.Turtle()
# # winner.hideturtle()
# # winner.penup()
# # winner.speed(0)
# # winner.sety(50)
# #
# # bet = s.textinput("입력", "배팅할 색상을 선택(red or blue or green)")
# # print(bet)
# #
# # while True:
# #     player1.forward(random.randint(1,5))
# #     player2.forward(random.randint(1,5))
# #     player3.forward(random.randint(1,5))
# #     player4.forward(random.randint(1,5))
# #     if player1.xcor() > 297 or player2.xcor() > 297 or player3.xcor() > 297 or player4.xcor() > 297:
# #         break
# #
# # if player1.xcor() > player2.xcor() and player1.xcor() > player3.xcor() and player1.xcor() > player4.xcor():
# #     winner.write("레드 승리", font=("굴림체", 30, "bold"))
# #     if bet == "red":
# #         write.write("배팅 성공", font=("굴림체", 30, "bold"))
# #     else:
# #         write.write("배팅 실패", font=("굴림체", 30, "bold"))
# #
# # elif player2.xcor() > player1.xcor() and player2.xcor() > player3.xcor() and player2.xcor() > player4.xcor():
# #     winner.write("블루 승리", font=("굴림체", 30, "bold"))
# #     if bet == "blue":
# #         write.write("배팅 성공", font=("굴림체", 30, "bold"))
# #     else:
# #         write.write("배팅 실패", font=("굴림체", 30, "bold"))
# #
# # elif player3.xcor() > player1.xcor() and player3.xcor() > player2.xcor() and player3.xcor() > player4.xcor():
# #     winner.write("그린 승리", font=("굴림체", 30, "bold"))
# #     if bet == "green":
# #         write.write("배팅 성공", font=("굴림체", 30, "bold"))
# #     else:
# #         write.write("배팅 실패", font=("굴림체", 30, "bold"))
# #
# # elif player4.xcor() > player1.xcor() and player4.xcor() > player2.xcor() and player4.xcor() > player3.xcor():
# #     winner.write("옐로우 승리", font=("굴림체", 30, "bold"))
# #     if bet == "yellow":
# #         write.write("배팅 성공", font=("굴림체", 30, "bold"))
# #     else:
# #         write.write("배팅 실패", font=("굴림체", 30, "bold"))
# #
# # s.mainloop()
#
#
# # 숫자두개를 입력 받는다.
# # 첫번째 숫자는 총 숫자의 갯수를 의미하고
# # 두번째 입력은 첫번째로 입력된 숫자 만큼 입력 받는다.
# # 이렇게 입력받은 숫자를 내림차순으로 정렬하는 함수를 작성
#
# # def arrange():
# #     list = []
# #     a = int(input("몇 번 입력 하실 지 입력하시오"))
# #     for i in range(a):
# #         b = int(input("숫자를 입력하시오"))
# #         list.append(b)
# #     list.sort(reverse=True)
# #     return list
# #
# # c = arrange()
# # print(c)
#
#
# #
# # 숫자 두개를 입력받아
# # 첫번 쨰 수부터 두번째 수까지 구구단 출력
#
# # a = int(input("숫자를 입력하시오"))
# # b = int(input("숫자를 입력하시오"))
# #
# # if b < a:
# #     for i in range(b,a+1,1):
# #         print("")
# #         for j in range(1, 10):
# #             print(i, "x", j, "=", i * j)
# # else:
# #     for i in range(a,b+1):
# #         print("")
# #         for j in range(1,10):
# #             print(i,"x",j,"=",i*j)
#
#
#
# # for i in range(1,10):
# #     print(a,"x",i,"=",a*i)
# # print("")
# # for j in range(1,10):
# #     print(b,"x",j,"=",b*j)
#
# # 1번
# # def solution(k,n):
# #     if 2 <= k <= 100:
# #         if 1 <= n <= 100:
# #             for i in range(0,n):
# #                 print(k+3*i,end=" ")
# #         else:
# #             print("숫자가 범위를 벗어났습니다")
# #     else:
# #         print("숫자가 범위를 벗어났습니다")
# # solution(7,5)
#
# # 2번
# # def solution(n):
# #     if 1 <= len(n) <= 10000:
# #         for i in range(0,len(n)):
# #             if n[i] == 7:
# #                 print(i)
# #                 break
# #     else:
# #         print("숫자가 범위를 벗어났습니다")
# #
# # solution([45,67,67,98,12,7])
#
# # 3번
# # def solution(n,m):
# #     if -1000 <= n <= 1000 and -1000 <= m <= 1000 and n != m:
# #         if n < m:
# #             print(n)
# #         else:
# #             print(m)
# #     else:
# #         print("숫자가 범위를 벗어났습니다")
# #
# # solution(64,27)
#
# # 4번
# # def solution(arr):
# #     if 1 <= len(arr) <= 10000:
# #         sum = 0
# #         for n in range(1,len(arr),2):
# #             if 0 <= arr[n] <= 1000:
# #                 sum = arr[n]+ sum
# #             else:
# #                 print("문자가 범위를 벗어났습니다")
# #         print('%d' % sum)
# #     else:
# #         print("문자가 범위를 벗어났습니다")
# #
# # solution([41,23,27,0,12,36,30])
#
# # 5번
# # def solution(n):
# #     for i in range(0,n):
# #         print("_"*i,end="")
# #         print("*"*(n-i),end="")
# #
# # solution(5)
#
# # 6번
# # def solution(str):
# #     counter = 0
# #     if 1 <= len(str) <= 100:
# #         if str.isalpha(True):
# #             for i in range(0,len(str)):
# #                 if str[i].islower():
# #                     counter += 1
# #             print('%d' % counter)
# #         else:
# #             print("문자가 알파벳이 아닙니다")
# #     else:
# #         print("문자가 범위를 벗어났습니다")
# #
# # solution("IOtwer")
#
# # 7번
# # def solution(str1,str2):
# #     print(str1,"&",str2,sep = "")
# #
# # solution("peach","lemon")
#
# # 8번
# # def solution(str1,str2):
# #     if 1 <= len(str1) <= 100 and 1 <= len(str2) <= 100 and str1.islower and str2.islower:
# #         if str1 > str2:
# #             print(str2)
# #         if str1 < str2:
# #             print(str1)
# #     else:
# #         print("문자가 범위를 벗어났습니다")
# #
# # solution("yellow","green")
#
# # 9번
# # def solution(str):
# #     if 1 <= len(str) <= 100:
# #         if str.isalpha(True):
# #             for i in range(0,len(str)):
# #                 for j in range(0,i+1):
# #                     print('%s' %str[j],end="")
# #                 print(end=" ")
# #         else:
# #             print("문자가 알파벳이 아닙니다")
# #     else:
# #          print("문자가 범위를 벗어났습니다")
# #
# # solution("IoT")
#
# # 10번
# # def solution(n1,n2):
# #     if -1000 <= n1 <= 1000 and -1000 <= n2 <= 1000:
# #         print(abs(n1-n2))
# #
# # solution(2,5)
#
# # for i in range(1,10):
# #     if i < 6:
# #         print(" " * (6 - i) + "*" * i)
# #     if i >= 6:
# #         print(" " * (i -4) + "*" * (10 - i))
#
# # 1번
# # def solution():
# #     n = int(input("숫자를 입력하시오"))
# #     for i in range(1,n+1):
# #         for j in range(1,i+1):
# #             print(j,end=" ")
# #         print()
# #
# # solution()
#
# # 2번
# # def solution():
# #     n = int(input("숫자를 입력하시오"))
# #     for i in range(n,-1,-1):
# #         print(i)
# # solution()
#
# # 3번
# # def solution():
# #     a = input("숫자를 입력하시오")
# #     answer = 0
# #     for i in range(0,len(a)):
# #         answer += int(a[i])
# #     print(answer)
# # solution()
#
# # 4번
# # def solution():
# #     a = int(input("숫자를 입력하시오"))
# #     b = int(input("숫자를 입력하시오"))
# #     c = int(input("숫자를 입력하시오"))
# #     print(a+b+c)
# # solution()
#
# # 5번
# # def solution():
# #     a = input("문자를 입력하시오")
# #     b = input("문자를 입력하시오")
# #     c = input("문자를 입력하시오")
# #     print(c,b,a,sep='\n')
# # solution()
#
# # 6번
# # def solution():
# #     n = int(input("숫자를 입력하시오"))
# #     for i in range(1,2*n):
# #         if i > n:
# #             print("*"*((2*n)-i))
# #         else:
# #             print("*"*i)
# # solution()
#
# # 7번
# # def solution():
# #     n = input("문자를 입력하시오")
# #     if n.islower():
# #         print("1")
# #     if n.isupper():
# #         print("0")
#
# # 8번
# # def solution():
# #     n = int(input("숫자를 입력하시오"))
# #     if n > 0:
# #         print(n*3)
# #     elif n < 0:
# #         print(n*2)
# #     elif n == 0:
# #         print("0")
# # solution()
#
# # 9번
# # def solution():
# #     a = input("문자를 입력하시오")
# #     b = input("문자를 입력하시오")
# #     if len(a)%len(b) == 0:
# #         if len(a) != 0 and len(b) != 0:
# #             print(len(a)//len(b))
# # solution()
#
# # 10번
# # def solution():
# #     count = 0
# #
# #     while True:
# #         a = int(input("숫자를 입력하시오"))
# #         count += 1
# #         if a == 10:
# #             print(count)
# #             break
# #
# # solution()
#
# # 1번
# # def solution():
# #     n = input("문자를 입력해주세요")
# #     print("'"+n+"'")
# # solution()
#
# # 2번
# # def solution():
# #     n = int(input("숫자를 입력해주세요"))
# #     for i in range(1,n+1):
# #         print(10*i)
# # solution()
#
# # 3번
# # def solution():
# #     a,b = input("숫자를 입력해주세요").split()
# #     a = int(a)
# #     b = int(b)
# #     if 1 <= a <= 100 and 1 <= b <= 100:
# #         if a > b:
# #             print(a-b)
# # solution()
#
# # 4번
# # def solution():
# #     s = input("문자를 입력하세요")
# #     name_list = list(s)
# #     name_list.reverse()
# #     s = ''.join(name_list)
# #     print(s)
# # solution()
#
# # 5번
# # def solution():
# #     n = int(input("배열의 길이를 입력해주세요"))
# #     arr = input("배열의 길이만큼 숫자를 입력해주세요").split()
# #     for i in range(n):
# #         arr[i] = int(arr[i])
# #     for i in range(0,n-1):
# #         print(arr[i+1]-arr[i],end = ' ')
# # solution()
#
# # 6번
# # def solution():
# #     for i in range(2,10):
# #         for j in range(1,10):
# #             print(i,'*',j,'=',i*j)
# # solution()
#
# # 7번
# # def solution():
# #     n = int(input("숫자를 입력하시오"))
# #     for i in range(1,n+1):
# #         if n%i==0:
# #             print(i,end=' ')
# # solution()
#
# # 8번
# # def solution():
# #     n = int(input("당신의 키를 입력하세요"))
# #     if n >= 150:
# #         print("True")
# #     if n < 150:
# #         print("False")
# # solution()
#
# # 9번
# # def solution():
# #     a = int(input("숫자를 입력하시오"))
# #     b = int(input("숫자를 입력하시오"))
# #     if 1 <= a <= 500 and 1 <= b <= 500:
# #         if a > b:
# #             print(a*b)
# #             print(a//b)
# # solution()
#
# # for i in range(1,4):
# #     print("*"*i)
#
# # def solution(n):
# #     for i in range(1,n+1):
# #         print("*"*i)
# # solution(5)
#
# # for i in range(1,7):
# #     if i < 4:
# #         print("*"*i)
# #     else:
# #         print("*"*(-1*i+7))
#
# # def solution(n):
# #     for i in range(1,n+1):
# #         if i < n//2+1:
# #             print("*"*(-1*i+4))
# #         else:
# #             print("*"*(i-3))
# # solution(6)
#
# # def solution(n):
# #     for i in range(1,n+1):
# #         print(" "*(i-1)+"*"*(-1*i+4))
# # solution(3)
#
# # * ** *** **** *****
# #
# # for i in range(1,6):
# #     print("*"*i,end=" ")
#
#
# #     *
# #    **
# #   ***
# #  ****
# # *****
#
# # for i in range(1,6):
# #     print(" "*(-1*i+5)+"*"*i)
#
# #
# # def solution(arr):
# #     a = []
# #     count = 1
# #     for i in range(0,len(arr)-1):
# #         if (arr[i + 1] - arr[i]) > 0:
# #             count += 1
# #         if (arr[i + 1] - arr[i]) <= 0 or i == len(arr)-2:
# #             a.append(count)
# #             print(count)
# #             count = 1
# #     largest = a[0]
# #     print(a)
# #     for l in a:
# #         if l > largest:
# #             largest = l
# #             return largest
# # #
# # #
# # print(solution([3,1,2,4,5,1,2,2,3,4]))
#
# # k = int(input("숫자를 입력해주세요"))
# # n = int(input("숫자를 입력해주세요"))
# #
# # if 2 <= k <= 100 and 1 <= n <= 100:
# #     for i in range(0,n):
# #         print(k+(3*i),end=" ")
# # else:
# #     print("숫자가 범위에서 벗어납니다")
#
# # a = int(input("숫자를 입력해주세요"))
# # b = int(input("숫자를 입력해주세요"))
# #
# # if -1000 <= a <= 1000 and -1000 <= b <= 1000 and a != b:
# #     if a > b:
# #         print(b)
# #     else:
# #         print(a)
# # else:
# #     print("숫자가 범위에서 벗어납니다")
#
# # n = int(input("숫자를 입력해주세요"))
# # arr = list(map(int,input("위에 입력한 만큼 숫자를 입력해주세요").split()))
# # sum = 0
# # for i in range(1, n, 2):
# #     sum += arr[i]
# # print("%d" % sum)
#
# # n = int(input("숫자를 입력해주세요"))
# # for i in range(0,n):
# #     print("_"*i,end="")
# #     print("*"*(n-i),end="")
#
# # counter = 0
# # str = input("영어 문자를 입력해주시오")
# #
# # for i in range(0,len(str)):
# #     if str[i].islower():
# #         counter += 1
# # print("%d" % counter)
#
# # str1 = input("영어 문자를 입력해주시오")
# # str2 = input("영어 문자를 입력해주시오")
# #
# # print(str1,"&",str2,sep = "")
#
# # str = input("영어 문자를 입력하시오")
# #
# # if 1 <= len(str) <= 100:
# #     if str.isalpha():
# #         for i in range(0, len(str)):
# #             for j in range(0, i + 1):
# #                 print('%s' % str[j], end="")
# #             print(end=" ")
# #     else:
# #         print("문자가 알파벳이 아닙니다")
# # else:
# #     print("문자가 범위를 벗어났습니다")
#
# # n1 = int(input("숫자를 입력하시오"))
# # n2 = int(input("숫자를 입력하시오"))
# # if -1000 <= n1 <= 1000 and -1000 <= n2 <= 1000:
# #     print(abs(n1-n2))
#
# # 1번
# # import turtle
# # t = turtle.Turtle()
# # s = turtle.Screen()
#
# # for i in range(3):
# #     t.forward(30)
# #     t.left(120)
#
# # 2번
# # for i in range(3):
# #     for j in range(3):
# #         t.forward(50)
# #         t.left(120)
# #     t.forward(50)
#
# # 5번
# # length = 50
# # for i in range(3):
# #     t.forward(length)
# #     t.left(120)
#
# # 6번
# # length = 50
# # for i in range(3):
# #     for j in range(3):
# #         t.forward(length)
# #         t.left(120)
# #     t.forward(length)
#
# # 7번
# # length = 50
# # for i in range(3):
# #     for j in range(3):
# #         t.forward(length)
# #         t.left(120)
# #     t.forward(length)
# #     t.right(90)
# #     t.penup()
# #     t.forward(length)
# #     t.pendown()
# #     t.left(90)
#
# # 8번
# # length = 50
# # for i in range(3):
# #     for j in range(3):
# #         t.forward(length)
# #         t.left(120)
# #     t.forward(length)
# #     t.right(90)
# #     t.penup()
# #     t.forward(length)
# #     t.pendown()
# #     t.left(90)
# # for l in range(3):
# #     for u in range(3):
# #         t.forward(length)
# #         t.left(120)
# #     t.penup()
# #     t.forward(length)
# #     t.left(90)
# #     t.forward(length)
# #     t.right(90)
# #     t.pendown()
#
# # 9번
# # length = 60
# # for i in range(3):
# #     for j in range(3):
# #         t.forward(length)
# #         t.left(120)
# #     t.forward(length)
# #     t.right(90)
# #     t.penup()
# #     t.forward(length)
# #     t.pendown()
# #     t.left(90)
# # for l in range(3):
# #     for u in range(3):
# #         t.forward(length)
# #         t.left(120)
# #     t.penup()
# #     t.forward(length)
# #     t.left(90)
# #     t.forward(length)
# #     t.right(90)
# #     t.pendown()
#
# # 10번
# # length = 80
# # for i in range(4):
# #     for j in range(4):
# #         t.forward(length)
# #         t.left(90)
# #     t.penup()
# #     t.forward(length)
# #     t.right(90)
# #     t.forward(length)
# #     t.left(90)
# #     t.pendown()
#
# # s.mainloop()
#
# import turtle
# t = turtle.Turtle()
# s = turtle.Screen()
# t1 = turtle.Turtle()
# t2 = turtle.Turtle()
# t3 = turtle.Turtle()
# t4 = turtle.Turtle()
# t5 = turtle.Turtle()
# t6 = turtle.Turtle()
# t1.hideturtle()
# t2.hideturtle()
# t3.hideturtle().
#
# t4.hideturtle()
# t5.hideturtle()
# t6.hideturtle()
# t.penup()
# t1.penup()
# t2.penup()
# t3.penup()
# t4.penup()
# t5.penup()
# t6.penup()
# t.shape("turtle")
# t.shapesize(2)
# t.setheading(180)
# t.setposition(75,75)
# t1.setposition(-25,50)
# t2.setposition(-75,50)
# t3.setposition(-75,-50)
# t4.setposition(-75,-100)
# t5.setposition(25,-100)
# t6.setposition(75,-100)
#
# t1.write("2",font=("굴림체", 30, "bold"))
# t2.write("2",font=("굴림체", 30, "bold"))
# t3.write("2",font=("굴림체", 30, "bold"))
# t4.write("2",font=("굴림체", 30, "bold"))
# t5.write("2",font=("굴림체", 30, "bold"))
# t6.write("2",font=("굴림체", 30, "bold"))
#
# a = 2
#
# def collect_flower():
#     global a
#     if t.xcor() == -25 and t.ycor() == 75:
#         t1.clear()
#         t1.write(a-1, font=("굴림체", 30, "bold"))
#         a -= 1
#     elif t.xcor() == -75 and t.ycor() == -25:
#         t3.clear()
#         t3.write(a - 1, font=("굴림체", 30, "bold"))
#         a -= 1
#     elif t.xcor() == 25 and t.ycor() == -75:
#         t5.clear()
#         t5.write(a - 1, font=("굴림체", 30, "bold"))
#         a -= 1
#
# def make_honey():
#     global a
#     if t.xcor() == -75 and t.ycor() == 75:
#         t2.clear()
#         t2.write(a-1, font=("굴림체", 30, "bold"))
#         a -= 1
#     elif t.xcor() == -75 and t.ycor() == -75:
#         t4.clear()
#         t4.write(a-1, font=("굴림체", 30, "bold"))
#         a -= 1
#     elif t.xcor() == 75 and t.ycor() == -75:
#         t6.clear()
#         t6.write(a-1, font=("굴림체", 30, "bold"))
#         a -= 1
#
# def collect():
#     global a,pillage
#     a = 2
#     for i in range(pillage):
#         t.forward(50)
#     for i in range(pillage):
#         collect_flower()
#     t.forward(50)
#     a = 2
#     for i in range(pillage):
#         make_honey()
#     t.left(90)
#
# pillage = 2
# for j in range(3):
#     collect()
#
# s.mainloop()

# import turtle
# import random
# t = turtle.Turtle()
# s = turtle.Screen()
# t.shape("circle")
# t.hideturtle()
# t.penup()
# t.speed(0)
# a = 3
# t.shapesize(a)
# cord_list = []
# size_list = []
# stamp_list = []
# x_list = []
# y_list = []
# def cl_t1(x,y):
#     t.setposition(x,y)
#     x_list.append(x)
#     y_list.append(y)
#     t_stamp = t.stamp()
#     stamp_list.append(t_stamp)
#     d = t.shapesize()
#     size_list.append(d[0])
# def cl_t2(x,y):
#     t.setposition(x,y)
#     for i in range(len(stamp_list)):
#         if x_list[i]-stamp_list[i]*5 <= t.xcor() <= x_list[i]+stamp_list[i]*5 and y_list[i]-stamp_list[i]*5 <= t.ycor() <= y_list[i]+stamp_list[i]*5:
#             t.clearstamp(stamp_list[i])
#
# def size_up():
#     global a
#     t.shapesize(a+1)
#     a += 1
# def size_down():
#     global a
#     t.shapesize(a-1)
#     a-=1
# def color_change():
#     color = random.randrange(1,11)
#     if color == 1:
#         t.color("#FF0000")
#     if color == 2:
#         t.color("#0000CC")
#     if color == 3:
#         t.color("#FFFF00")
#     if color == 4:
#         t.color("#00CC00")
#     if color == 5:
#         t.color("#00FFFF")
#     if color == 6:
#         t.color("#4C0099")
#     if color == 7:
#         t.color("#CC0000")
#     if color == 8:
#         t.color("#000066")
#     if color == 9:
#         t.color("#FF33FF")
#     if color == 10:
#         t.color("#000000")
#
# s.onclick(cl_t1)
# s.onclick(cl_t2, btn = 3)
# s.listen()
# s.onkeypress(size_up,"Up")
# s.onkeypress(size_down,"Down")
# s.onkeypress(color_change,"c")
# s.mainloop()

# 1번
# inp = input("5를 입력하시오")
# inp = int(inp)
# print(inp+5)

# 2번
# print("Hello\nKait")

# 3번
# lis = [10,20,30,40]
# su = 0
# for i in lis:
#     su += i
# print(su)

# 4번
# tu = (10.1,20.2,30.3,40.4)
# tu = tuple(map(int,tu))
# print(tu)

# 5번
# inp = int(input("10을 입력하세요 :"))
# hap = 0
# for i in range(inp+1):
#     hap += i
#
# print(hap)

# 6번
# def hap(x,y):
#     a = x+y
#     return a
# re = hap(10,20)
# print(re)

# 7번
# def fac(x):
#     if x == 1:
#         return 1
#     else:
#         return x * fac(x-1)
# inp = int(input("5를 입력"))
# re = fac(inp)
# print(re)

# 8번
# lis = [15,25,12,22,14]
#
# re = lis[0]
# for i in range(len(lis)):
#     if re > lis[i]:
#         re = lis[i]
# print(re)

# 9번
# lis = [20,10,30,50,40]
#
# for i in range(0,len(lis)-1):
#     for j in range(0,(len(lis)-1)-i):
#         if lis[j] < lis[j + 1]:
#             lis[j],lis[j+1] = lis[j+1],lis[j]
#
# print(lis)

# 10번
# lis = [10,20,30,25,15,27]
#
# print(max(lis)-min(lis))



# ****_***__**___*
# for i in range(0,4):
#         print("_"*i,end="")
#         print("*"*(4-i),end="")

# import random
#
# a = random.randint(1,100)
# ai_num = 50
# count = 0
# num_list = [50]
#
# def up():
#     global ai_num,a,count
#     while True:
#         ai_num = random.randint(ai_num,ai_num+5)
#         if num_list.count(ai_num) == 0:
#             num_list.append(ai_num)
#             break
#         if num_list.count(ai_num) != 0:
#             count -= 1
#             break
#
# def down():
#     global ai_num,a,count
#     while True:
#         ai_num = random.randint(ai_num-5,ai_num)
#         if num_list.count(ai_num) == 0:
#             num_list.append(ai_num)
#             break
#
#         if num_list.count(ai_num) != 0:
#             count -= 1
#             break
#
# while True:
#     if num_list[-1] < a:
#         count += 1
#         up()
#
#     if num_list[-1] > a:
#         count += 1
#         down()
#
#     if num_list[-1] == a:
#         count += 1
#         print(count,"번 만에 맞추셨습니다")
#         print(num_list)
#         break


# 임의의 숫자 6자리 생성

# 숫자를 맞추는 로직

# import random

# password = []
# result = []
# for i in range(6):
#     a = random.randint(0,9)
#     password.append(a)

# for i in range(0,6):
#     for j in range(0,10):
#         if j == password[i]:
#             result.append(j)

# print("비밀번호는",result[0],result[1],result[2],result[3],result[4],result[5],"입니다")