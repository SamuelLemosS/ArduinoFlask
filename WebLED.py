from singleton import Arduino
from flask import Flask, render_template
import pyfirmata

LED = 13
BOTAO = 0
estado = {'led': True}

#board = pyfirmata.Arduino('COM5')
app = Flask(__name__, template_folder='template')

@app.route('/')
def inicio():
    arduino = Arduino()
    click = arduino.analogRead(BOTAO)
    #click = board.digital[BOTAO].read()
    #click='teste'
    if click<= 5.0:
        qntclik="DESLIGADO"
        return render_template('teste.html', **estado, click=qntclik)
    else:
        qntclik="LIGADO"
        return render_template('teste.html', **estado, click=qntclik)
    

@app.route('/led/1')
def ligar_led():
    arduino = Arduino()
    arduino.digitalWrite(LED, 1)
    #board.digital[LED].write(1)
    estado['led'] = True
    return inicio()

@app.route('/led/0')
def desl_led():
    arduino = Arduino()
    arduino.digitalWrite(LED, 0)
    #board.digital[LED].write(0)
    estado['led'] = False
    return inicio()

def mostra_estado():
    """ global qntclick
    qntclick="DESLIGADO"
    return render_template('teste.html', **estado, click=qntclick) """
    
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)