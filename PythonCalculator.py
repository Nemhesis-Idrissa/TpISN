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
    global current_value, current_value_init, current_value_decimal 
    current_value = 0
    current_value_init = True
    current_value_decimal = 0
    
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
        print("Vous avez appuyé sur AC")
   
    def key_digit(n):
        def real_key_digit():
            global current_value, current_value_init, current_value_decimal 
            print("Vous avez appuyer sur",n , "alors que", current_value)
            if current_value_init: 
                current_value = n 
            else: 
                current_value = current_value * 10 + n 
                current_value_init = False
                print("ecran", current_value)
        return real_key_digit
            
    
    create_button( 0, 0, "AC",on_va_voir)
    create_button( 0, 1, "7", key_digit (7))
    create_button( 0, 2, "4", key_digit(4))
    create_button( 0, 3, "1", key_digit(1))
    create_button( 0, 4, "0", key_digit(0))
    
    create_button( 1, 0, "C", on_va_voir)
    create_button( 1, 1, "8", key_digit(8))
    create_button( 1, 2, "5", key_digit(5))
    create_button( 1, 3, "2", key_digit(2))
    create_button( 1, 4, ".", on_va_voir)

    create_button( 2, 0, "r", on_va_voir)
    create_button( 2, 1, "9", key_digit(9))
    create_button( 2, 2, "6", key_digit(6))
    create_button( 2 ,3, "3", key_digit(3))
    create_button( 2, 4, ",", on_va_voir)
    
    create_button( 3, 0, "=", on_va_voir)
    create_button( 3, 1, "/", on_va_voir)
    create_button( 3, 2, "*", on_va_voir)
    create_button( 3, 3, "-", on_va_voir)
    create_button( 3, 4, "+", on_va_voir)
   


  


    window.show()
    sys.exit(app.exec_())

main()
