# FruitPopper
This is a fun little game that I made in Python. It takes insparation from the old mobile game "Fruit Ninja".
<img width="500" alt="Screenshot 2025-05-12 at 10 39 18 PM" src="https://github.com/user-attachments/assets/9435a6b4-c224-4ea8-a45e-1e8690d99547" />

<img width="500" alt="Screenshot 2025-05-12 at 10 32 04 PM" src="https://github.com/user-attachments/assets/6f2bcffc-18c9-465b-9a1d-fefc087c0a9b" />




# How to Play
Make sure to download the files and folders, and move them into a folder in your local workspace. Once you are moved into the corect directory make sure to type: "pip install pygame" into the terminal. After that the game is set up and ready to go, just run the program and the game should automatically open up a new window for you to play the game.

# What this project shows
Not only was this a fun project to make, but this coding project encompasses a lot of very important skills and concepts.

Proper Memory Allocation - Throughout this game there are a number of sprite objects consisting of both fruits and bombs. One thing I wanted when creating this game, was for the possability of multiple sprites to be on the screen at the same time. Not only did this add the challange of having to deal with multiple objects at once, but forced me to use proper and smart memory allocation. Each of the sprites are kept in a group/list/array. I put extra effor into making sure that once each sprite leaves the screen or is clicked on, that it is properly destroyed and the memory used to allocate it is freed. This ensures that the game runs smoothly and will not cause any memory leaks or buildup of uneeded memory.

Sprite Class OOP - Another thing I wanted to do for this project, was have "Game Design Correct" Sprite classes. For those who don't know, a Sprite class is a class that gives objects/players/enemies in games their own attributes. Throughout this game, every bomb and fruit is a Sprite. So within this game Bombs, Fruits and even the Player themselves are built in to their own Sprite class. This makes the code MUCH more organized, and more easierly allows for functionality to be added to this game.

Animation - You'll notice in this game, that when clicked on, both Bombs and Fruits explode(With fun sound effects made by me). This presented the challange of making an animation for each sprite. When each object is 'clicked' on by the player, it activated a sprite class function that causes the object to go into a state of animation. Displaying a series of images before properly deleting the sprite. 

GUI - Lastly this game has a GUI, I did my best to design it as "Retro" and "Zen" and hope it paid off. This project took a lot of time designing how things "look" and considering where certain objects are, on screen.

# What I learned:
This project was one of the first I put on my resume/website. While I don't exactly want to go into Game Design, I think this is a great overall project to showcase my skills. Creating a game involved the combination of many technical coding skills. This project tested my skills of OOP as well as taught me how to create a proper Sprite class. As well as taught be how to organize data, organize code, work with a GUI, and overall had me worry about "All the little things" that go on behind the scences of a videogame.

I am proud of this basic game, as I created it very early in my coding career. And I also created this fully on my own without copying the code from a tutorial or video. Instead I took the time to learn "pygame" and work through how to solve problems on my own.
