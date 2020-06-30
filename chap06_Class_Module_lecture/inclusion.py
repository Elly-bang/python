'''
1. private 변수 = 클래스 내의 은닉 변수
object.member 객체 -> 은닉 변수 (x)
getter()/setter() -> 은닉 변수 (0)

2. class 포함 관계 (inclusion)
-특정 객체가 다른 객체를 포함하는 클래스 설계 기법
-두 객체 간의 통신 지원
- class a <-> class b
'''

#1. private 변수
class Login :
    def __init__(self, uid, pwd):
        self.__dbId = uid
        self.__dbPwd = pwd

    def getIdPwd(self):
        return self.__dbId, self.__dbPwd

    def setIdPwd(self,uid, pwd):
        self.__dbId= uid
        self.__dbPwd = pwd

login = Login('hong','1234')
sad
uid, pwd = login.getIdPwd()
print(uid, pwd, sep=',')


def solution(a, b):
    for i in range(min(a, b), max(a, b) + 1):

    return answer



