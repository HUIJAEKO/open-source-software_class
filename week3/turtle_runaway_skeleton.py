import tkinter as tk
import turtle
import random
import time

# 거리 계산 함수
def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# 공(장애물) 생성 함수
def make_ball(size, speed_multiplier):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    color = random.choice(["red", "green", "blue", "yellow", "pink", "purple"])
    while True:
        dx = random.choice([-1, 1]) * speed_multiplier
        dy = random.choice([-1, 1]) * speed_multiplier
        if dx != 0 or dy != 0:
            break
    return [x, y, size, color, dx, dy]

# 공 애니메이션 함수
def animate_ball(pen, ball_list, runner, speed_multiplier):
    global score
    turtle.tracer(False)
    game = True
    start_time = time.time()
    timer = 0
    round_num = 1  # Round starts at 1
    last_round_time = start_time

    while game:
        turtle.listen()
        pen.clear()  # 공을 지움

        # 1초마다 타이머 증가
        elapsed_time = time.time() - start_time
        if elapsed_time >= 1:
            timer += 1
            start_time = time.time()

        # 10초가 지났고 마지막 라운드 증가 시간에서 10초가 지났는지 체크
        if time.time() - last_round_time >= 10:
            speed_multiplier *= 1.5
            round_num += 1  # Round number increases every 10 seconds
            last_round_time = time.time()  # 라운드 증가 시간을 갱신
            # 공의 속도 재조정
            for i in range(len(ball_list)):
                dx, dy = ball_list[i][4], ball_list[i][5]
                ball_list[i][4] = (dx / abs(dx)) * speed_multiplier if dx != 0 else random.choice([-1, 1]) * speed_multiplier
                ball_list[i][5] = (dy / abs(dy)) * speed_multiplier if dy != 0 else random.choice([-1, 1]) * speed_multiplier

        # 공의 이동
        for i in range(len(ball_list)):
            ball_x, ball_y, size, color, dx, dy = ball_list[i]
            ball_x += dx
            ball_y += dy
            ball_list[i][0] = ball_x
            ball_list[i][1] = ball_y

            # 거북이와 공의 충돌 -> 즉시 게임 종료
            if distance(runner.xcor(), runner.ycor(), ball_x, ball_y) <= 15:
                print("Game Over! Turtle collided with the ball.")
                pen.setpos(0, 0)
                pen.write(f"GAME OVER, Your score is {int(score)}", align="center", font=("Arial", 36, "bold"))
                turtle.update()
                game = False
                return

            # 공이 화면을 벗어나면 방향 전환
            if ball_x < -300 or ball_x > 300:
                ball_list[i][4] *= -1
            if ball_y < -300 or ball_y > 300:
                ball_list[i][5] *= -1

            # 공과 공의 충돌 처리
            for j in range(len(ball_list)):
                if i != j:
                    ball2_x = ball_list[j][0]
                    ball2_y = ball_list[j][1]
                    if distance(ball_x, ball_y, ball2_x, ball2_y) <= size:
                        ball_list[i][4] *= -1
                        ball_list[i][5] *= -1
                        ball_list[j][4] *= -1
                        ball_list[j][5] *= -1
                        ball_list[i][0] += ball_list[i][4] * 2
                        ball_list[i][1] += ball_list[i][5] * 2
                        ball_list[j][0] += ball_list[j][4] * 2
                        ball_list[j][1] += ball_list[j][5] * 2

            pen.setpos(ball_x, ball_y)
            pen.dot(size, color)

        # 스코어 업데이트
        score += 3 / turtle.getcanvas().winfo_fpixels('1i')
        pen.setpos(-300, 320)
        pen.write(f"Score: {int(score)}", align="left", font=("Arial", 16, "normal"))

        # 타이머 업데이트
        pen.setpos(-300, 290)
        pen.write(f"Time: {timer}", align="left", font=("Arial", 16, "normal"))

        # 라운드 업데이트
        pen.setpos(-300, 260)
        pen.write(f"Round: {round_num}", align="left", font=("Arial", 16, "normal"))

        turtle.update()  # 스크린 갱신

# 키보드 제어 이벤트 함수들
def key_left():
    runner.seth(180)
    runner.fd(step)
    if runner.xcor() < -300:
        runner.setx(-300)

def key_right():
    runner.seth(0)
    runner.fd(step)
    if runner.xcor() > 300:
        runner.setx(300)

def key_up():
    runner.seth(90)
    runner.fd(step)
    if runner.ycor() > 300:
        runner.sety(300)

def key_down():
    runner.seth(270)
    runner.fd(step)
    if runner.ycor() < -300:
        runner.sety(-300)

# 게임 실행 함수
def start_game():
    global runner, goal, step, score

    # 창 설정
    turtle.setup(700, 700)
    turtle.bgcolor("lightgreen")
    turtle.title("Turtle Runaway Game")

    goal = 250
    step = 20
    score = 0

    # 도착 지점 그리기
    runner = turtle.Turtle()
    runner.shape("turtle")
    runner.penup()
    runner.setpos(-goal, goal)

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()

    # 키보드 이벤트 연결
    turtle.onkey(key_left, "Left")
    turtle.onkey(key_right, "Right")
    turtle.onkey(key_up, "Up")
    turtle.onkey(key_down, "Down")
    turtle.listen()

    # 공 생성 및 애니메이션 시작
    speed_multiplier = 1.0
    ball_list = [make_ball(20, speed_multiplier) for _ in range(10)]
    animate_ball(pen, ball_list, runner, speed_multiplier)

# 게임 시작
if __name__ == "__main__":
    start_game()
    turtle.mainloop()
