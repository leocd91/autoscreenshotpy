# autoscreenshotpy
auto screenshot webinar / virtual meeting presentation when the slides changes.

## Background
- [x] Too many webinar / virtual meeting
- [x] ~~Too lazy to screenshot, move it to docs etc~~.
- [x] I just want to focus on the presentation

Just got a little time to code this (***speedrun!!!***), so if there's any problem just submit the issue.

## How it works
1. We set the screen area which will be saved
2. We set the focus area (for example, part of the slides) which the program will monitor. 
3. If the area of focus changes (simulate presenter changing to the next slide), the program will save the screen area we wanted to save.

![Demo](demo.gif)

## Requirements
- python 3.x on Windows OS (haven't tried it on other OS yet)

## Package I use (tried to make this as lightweight as possible)
- ```tkinter```
- ```os```
- ```PIL```
- ```time```
- ```datetime```
- ```ctypes```

## Installation
Copy or clone this package.

## How to Use
1. Run the ```run_auto_screenshot.bat```.
2. Select ```Area to Screenshot```, which will be saved, then ```Area to Focus``` (part of the slides), which if it changes, will trigger the save function. Avoid selecting area which change constantly like presenter's face cam, etc.
3. Enjoy your presentation! The files will be saved on ```screenshot``` folder.

## Credits & Source
- https://stackoverflow.com/questions/58128787/python-use-mouse-to-draw-a-rectangle-around-objects-in-any-window-also-store-s
- https://stackoverflow.com/questions/3585293/pil-imagegrab-fails-on-2nd-virtual-monitor-of-virtualbox
- https://www.programcreek.com/python/example/72489/PIL.ImageChops.difference
