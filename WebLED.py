from singleton import Arduino
from flask import Flask, render_template


LED = 13
Botao = 12
estado = {'led' : True}

app = Flask(__name__,template_folder='template')

#arduino = Arduino('OM')
#arduino.digitalWrite(LED, 1)
#arduino.pass_time(3)
 
@app.route('/')
def inicio():
 return mostra_estado()

@app.route('/led/1')
def ligar_led():
 arduino = Arduino()
 arduino.digitalWrite(LED, 1)
 estado['led'] = True
 return mostra_estado()

@app.route('/led/0')
def desl_led():
 arduino = Arduino()
 arduino.digitalWrite( LED, 0)
 estado['led'] = False
 return mostra_estado()
    
def mostra_estado():
 return render_template('teste.html', **estado)

if __name__ == "__main__":
 app.run(host='0.0.0.0', debug=True)