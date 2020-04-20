import random

res = [] ##최고기록
name= [] ##랭킹 이름
maxres = 101
getmaxres = 101

def getscore():
    global maxres
    getmaxres=101
    f = open("C:\\Users\\proqk\\Documents\\school\\test.txt", 'r')
    line=f.readlines()

    for i in range(0, len(line)):
        score=line[i].split(':')
        name.append(score[0]) ##이름
        res.append(int(score[1])) ##점수

        if(getmaxres>int(score[1])): ##파일의 최고 기록을 저장함
            getmaxres = int(score[1])
    maxres=getmaxres
   
    f.close()

def putscore():
    f = open("C:\\Users\\proqk\\Documents\\school\\test.txt", 'w')
    for i in range(0, len(res)):
        f.write(name[i]+":"+str(res[i])+"\n")
    f.close()


getscore()
while True:
##    print(maxres)

    print("업다운게임 1.시작 2.기록확인 3.종료")
    what = int(input())

    if(what == 1):
        ans = random.randint(1,101) ##정답 뽑기
        l = 1 ##왼쪽값
        r=100 ##오른쪽값-수정1
        i=0	##n번째 도전
        print(ans)
        while True:
            i+=1
            if(i > 10):
                print("게임오버")
                break

            while True:
                print("%d번째 숫자 입력(%d~%d)" % (i,l,r))
                num = int(input(""))
                if(num>=l and num <= r): ##숫자가 범위 안에 있어야 통과
                    break
                else:
                    print("다시 입력")

            if(num < ans): ##입력값이 정답보다 작으면 크다고 해줌
                print("큼")
                l = num
            elif(num > ans):
                print("작음")
                r = num
            else: ##입력값이 정답이랑 같으면
                print("정답\n%d번만에 맞춤" % i)
                if(maxres > i): ##갱신이면 최고기록 갱신해줌
                    print("최고 기록 갱신")
                    tmpname = input("닉네임을 입력하세요: ")
                    name.insert(0, tmpname)
                    maxres = i
                    res.insert(0, i) ##최고기록일 때 추가-수정2                
                break
    elif(what == 2):
        ##res.sort() ##점수 정렬1

        print("rank/name/score")
        for i in range(len(res)):
            print("%d. %s %d" % (i+1,name[i],res[i]))
    else:
        putscore()
        break
