# Raspberry Pi Portraits Animation

## Raspberry Pi Camera setup

Connect a momentary push-button switch to `GPIO pin 18` and `Ground` of the Raspberry Pi

Next connect an LED to `GPIO pin 17` and `Ground` of the Raspberry Pi

install *pip*

https://pip.pypa.io/en/latest/installing.html#pip-included-with-python

install *request*

http://docs.python-requests.org/en/latest/user/install/#install

## Server setup (still on Raspberry Pi)

install npm packages

    npm install

make animation.db file in storage/db/

    touch storage/db/animation.db

## Run Server

install node them run server.js

    node server.js

start camera

    sudo python camera.py

By adding ` &` to the end of both commands, allows each script to run in the background.

Make sure to wait for both scripts to print out to the terminal that they have started.

## Tests

Before starting the animation, it is important to test the camera's brightness

    python tests/camera/brightness.py

To set the brightness for the camera, you must edit camera.brightness in camera.py

    vim camera.py
