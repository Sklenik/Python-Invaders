# Python Invaders
- This is my version of the 1978 videogame **SPACE INVADERS**
- I apologize to english only users, half of the code is in czech, variables and comments alike. It's because this was my first project and I was more focused on the actual functionality than on the styling or general state of the code. 

### PYTHON INVADERS MANUAL

#### Launching the game
- To launch the game, open the */invaders* folder as root in any IDE and launch the *invaders_aplha.py* as a script.
- It is important to launch the game as a script, in such a way that the root folder is the *invaders/* folder. Otherwise it won't work.
- You might ask why so complicated. Well, this was my first project, so, yeah, not really optimalized for general use. There is no .exe file, you are launching a script, and because of that, it must be launched exactly from the */invaders* path, so it can operate with paths like this one:

`turtle.register_shape("Sprites/Hrac/Laser_Cannon.gif")`

#### Notice
- The game was made in python 3.9 in microsoft visual studio code IDE, where it was always working. I am not responsible for any crashes in other IDE's or python versions and will not update the code to make it compatible with other programs.
- The game uses the winsound library, so the game might work on apple and linux, but there will be no sound. I am not porting the sound code to be multiplatform, sorry.
- Do not open *invaders_alpha.py* directly. Any attempts to do so will lead to crashes and might corrupt the code. Launch the game as a script from an IDE.
- Do not move or rename any files, you will most likely break the game.

#### Controls and interface

- The game is simmilar to the original space invaders from 1978, really simple black and white game.
- The player is playing as a cannon in the bottom of the screen. You can move using the left and right arrow keys, and shoot using spacebar.
- In the top left corner is a score counter. To win the game, shoot all invaders from the sky. If you manage to do so or fail, a message will be displayed, offering you restarting the game with the R key, or quitting with the esc key, and displaying your final score.

# Credit
Created: 24.1.2022 by me.

Finished: 7.2.2022 by me.

You are free to play the game or use my code, however please do not claim this as your work, it took me some time and I wouldn't like seeing this displayed elsewhere. There are many tutorials for simmilar python games on YouTube and else on the internet, you can make your own.

Thanks and have fun.

-*Sklenik*


