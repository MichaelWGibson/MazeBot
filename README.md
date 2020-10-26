# MazeBot
A maze solving robot


# Setup

First make sure you have python installed 

## Install Dependencies

Run the following command
```
pip install opencv-python, flask 
```

## Adjust configurations

Edit the config dictionary in src/config.py

For desktop development use (If this doesn't work try setting the port to 1)
```python
config = {
    "camera" : {
        "type" : "web",
        "port" : 0
    }
}
```

To use g-streamer (only available on pi/jetson)
```python
config = {
    "camera" : {
        "type" : "pi"
    }
}
```

## Run

Then run `python src/maze_bot.py`  
And navigate to http://localhost:5000/  
If everything works you should see an image from your camera

