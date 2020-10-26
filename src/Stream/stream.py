import math
from flask import Flask, render_template, Response, request

# The flask app
app = Flask(__name__)

# Globals
SOURCE = None
DRIVE = None


@app.route('/')
def index():
    """ Default route """
    return render_template('index.html')


@app.route("/video_feed")
def video_feed():
    """ Serves the video feed """
    return Response(SOURCE(), mimetype="multipart/x-mixed-replace; boundary=frame")


@app.route("/heading", methods=['POST'])
def set_heading():
    """ Receives a raw heading from the joystick """
    # Get data from form
    speed = request.form.get('speed',  type=float)
    angle = request.form.get('angle',  type=float)

    # Cap speed at a force of 3, scale range [0, 1]
    speed = min(speed, 3) / 3

    # Rotate one quarter turn
    angle = (angle + math.pi/2) % (math.pi * 2)

    # Invert and center for a range of [-π, π]
    angle = -angle + math.pi

    DRIVE.set_heading(speed, angle)
    return "done"


def start(image_source, drive_train):
    """
    Start the flask server and begin serving the video feed

    Args:
        image_source (generator): A generator that produces the video stream to serve
    """
    # I know globals are bad, but making flask into a class looked hard
    global SOURCE
    SOURCE = image_source

    global DRIVE
    DRIVE = drive_train

    # Start flask server publicly on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True,
            threaded=True, use_reloader=False)
