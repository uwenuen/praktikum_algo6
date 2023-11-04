# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 19:23:01 2023

@author: Gwen
"""
def rata_rata():
    print("masukkan nilai A")
    a = float(input("Nilai= "))
    print("masukkan nilai C")
    c = float(input("Nilai= "))
    rerata= ( a + c )/2
    return rerata
    
hasil = rata_rata()
print("rata-ratanya= ", hasil)
