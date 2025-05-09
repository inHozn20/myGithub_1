import random
import pymysql



#DB 개인정보
conn = pymysql.connect(
	host = 'localhost',
	port = 3306,
	user = 'root',
	password= '0746',
	db = 'lgh',
	charset= 'utf8'
)

curs = conn.cursor()


#sql = "SELECT seq, word FROM wordlist"
#curs.execute(sql)
#result = curs.fetchall()
#print("테이블 내 데이터 = {0}".format(result))

# 원하는 칼럼만 선택해서 쿼리 실행
curs.execute("SELECT word FROM wordlist")

# 결과를 모두 가져옴
rows = curs.fetchall()

# 튜플에서 값만 꺼내서 리스트로 저장
word_list = [row[0] for row in rows] #데이터를 받아오는 리스트
print(word_list)


words = []


word_list2 = ["javascript"] # 원하는 단어 입력
QList = []
exStr = ""
presentScore = 0
goalScore = 0
lifeStage = 0
usedL = []

def choseWord() :
	global QList
	global words
	wordSeq = random.randint(0, len(words))
	
	for s in words[wordSeq] :
		QList.append(s) 
		
	return wordSeq
	
def strChange(strQ, seq, strT) :
	listStr = []
	answerStr = ""
	for w in strQ :
		listStr.append(w)
	listStr[seq] = strT #오류 발생
	for t in listStr :
		answerStr += t
	return answerStr
	
	
def findAnswer(wordQ) :
	global lifeStage
	
	seq = 0
	delSeq= ""
	
	while True :
		strAnswer = str(input(">> "))
		if strAnswer in usedL :
			print("이미 입력한 글자입니다.")
			continue
		elif not strAnswer in "abcdefghijklmnopqrstuvxwyz" :
			print("적절하지 않은 입력값입니다.")
			continue
		else :
			for s in QList :
				if s == strAnswer :
					delSeq += str(seq)
				seq += 1
			if delSeq == "" :
				lifeStage += 1
			usedL.append(strAnswer)
			break
	return delSeq #str


#실작동부	

print("<HangMan Game>")

while True :

	choiceMode = input("게임플레이(1)/단어추가(2) 중 선택해주세요. >> ")
	if int(choiceMode) == 1 :
		words = word_list
		wordG = words[choseWord()]
		break

	elif int(choiceMode) == 2 :
		#DB에 단어 추가
		insertWords = []
		insertString = ""

		while True :
			insertWords.append(input("추가하고 싶은 단어를 입력해주세요.(단어 입력을 멈추고 싶다면 @를 입력하세요.) >> "))
			#단어효용성검사 필요
			if insertWords[len(insertWords)-1] == "@" :
				break
		
		# 입력쿼리 만들기
		insertQuery = "INSERT INTO wordlist VALUES "
		for j in range(len(insertWords)-1) :
			print(insertWords[j])
			insertQuery += "({0}, '{1}')".format(len(word_list)+j+1, insertWords[j])

		# 쿼리 execute
		print(insertQuery)
		curs.execute(insertQuery)

		# 쿼리 작동확인 및 리스트 다시 업뎃
		curs.execute("SELECT word FROM wordlist")
		rows = curs.fetchall()
		word_list = [row[0] for row in rows] #데이터를 받아오는 리스트
		print(word_list)
		
		print("단어추가 완료")
		continue
	else :
		print("잘못된 입력값입니다.")
		continue

# DB 연결 최종종료
curs.close()
conn.close()

"""
while True :

	choiceWord = input("개인단어(1)/내장단어(2) 중 선택해주세요. >> ")
	if int(choiceWord) == 2 :
		words = word_list
		wordG = words[choseWord()] 
		break
	elif int(choiceWord) == 1 :
		words = word_list2
		wordG = word_list[choseWord()]
		break
	else :
		print("잘못된 입력값입니다.")
		continue
"""

goalScore = len(wordG)

exStr = "x"*len(wordG)

def Screen(wordQ, delStr) : #wordQ - apple

	global exStr
	global presentScore

	seq = 0
	print()
	print("□"*25)
	print()
	if delStr != None : #12
		# 정답 제외
		for j in delStr :
			exStr = strChange(exStr,int(j), "o")
			presentScore += 1
	# 화면
	for s in wordQ :
		seq += 1 
		if exStr[seq-1] == "o" :
			print(QList[seq-1]+" ", end="")
		elif exStr[seq-1] == "x" :
			print("_ ", end="")
	print()
	print()
	print(PIC[lifeStage])
	print()
	print("□"*25)
	print()

	
PIC = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


#첫 화면 구성
Screen(wordG, None)

while True : #작동반복
	if int(presentScore) != int(goalScore) :
		if lifeStage == 6 :
			seq = 0
			print()
			print("□"*25)
			print()
			for s in wordG :
				seq += 1 
				print(QList[seq-1]+" ", end="")
			print()
			print()
			print(PIC[lifeStage])
			print()
			print("□"*25)
			print()
			print("실패")
			break
		# 인풋 물어보는 동시에 스크린 구성
		else :
			Screen(wordG, findAnswer(wordG))
	else :
		print()
		print("정답")
		break
		
	
