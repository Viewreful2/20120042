row=5;
col=5;

BINGO_CHECK=[] # 0과 1로 이루어진 빙고 체크판
BINGO=[] # 많은 숫자로 이루어진 빙고판
T= int(input()) # 반복하는 수

for t in range(0,T): # 처음으로 불러진 숫자만큼 반복

    BINGO_CHECK=[] # 0과 1로 이루어진 빙고 체크판
    BINGO=[] # 많은 숫자로 이루어진 빙고판
    isFinished = False
    for i in range(0,5) : # i = 0 ~ 4
        row_number=input().split()
        row_number=[int(j) for j in row_number]
        BINGO.append(row_number)
        # 빙고 만들기 끝

    BINGO[2][2] = -1

    # 빙고 맞출 숫자를 입력받자!
    checknum=[]
    checknum=input().split()
    checknum = [int(j) for j in checknum]

    count=0     # 체크된 숫자의 갯수를 세줌
    count_of_input=0; # 빙고 할때 부르는 숫자의 순서

    for num in checknum :

        # 빙고판이랑 수랑 같은지 체크 하는 부분
        for x in range(0,5): #행
            for y in range(0,5): #열
                if (BINGO[x][y] == checknum[count_of_input]):
                     BINGO[x][y]=-1; #-1은 체크가 됫다는 뜻!
        count_of_input +=1;
        #--------------------------------------
        isFinished = False
        #첫번째 조건
        for x in range(0,5): #0번째 행부터 4번째 행까지 반복
            count1 = 0
            if isFinished == True:
                break
            for y in range(0,5):
                if (BINGO[x][y] == -1) : # 빙고판의 좌표가 (x,y)일때 -1이라면
                    count1=count1+1
            if(count1 == 5) :
                print(count_of_input)
                isFinished = True
                break
        #--------------------------------------
        #두번째 조건
        if isFinished == True:
            break
        for x in range(0,5):
            count1 = 0
            if isFinished == True:
                break;
            for y in range(0,5) :
                if (BINGO[y][x] == -1):
                    count1=count1+1
            if(count1 == 5):
                print(count_of_input)
                isFinished = True
                break
        #--------------------------------------
        #세번째 조건
        #3-1번
        if isFinished == True:
            break
        count1=0
        for x in range(0,5):
            if(BINGO[x][x] == -1):
                count1=count1+1
        if (count1 == 5):
            print(count_of_input)
            break
        #3-2번
        if isFinished == True:
            break
        count1=0
        for x in range(0,5):
            if(BINGO[x][4-x] == -1):
                count1=count1+1
        if (count1 == 5):
            print(count_of_input)
            break
        #--------------------------------------
        #네번째 조건
        if isFinished == True:
            break
        if(BINGO[0][0] + BINGO[0][4] + BINGO[4][0] + BINGO[4][4] == -4):
            print(count_of_input)
            break