# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import sys 
from PyQt5 import QtGui, QtWidgets

def on_va_voir():
    global click_count
    click_count = click_count + 1
    print("on a vu ",click_count, "fois ") 


def main():
    global click_count
    click_count = 0
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.resize(250,150 )
    window.setWindowTitle("Programme ")
 

    def create_button(x, y, t, cb): 
        
        button = QtWidgets.QPushButton(t, window)
        button.move(10 + x * 60, 60 + y * 50)
        button.resize(50, 40)
        button.clicked.connect(cb)
      
    def key_digit(): 
        print("Vous avez appuyé sur AC",)
   
    def real_key_digit(n):
        print("Vous avez appuyer sur",n)
        return real_key_digit
            
    
    create_button( 0, 0, "AC",key_digit )
    create_button( 0, 1, "7", on_va_voir)
    create_button( 0, 2, "4", on_va_voir)
    create_button( 0, 3, "1", on_va_voir)
    create_button( 0, 4, "0", on_va_voir)
    
    create_button( 1, 0, "C", on_va_voir)
    create_button( 1, 1, "8", on_va_voir)
    create_button( 1, 2, "5", on_va_voir)
    create_button( 1, 3, "2", on_va_voir)
    create_button( 1, 4, ".", on_va_voir)

    create_button( 2, 0, "r", on_va_voir)
    create_button( 2, 1, "9", on_va_voir)
    create_button( 2, 2, "6", on_va_voir)
    create_button( 2 ,3, "3", on_va_voir)
    create_button( 2, 4, ",", on_va_voir)
    
    create_button( 3, 0, "=", on_va_voir)
    create_button( 3, 1, "/", on_va_voir)
    create_button( 3, 2, "*", on_va_voir)
    create_button( 3, 3, "-", on_va_voir)
    create_button( 3, 4, "+", on_va_voir)
   


  


    window.show()
    sys.exit(app.exec_())

main()

