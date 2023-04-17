import pyfirmata

PORTA = 'COM10'

def singleton(cls):
 instances = {}
 def getinstance():
  if cls not in instances:
   instances[cls] = cls()
  return instances[cls]
 return getinstance

@singleton 
class Arduino(object):
 def __init__(self, port=None):
 #def __init__(self, port=None):
  self.board = pyfirmata.Arduino(PORTA)

 def digitalWrite(self, pin, value):
  self.board.digital[pin].mode = pyfirmata.OUTPUT
  self.board.digital[pin].write(value)