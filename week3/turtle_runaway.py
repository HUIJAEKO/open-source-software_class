import turtle
import random
import time

class RunawayGame:
    def __init__(self, canvas, runner, num_balls=10, ball_size=20, catch_radius=50):
        self.canvas = canvas
        self.runner = runner
        self.catch_radius2 = catch_radius ** 2  
        
        self.step = 20  # 거북이 이동 거리
        self.score = 0  # 점수
        self.timer = 0  # 타이머
        self.round_num = 1  # 라운드
        self.speed_multiplier = 1.0  # 공의 속도 배수

        # 이미지 등록
        canvas.addshape("week3/images/ghost.gif") 
        canvas.addshape("week3/images/ahhhhh-dwight.gif")

        # 공 생성
        self.ball_list = [self.make_ball(ball_size, self.speed_multiplier) for _ in range(num_balls)]
        
        self.drawer = turtle.RawTurtle(canvas)
        self.drawer.hideturtle()
        self.drawer.penup()

        self.runner.shape('week3/images/ahhhhh-dwight.gif')  
        self.runner.color('black')
        self.runner.penup()

        # 키보드 제어
        self.canvas.onkey(self.key_left, "Left")
        self.canvas.onkey(self.key_right, "Right")
        self.canvas.onkey(self.key_up, "Up")
        self.canvas.onkey(self.key_down, "Down")
        self.canvas.listen()

    def distance(self, x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    # 공에 해당하는 거북이 객체 생성
    def make_ball(self, size, speed_multiplier):
        ball = turtle.Turtle()  
        ball.shape("week3/images/ghost.gif")  
        ball.penup()
        ball.speed(0)
        ball.goto(random.randint(-200, 200), random.randint(-200, 200))  
        ball.dx = random.choice([-1, 1]) * speed_multiplier
        ball.dy = random.choice([-1, 1]) * speed_multiplier
        return ball

    def key_left(self):
        self.runner.seth(180)
        self.runner.fd(self.step)
        if self.runner.xcor() < -300:
            self.runner.setx(-300)

    def key_right(self):
        self.runner.seth(0)
        self.runner.fd(self.step)
        if self.runner.xcor() > 300:
            self.runner.setx(300)

    def key_up(self):
        self.runner.seth(90)
        self.runner.fd(self.step)
        if self.runner.ycor() > 300:
            self.runner.sety(300)

    def key_down(self):
        self.runner.seth(270)
        self.runner.fd(self.step)
        if self.runner.ycor() < -300:
            self.runner.sety(-300)

    def animate_ball(self):
        turtle.tracer(False)
        game = True
        start_time = time.time()
        last_round_time = start_time

        while game:
            self.drawer.clear()

            # 1초마다 타이머 증가
            elapsed_time = time.time() - start_time
            if elapsed_time >= 1:
                self.timer += 1
                start_time = time.time()

            # 10초마다 라운드 증가 및 속도 배수 변경
            if time.time() - last_round_time >= 10:
                self.speed_multiplier *= 1.3
                self.round_num += 1
                last_round_time = time.time()
                for ball in self.ball_list:
                    ball.dx *= self.speed_multiplier
                    ball.dy *= self.speed_multiplier

            # 공의 이동 및 충돌 처리
            for ball in self.ball_list:
                ball.setx(ball.xcor() + ball.dx)
                ball.sety(ball.ycor() + ball.dy)

                # 거북이와 공의 충돌 -> 게임 종료
                if self.distance(self.runner.xcor(), self.runner.ycor(), ball.xcor(), ball.ycor()) <= 15:
                    self.drawer.setpos(0, 0)
                    self.drawer.write(f"GAME OVER, Your score is {int(self.score)}", align="center", font=("Arial", 36, "bold"))
                    turtle.update()
                    game = False
                    return

                # 공이 화면을 벗어나면 방향 전환
                if ball.xcor() < -300 or ball.xcor() > 300:
                    ball.dx *= -1
                if ball.ycor() < -300 or ball.ycor() > 300:
                    ball.dy *= -1

            # 스코어 업데이트
            self.score += 3 / turtle.getcanvas().winfo_fpixels('1i')
            self.drawer.setpos(-300, 320)
            self.drawer.write(f"Score: {int(self.score)}", align="left", font=("Arial", 16, "normal"))

            # 타이머 업데이트
            self.drawer.setpos(-300, 290)
            self.drawer.write(f"Time: {self.timer}", align="left", font=("Arial", 16, "normal"))

            # 라운드 업데이트
            self.drawer.setpos(-300, 260)
            self.drawer.write(f"Round: {self.round_num}", align="left", font=("Arial", 16, "normal"))

            turtle.update()  

    def start(self):
        self.runner.setpos((-200, 0))
        self.animate_ball()

# 게임 실행 함수
if __name__ == "__main__":
    root = turtle.Screen()
    root.setup(700, 700)
    root.bgcolor("lightgreen")
    root.title("Turtle Runaway")

    runner = turtle.Turtle()
    game = RunawayGame(root, runner) 
    game.start()

    turtle.mainloop()
