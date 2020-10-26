from flask import Flask, render_template, Response
import cv2
import time
import threading
from threading import Thread

# The flask app
app = Flask(__name__)

# Video feed generator
source = None

@app.route('/')
def index():
    """ Default route """
    return render_template('index.html')

@app.route("/video_feed")
def video_feed():
    """ Serves the video feed """
    return Response(source(), mimetype="multipart/x-mixed-replace; boundary=frame")

def start(image_source):
    """
    Start the flask server and begin serving the video feed

    Args:
        image_source (generator): A generator that produces the video stream to serve
    """
    # I know globals are bad, but making flask into a class looked hard
    global source
    source = image_source

    # Start flask server publicly on port 5000, don't reload so we don't 
    app.run(host='0.0.0.0', port=5000, debug=True, threaded = True, use_reloader=False)
