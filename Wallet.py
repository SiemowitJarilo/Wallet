from ast import Break, Continue, Return
from operator import truediv
import os, math, webbrowser
from tkinter.filedialog import SaveAs
from turtle import back, goto
import py_compile
from pickle import APPEND  









def pokaż_przychody(konto):
    print(przychody)

def dodaj_przychód(konto):
    print()
    przychód_wartość = int(input('Podaj kwotę:'))


    #przychód = (przychód_wartość, konto)
    #przychody.append(przychód)

def stanKonta(Konto):


def dodaj_rozchód(konto):
    print()
    rozchód_wartość = int(input('Podaj kwotę:'))

    rozchód = (rozchód_wartość, konto)
    

przychody = int
stanKonta = 0
stanTransakcji = '101 + PLN'
stanKrypto = '120 + pln'
opcje = ["konto", "giełda", "krypto"]
nameList = ['Konrad']
konto = 0



while True:
  print('Witaj, zaloguj się wprowadzając nazwę użytkownika, bądź wpisz Konto żeby założyć nowe konto')
  nameList = ['Konrad']
  login = input()
  if login in nameList:
    print('Witaj' + ' ' + login)
  if login not in nameList:
    print('Wpisz nową nazwę użytkownika')
    login = input('Wpisz nazwę użytkownika')
    nameList.append(login)
    print('Nowy użytkownik dodany')
  print('Zostałeś poprawnie zalogowany.' )   

  while True:
        print('0. Powrót do poprzedniego menu')
        print('1. Konto')
        print('2. Giełda')
        print('3. Krypto')
        choice = int(input('Wybierz opcję:'))
        
        while True:
          if choice == 0:
            break
          if choice == 1:
              print()
              print('0. Powrót do poprzedniego menu')
              print('1. Stan Konta')
              print('2. Dodaj przychód')
              choice = int(input('Wybierz opcję:'))

              if choice == 0:
                break
              if choice == 1:
                pokaż_przychody(konto)
              if choice == 2:
                dodaj_przychód(konto)    
        
          if choice == 2:
              print()
              print('0. Powrót do poprzedniego menu')
              print('1. Stan Konta')
              print('2. Dodaj transakcję')
              choice = int(input('Wybierz opcję:'))
              
              if choice == 0:
                break
              if choice == 1:
                print()
              if choice == 2:
                print()

          if choice == 3:
              print()
              print('0. Powrót do poprzedniego menu')
              print('1. Stan Konta')
              print('2. Dodaj transakcję')
              choice = int(input('Wybierz opcję:'))
              
              if choice == 0:
                break
              if choice == 1:
                print()
              if choice == 2:
                print()
