logins = {
    'Erik': '1234erik',
    'Anton': '44ff2#z//'
}
def NewLogin():
    new_login = input('Дайте новий логін -> ')
    new_password = input(f'Дайтe новий пароль до цього логіну {new_login} -> ')

    logins[new_login] = new_password



def Deletelogin():
    delete_login = input('Напишіть логін, який хочете видалити -> ')
    delete_password = input('Введіть пароль, щоб удостовіритися, що цей логін належить Вам -> ')
    x=0
    for i in logins.keys():
        if i == delete_login:
            x+=1
    if x > 0:
          if logins[delete_login] == delete_password: 
              del logins[delete_login]
          else:
              print('Пароль не вірний!')
    else:
        print('Такого логіну не знайдено!')



def Print_Logins():
    for i, j in logins.items():
        print(f"\nЛогін - {i}\nПароль - {j}\n")

def Update_Passwords():
    x=0
    check_login = input('Введіть логін який хочете змінити -> ')
    for i in logins.keys():
        if i == check_login:
            x+=1
    if x > 0:
        check_password = input("Введіть старий пароль -> ")
        if logins[check_login] == check_password:
            new_password = input('Введіть новий пароль -> ')
            logins[check_login] = new_password
        else:
            print('Пароль не вірний!')
    else:
        print('Такого логіну не існує!')
    
    
def main():
    while True:
        print("Створити юзера - *1*\nВидалити юзера - *2*\nВивести список усіх юзерів та паролів - *3*\nЗмінити пароль - *4*\nЗавершити програму - *0*")
        check = int(input("Введіть число: "))
        if check == 1:
            NewLogin()
        elif check == 2:
            Deletelogin()
        elif check == 3:
            Print_Logins()
        elif check == 4:
            Update_Passwords()
        elif check == 0:
            break
        else:
            print("Помилка... Спробуйте знову!")
main()
