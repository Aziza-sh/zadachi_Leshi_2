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


