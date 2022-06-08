# 구구단
g = 0
while g == 0:
    a = int(input("몇 단을 계산할까요? (0 : 종료) "))
    x = [1,2,3,4,5,6,7,8,9]
    print("="*20)
    if a == 0:
        print("이용해 주셔서 감사합니다.")
        print()
        break
    else:
        print("{}단은 바로..".format(a))
        for i in range(len(x)):
            b = a*x[i]
            print("{} x {} = {}".format(a,x[i],b))
        print("="*20)


#숫자 맞추기 게임
game = int(input("게임을 몇 번 진행할까요? (0 : 종료)"))
import random
win = 0
lose = 0
m = 0
while m < game:
    if game == 0:
        break
    com = random.randint(1,99)
    print("{}번째 게임을 시작합니다.".format(m+1))
    i = 0
    while i < 5:
        user = int(input("당신의 숫자는?"))
        if user-com > 10:
            print("정답보다 매우 큼")
            print()
            i += 1
        elif user-com > 0.1:
            print("정답보다 큼")
            print()
            i += 1
        elif com-user > 10:
            print("정답보다 매우 작음")
            print()
            i += 1
        elif com-user > 0.1:
            print("정답보다 작음")
            print()
            i += 1
        elif com == user:
            print("정답!")
            win += 1
            print("정답 누적횟수 : {}".format(win))
            print()
            m += 1
            i += (5-i)
            continue
        if i == 5:
            print("실패")
            print("숫자는 {}였습니다.".format(com))
            lose += 1
            m += 1
if win > 0:
    print("{}번 게임해서 {}번 성공하고 {}번 실패했습니다!".format(game,win,lose))
    if win>lose and lose>0:
        print("당신의 승리!")
    elif lose ==0:
        print("당신의 완승!")
    elif win == lose:
        print("무승부")
    else:
        print("컴퓨터 승리!")
elif win == 0 and game>0:
    print("{}번 시도하여 한 번도 성공하지 못했습니다.".format(game))
    print("컴퓨터 완승!")
print("이용해 주셔서 감사합니다.")
print()


#리스트 연습
to_do_list = []
y = 1
h = 0
print()
print("To do List")
while y == 1:
    what = int(input("추가?제거? (1/2/3) / (3 : 종료)"))
    if what == 1:
        a = input("할 일?")
        h += 1
        to_do_list.append(a)
        print("남은 할 일 : {}\n{}개의 할 일이 남았습니다.".format(to_do_list,h))
    elif what == 2:
        print(to_do_list)
        h -= 1
        b = int(input("몇 번째 할 일을 끝냈나요?"))
        del to_do_list[b-1]
        print("남은 할 일 : {}\n{}개의 할 일이 남았습니다.".format(to_do_list,h))
    else:
        print("휴식!")
        break
