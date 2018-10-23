from flask import Flask, request, render_template, redirect, url_for
import RPi.GPIO as GPIO
import time

channel = 21

app = Flask(__name__)

def buzz_in():
    print("Fake buzz!")

def buzz_in_old():
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(channel, GPIO.OUT)
        GPIO.output(channel, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(channel, GPIO.LOW)
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()

@app.route('/')
def index():
    return "Hello"


@app.route('/open-sesame/7895327894', methods=['POST', 'GET'])
def open_sesame():
    if request.method == 'POST':
        buzz_in();
        return redirect(url_for('open_sesame'))
    else:
        return render_template('open-sesame.html')
