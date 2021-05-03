import random

print("갤러그 게임 시작")
score=0

while score >= 0:
    print("적 비행기 발생")
    enemymove = ["전진", "정면 공격중", "우측 공격중", "좌측 공격중"]
    enemy=random.choice(enemymove)
    #적 움직움 중 랜덤으로 1개 출력하는 코드
    print(enemy)
    print("1. 발사 2. 오른쪽 이동 3. 왼쪽이동")
    number = input("당신의 입력값 : ")
    # 적이 전진 중 일때 공격시
    if enemy=="전진" and number == "1":
        print("격파 했습니다.")
        score += 1
        print("스코어: ",score)
    # 적이 전진 중 일때 회피시
    if enemy == "전진" and number == "2":
        print("회피 하였습니다.")
        print("스코어: ",score)
    if enemy == "전진" and number == "3":
        print("회피 하였습니다.")
        print("스코어: ",score)

    #적이 정면 공격중일때 공격시
    if enemy == "정면 공격중" and number == "1":
        print("받은 데미지 1")
        score -= 1
        print("스코어: ",score)
    #적이 정면 공격중일때 회피시
    if enemy == "정면 공격중" and number == "2":
        print("회피 하였습니다.")
        print("스코어: ",score)
    if enemy == "정면 공격중" and number == "3":
        print("회피 하였습니다.")
        print("스코어: ",score)

    #적이 우측 공격중일때 공격시
    if enemy == "우측 공격중" and number == "1":
        print("적이 지나쳐 갔습니다.")
        print("스코어: ",score)
    #적이 우측 공격중일때 회피시
    if enemy == "우측 공격중" and number == "3":
        print("회피 하였습니다.")
        print("스코어: ",score)
    #적이 우측 공격중일때 피해받을시
    if enemy == "우측 공격중" and number == "2":
        print("받은 데미지 1")
        score -= 1
        print("스코어: ",score)

    #적이 좌측 공격중일때 공격시
    if enemy == "좌측 공격중" and number == "1":
        print("적이 지나쳐 갔습니다.")
        print("스코어: ",score)
    #적이 좌측 공격중일때 회피시
    if enemy == "좌측 공격중" and number == "2":
        print("회피 하였습니다.")
        print("스코어: ",score)
    #적이 좌측 공격중일때 피해받을시
    if enemy == "좌측 공격중" and number == "3":
        print("받은 데미지 1")
        score -= 1
        print("스코어: ",score)

    print("")

    #while문 끝내는 문
    if score < 0:
        break