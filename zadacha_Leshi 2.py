import sqlite3

class Account: #https://peps.python.org/pep-0008/#class-names #https://dvmn.org/encyclopedia/qna/13/chto-takoe-docstring-s-chem-ego-edjat/
    def __init__(self, user_id, email, password):
        self.user_id = user_id
        self.email = email
        self.password = password
        self.balance = 0


connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

def create_bd():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            balance REAL DEFAULT 0
        )
    ''')
    connection.commit()
    connection.close()

def insert_accounts(users):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()

    for user in users:
        cursor.execute('''
            INSERT OR REPLACE INTO users (user_id, email, password, balance) 
            VALUES (?, ?, ?, ?)
        ''', (user.us_id, user.email, user.password, user.balance))

    connection.commit()
    connection.close()

create_bd()
users = [
    Account(1, 'user1@mail.ru', 'password1'),
    Account(2, 'user2@mail.ru', 'password2'),
    Account(3, 'user3@mail.ru', 'password3')
]
insert_accounts(users)
    

def login(email, password): 
    for user in users:
        if user.email == email and user.password == password:
            return user
    return None

def main():
    email = input("Введите email: ")
    password = input("Введите пароль: ")
    
    user = login(email, password)
    if not user:
        print("Неверные учетные данные")
        return

    while True:
        act = input("Выберите действие: 'посмотреть баланс', 'положить деньги', 'снять деньги', 'выход': ")
        
        if act.lower() == 'посмотреть баланс': 
            print(f"Ваш баланс: {round(user.balance, 3)}")
        elif act == 'положить деньги':
            sum_b = float(input("Введите сумму для пополнения: ")) 
            user.balance += sum_b
            print(f"Деньги были положены. Текущий баланс: {round(user.balance, 3)}")
        elif act == 'снять деньги':
            sum_b = float(input("Введите сумму для снятия: ")) 
            if sum_b <= user.balance:
                user.balance -= sum_b
                print(f"Сумма снята. Текущий баланс: {round(user.balance, 3)}")
            else:
                print("Недостаточно средств")
        elif act == 'выход':
            print("Выход из системы")
            break

if __name__ == "__main__":
    main()


