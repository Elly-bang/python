'''
중쳡함수 -> 클래스(data+ fuction)

'''
class Account:
  balance=0

  def __init__ (self, bal, name, no):
      self.balance = bal
      self.accName = name
      self.accNo = no

  def getBalance(self):
      return self.balance, self.accName, self.accNo

  def deposit(self, money):
      if money < 0:
          print("금액을 확인하세요")
      else:
          self.balance += money

  def withdraw(self, money):
      if self.balance < money:
          print("잔액이 부족합니다.")
      else:
          self.balance -= money

acc = Account(1000, '홍길동', '012-125-41520')
bal, name, no = acc.getBalance()
print('잔액 : {}, 예금주 : {}, 계좌번호 : {}'.format(bal, name, no)) # getter : 잔액 : 1000

acc.deposit(20000) # 2만원 입금
bal, name, no = acc.getBalance()
print('잔액 : {}, 예금주 : {}, 계좌번호 : {}'.format(bal, name, no)) # getter : 잔액 : 1000

acc.withdraw(5000) # 5천원 인출
bal, name, no = acc.getBalance()
print('잔액 : {}, 예금주 : {}, 계좌번호 : {}'.format(bal, name, no)) # getter : 잔액 : 1000





