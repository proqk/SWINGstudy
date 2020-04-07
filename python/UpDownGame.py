import random

res = []
maxres = 0

while True:
    print("업다운게임 1.시작 2.기록확인 3.종료")
    what = int(input())

    if(what == 1):
        ans = random.randint(1,101) ##정답 뽑기
        l = 1 ##왼쪽값
        r=1000 ##오른쪽값
        i=0	##n번째 도전
        ##print(ans)
        while True:
            i+=1
            if(i > 10):
                print("게임오버")
                break

            print("%d번째 숫자 입력(%d~%d)" % (i,l,r))
            num = int(input(""))
            if(num < ans): ##입력값이 정답보다 작으면 크다고 해줌
                print("큼")
                l = num
            elif(num > ans):
                print("작음")
                r = num
            else:
                print("정답\n%d번만에 맞춤" % i)
                if(maxres < i): ##갱신이면 최고기록 갱신해줌
                    print("최고 기록 갱신")
                    maxres = i
                res.append(i) ##갱신이든 아니든 점수는 기록
                break
    elif(what == 2):
        res.sort() ##점수 정렬
        for i in range(len(res)):
            print("%d. %d" % (i+1,res[i]))
    else:
        break
