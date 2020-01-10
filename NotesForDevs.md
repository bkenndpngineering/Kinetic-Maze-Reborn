#Notes for future devs

Hope this helps! This project was inherited with zero documentation, so hopefully this can speed up the process of understanding the project.

Last updated: Jan 10 2020, by Andrew Xie

pre-2019/2020 was done by Paul. 2019/2020 was done by Braedan Kennedy and Andrew Xie.

## Organization/How this project works
Important files/folders, in no particular order:
Kinect_Skeleton_Tracker stores the code that interfaces with the Kinect.
Highscores.py is the scoreboard management code, and the scoreboard itself is stored in highscores.txt
Interact.py stores the custom pygame gui elements, currently just a button.
The "arcade" font is stored in assets (if sound/music is added it'll be in there too), and the JSON configs from Paul are in configs.
main.py, of course, is the main program (run this with python3 main.py to run the project).
physics.py is code for the motor that Paul wrote for the first iteration of this project (pre-2019/2020)

We realize that using JSON configs parsed through a custom function, and the weirdness of physics.py is not the best, however, we have no idea if we can replace it since it's so highly specific to the motor the project uses. We've just lived with it and tried not to touch it because when we tried we broke things, however if you want to replace it, it's probably for the best, go for it.

### main.py organization
This is the main program that'll need explanation probably, the other python files are mainly libraries for functions used in main.

The first few lines are the normal python setup, declaring objects and setting global variables (like fonts). Within that, buttons are declared, with where they're drawn, text, color, etc declared BUT NOT WHAT THEY DO WHEN PRESSED.

prog_running is the main program loop. Every loop, it pulls a frame with the skeleton drawn from the tracker. We use gamestate to store what screen the game displays, main being the main menu, game the game when running, scoreboard being scoreboard display, name being the score input screen, etc. Add as needed. The screens are displayed within if statements, since the while loop runs fast enough to update the screen quickly.

Buttons and other static text are drawn right after the new frame is gotten, and after that various joints are pulled from the tracker.

After joint info is pulled, interactive code runs. From the game, to the actions involved with all the buttons being pushed and what they update, are within the "angle is not None" if statement.

(See Current problems section)

A few keyboard keys are currently bound to functions to quit and toggle the tracker, probably remove as problems are solved.

##Submodules/Libraries
Instead of editing Tracker when you need new functions, make changes in Kinect_Skeleton_Tracker and push to that, the do the submodule init/update.
This version of highscores.py is partially rewritten from the one in GenericUtils!


## Current Problems/Potential tasks never got to

Each button press is detected by the same code, copy pasted. Maybe make it a function?

Need a way to access the admin screen, by gesture or physical button.

[Severe] The program crashes the computer with packet loss after around 4.5 minutes of continuous operation. Not tested with people constantly being tracked but that'll probably have the same effect. No idea how to fix, Paul's code mentioned starting a fake stream (then killing it after a short delay) to "bypass a bug," but did not mention what the bug is. Tried that, didn't work. Maybe use the tracker toggle to activate at certain times? Or to toggle the tracker when no body is detected to try to reset the packet loss?  


##Contact Info
Ask a teacher or something, info might change so response not 100% guaranteed.
