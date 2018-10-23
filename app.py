from flask import Flask, request, render_template, redirect, url_for, flash
import RPi.GPIO as GPIO
import time

channel = 21

app = Flask(__name__)
app.secret_key = b'74b2055bf813a37c67d7c018f2ae91ce'

def buzz_in():
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
        flash("Enterrrr.")
        return redirect(url_for('open_sesame'))
    else:
        return render_template('open-sesame.html')
