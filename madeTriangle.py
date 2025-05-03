'''
repeatNum = int(input(">> "))
n1 = 0


if 5번 반복시 > 총 9개의 칸 생성 필요
1 > 3 > 5 > 7 > 9

- - - 0 0 0 - - -

일반화 - n번 반복시 2n-1


wholeBlank = repeatNum * 2 - 1

for i in range(repeatNum) :
    n1 += 1
    #print(wholeBlank)
    # 공백그리기
    #print((wholeBlank-n1)/2)
    print("   "*int((wholeBlank-(n1*2-1))/2), end="")
    # 줄 그리기
    print(" 0 "*(n1*2-1), end="")
    # 공백그리기
    print("   "*int((wholeBlank-(n1*2-1))/2), end="")
    # 줄 옮기기
    print()


'''
repeatNum = int(input(">> "))
wholeBlank = repeatNum * 2 - 1

'''
-i+4번 동안 공백 만들기
'''

pascalList = [1]
pibonaciNum = 1

# 피보나치 수열 구하기
for j in range(repeatNum) :
    pascalList.append(pibonaciNum)
    pibonaciNum = pascalList[j] + pascalList[j+1]

print(pascalList)


