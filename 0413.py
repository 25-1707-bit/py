class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f"입금 완료 : {amount}")
    def withdraw(self,amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("잔액부족!")
    def status(self):
        print(f"계좌 주인 : {self.owner} / 잔액 : {self.balance}")

owner = BankAccount("aka",10000)
owner.deposit(1000)
owner.status()
owner.withdraw(10000)
owner.status()
owner.withdraw(100000)
owner.status()

class Movie:
    def __init__(self,title,total_seats,reserved_seats):
        self.title = title
        self.total_seats = total_seats
        self.reserved_seats = reserved_seats

    def reserve(self,seats):
        if self.total_seats > self.reserved_seats:
            self.reserved_seats += seats
        else:
            print("잔여 좌석 부족")
    def cancel(self,seats):
        self.reserved_seats -= 1
        if self.reserved_seats < 0:
            self.reserved_seats = 0
    def status(self):
        print(f"영화 제목 : {self.title} / 남은 좌석 : {self.total_seats-self.reserved_seats} / 예약된 자석 {self.reserved_seats}")

movie = Movie("승현이는 멍청이",100,10)
movie.reserve(10)
movie.cancel(1)
movie.status()