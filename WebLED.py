from singleton import Arduino
from flask import Flask, render_template
import pyfirmata

LED = 13
BOTAO = 12
estado = {'led': True}
qntclik = 0

#board = pyfirmata.Arduino('COM4')
app = Flask(__name__, template_folder='template')

@app.route('/')
def inicio():
    return mostra_estado()

@app.route('/led/1')
def ligar_led():
    arduino = Arduino()
    arduino.digitalWrite(LED, 1)
    #board.digital[LED].write(1)
    estado['led'] = True
    return mostra_estado()

@app.route('/led/0')
def desl_led():
    arduino = Arduino()
    arduino.digitalWrite(LED, 0)
    #board.digital[LED].write(0)
    estado['led'] = False
    return mostra_estado()

def mostra_estado():
    global qntclik
    arduino = Arduino()
    click = arduino.digitalRead(BOTAO)
    #click = board.digital[BOTAO].read()
    #click='teste'
    if click==True:
       qntclik = qntclik + 1
    return render_template('teste.html', **estado, click=click)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)