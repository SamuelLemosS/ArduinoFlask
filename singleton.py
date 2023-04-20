import pyfirmata

PORTA = 'COM5'

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
  
 def analogRead(self, pin):
  it = pyfirmata.util.Iterator(self.board)
  it.start()
  self.board.analog[pin].enable_reporting()
  valor = 'None'
  while valor =='None':
    valor = str(self.board.analog[pin].read())
  return float(valor)