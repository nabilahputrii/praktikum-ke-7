# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 13:18:40 2021

@judul : Praktikum ke-7 latihan ke-1
@NIM : 065002100002
@author: Nabilah Putri


"""

def kateg(n="0",total=0,menampung=0 ):
    while (n != "") :
        n = str(input("silahkan masukkan nilai :"))
        menampung = menampung + 1
        if (n == ''):
            return total/(menampung -1)
        elif (n== 'A'):
            print ("nilai = 4.00")
            total += 4.00
        elif (n == 'A-'):
            print ("nilai = 3.75")
            total += 3.75
        elif (n== 'B+'):
            print ("nilai = 3.50")
            total += 3.50
        elif (n == 'B'):
            print ("nilai = 3.00")
            total += 3.00
        elif (n== 'B-'):
            print ("nilai = 2.75")
            total += 2.75
        elif (n== "D"):
            print('nilai=1.5')
            total += 1.75
        else :
            print ("silahkan masukan nilai valid ya")
            
rata_rata = kateg ()
print("rata-ratanya adalah",rata_rata)