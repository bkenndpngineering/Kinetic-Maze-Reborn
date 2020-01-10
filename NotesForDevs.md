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


##Submodules/Libraries
Instead of editing Tracker when you need new functions, make changes in Kinect_Skeleton_Tracker and push to that, the do the submodule init/update.
This version of highscores.py is partially rewritten from the one in GenericUtils!




##Contact Info
Andrew Xie -
