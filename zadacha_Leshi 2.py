import sqlite3

def create_bd():
    connection = sqlite3.connect('accounts.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT,
            balance REAL DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()


def add_account(username, password, balance):
    conn = sqlite3.connect('accounts.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO accounts (username, password, balance) VALUES (?, ?, ?)', (username, password, balance))
    conn.commit()
    conn.close()

def auth(username, password):
    conn = sqlite3.connect('accounts.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM accounts WHERE username = ? AND password = ?', (username, password))
    account = cursor.fetchone()
    conn.close()
    return account

def update_balance(username, amount):
    conn = sqlite3.connect('accounts.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE accounts SET balance = balance + ? WHERE username = ?', (amount, username))
    conn.commit()
    conn.close()

def check_balance(username):
    conn = sqlite3.connect('accounts.db')
    cursor = conn.cursor()
    cursor.execute('SELECT balance FROM accounts WHERE username = ?', (username,))
    balance = cursor.fetchone()
    conn.close()
    return balance[0] if balance else None

create_database()

add_account('user1', 'password1', 0.0)
add_account('user2', 'password2', 0.0)
add_account('user3', 'password3', 0.0)


username = input("Введите логин: ")
password = input("Введите пароль: ")

user = auth(username, password)
if user:
    print("Вход выполнен успешно!")
    while True:
        act = input("Выберите действие: 'посмотреть баланс', 'положить деньги', 'снять деньги', 'выход': ")
        if act.lower() == "выход":
            break
        elif act.lower() == "положить деньги":
            amount = float(input("Введите сумму: "))
            update_balance(username, amount)
            balance = check_balance(username)
            print(f'Деньги были положены. Текущий баланс: {round(balance, 3)}')
        elif act.lower() == "снять деньги":
            amount = float(input("Введите сумму: "))
            update_balance(username, -amount)
            balance = check_balance(username)
            print(f'Сумма снята. Текущий баланс: {round(balance, 3)}')
        elif act.lower() == "посмотреть баланс":
            balance = check_balance(username)
            print(f"Текущий баланс: {round(balance, 3)}")
else:
    print("Неверный логин или пароль.")

   
         

