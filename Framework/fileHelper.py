# 전역변수 = 1

# def 함수() :
#     print(전역변수)

import pickle

# 파일 입출력 관련 및 폴더 관련 모음
class fileHelperInfo(object):
    # 클래스가 인스턴스(객체)화 될 때 한번만 실행되는 함수
    def __init__(self): # 생성자
        # self.전역변수 = 10 # 전역변수
        # 전역변수1 = 20 # 지역변수
        pass
    
    def fileOpen_ArrayList(self, filePath, openMode): # try except 해오기
        # self.전역변수 = 30 # 전역변수
        try:
            lstResult = []
            r = open(filePath, mode=openMode)
            for s in r:
                lstResult.append(s.replace("\n",""))
            r.close()
            return lstResult
        except Exception as ex:
            print(ex)
            
    # 직렬화로 파일저장
    # 모든 객체를 바이너리 코드로 직렬화(Serialization)
    def saveSerialization(self, saveData, sFilePath, saveMode):
        with open(sFilePath, saveMode) as f:
            pickle.dump(saveData, f)

    # 직렬화된 파일을 읽어서 반환하기
    # 파일을 읽어서 바로 반환을 한다.
    def readFileSerial(self, sFilePath, readMode):
        with open(sFilePath, readMode) as f :
            return pickle.load(f)  