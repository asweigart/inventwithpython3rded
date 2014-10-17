Chapter 19 - Sound and Images

Topics Covered In This Chapter:

Image and Sound Files
Drawing Sprites
The pygame.image.load() Function
The pygame.mixer.Sound Data Type
The pygame.mixer.music Module
In the last two chapters, we've learned how to make GUI programs that have graphics and can accept input from the keyboard and mouse. We've also learned how to draw shapes in different colors on the screen. In this chapter, we will learn how to show pictures and images (called sprites) and play sounds and music in our games.

A sprite is a name for a single two-dimensional image that is used as part of the graphics on the screen. Here are some example sprites:


Figure 19-1: Some examples of sprites.

This is an example of sprites being used in a complete scene.


Figure 19-2: An example of a complete scene, with sprites drawn on top of a background.

The sprite images are drawn on top of the background. Notice that we can flip the sprite image horizontally so that the sprites are facing the other way. We can draw the same sprite image multiple times on the same window. We can also resize the sprites to be larger or smaller than the original sprite image. The background image can also be considered one large sprite.

The next program we make will demonstrate how to play sounds and draw sprites using Pygame.

Image and Sound Files

Sprites are stored in image files on your computer. There are several different image formats that Pygame can use. You can tell what format an image file uses by looking at the end of the file name (after the last period). This is called the file extension. For example, the file happy.png is in the PNG format. The image formats Pygame supports include BMP, PNG, JPG (and JPEG), and GIF.

You can download images from your web browser. On most web browsers, you just have to right-click on the image in the web page and select Save from the menu that appears. Remember where on the hard drive you saved the image file. You can also create your own images with a drawing program like MS Paint or Tux Paint.

The sound file formats that Pygame supports are MID, WAV, and MP3. You can download sound effects from the Internet just like image files, as long as the sound effects are in one of these three formats. If you have a microphone, you can also record sounds with your computer yourself and use them in your games.

Sprites and Sounds Program

This program is the same as the Keyboard and Mouse Input program from the last chapter. However, in this program we will use sprites instead of plain looking squares. We will use a sprite of a little man instead of the white player square, and a sprite of cherries instead of the green food squares. We also play background music and a sound effect when the player sprite eats one of the cherry sprites.

The Sprites and Sounds Program's Source Code

If you know how to use graphics software such as Photoshop or MS Paint, you can draw your own images and use the image files in your games. If you don't know how to use these programs, you can just download graphics from websites and use those image files instead. The same applies for music and sound files. You can also find images on web sites or images from a digital camera. You can download the image and sound files from this book's website at http://inventwithpython.com/resources/. You can download the source code in this chapter from the URL http://inventwithpython.com/chapter19.

spritesAndSounds.py
This code can be downloaded from http://inventwithpython.com/spritesAndSounds.py
If you get errors after typing this code in, compare it to the book's code with the online diff tool at http://inventwithpython.com/diff or email the author at al@inventwithpython.com

import pygame, sys, time, random
from pygame.locals import *
# set up pygame
pygame.init()
mainClock = pygame.time.Clock()
# set up the window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Sprites and Sound')
# set up the colors
BLACK = (0, 0, 0)
# set up the block data structure
player = pygame.Rect(300, 100, 40, 40)
playerImage = pygame.image.load('player.png')
playerStretchedImage = pygame.transform.scale(playerImage, (40, 40))
foodImage = pygame.image.load('cherry.png')
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - 20), random.randint(0, WINDOWHEIGHT - 20), 20, 20))
foodCounter = 0
NEWFOOD = 40
# set up keyboard variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
MOVESPEED = 6
# set up music
pickUpSound = pygame.mixer.Sound('pickup.wav')
pygame.mixer.music.load('background.mid')
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True
# run the game loop
while True:
    # check for the QUIT event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # change the keyboard variables
            if event.key == K_LEFT or event.key == ord('a'):
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == ord('d'):
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == ord('w'):
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == ord('s'):
                moveUp = False
                moveDown = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == ord('a'):
                moveLeft = False
            if event.key == K_RIGHT or event.key == ord('d'):
                moveRight = False
            if event.key == K_UP or event.key == ord('w'):
                moveUp = False
            if event.key == K_DOWN or event.key == ord('s'):
                moveDown = False
            if event.key == ord('x'):
                player.top = random.randint(0, WINDOWHEIGHT - player.height)
                player.left = random.randint(0, WINDOWWIDTH - player.width)
            if event.key == ord('m'):
                if musicPlaying:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                musicPlaying = not musicPlaying
        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0] - 10, event.pos[1] - 10, 20, 20))
    foodCounter += 1
    if foodCounter >= NEWFOOD:
        # add new food
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - 20), random.randint(0, WINDOWHEIGHT - 20), 20, 20))
    # draw the black background onto the surface
    windowSurface.fill(BLACK)
    # move the player
    if moveDown and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.right += MOVESPEED
    # draw the block onto the surface
    windowSurface.blit(playerStretchedImage, player)
    # check if the block has intersected with any food squares.
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)
            player = pygame.Rect(player.left, player.top, player.width + 2, player.height + 2)
            playerStretchedImage = pygame.transform.scale(playerImage, (player.width, player.height))
            if musicPlaying:
                pickUpSound.play()
    # draw the food
    for food in foods:
        windowSurface.blit(foodImage, food)
    # draw the window onto the screen
    pygame.display.update()
    mainClock.tick(40)

Figure 19-3: The Sprites and Sounds game.

Setting Up the Window and the Data Structure

Most of the code in this program was explained in the previous chapter, so we will only focus on the parts that add sprites and sound.

pygame.display.set_caption('Sprites and Sound')
First, let's set the caption of the title bar to a string that describes this program on line 12. Pass the string 'Sprites and Sound' to the pygame.display.set_caption() function.

# set up the block data structure
player = pygame.Rect(300, 100, 40, 40)
playerImage = pygame.image.load('player.png')
playerStretchedImage = pygame.transform.scale(playerImage, (40, 40))
foodImage = pygame.image.load('cherry.png')
We are going to use three different variables to represent the player, unlike the previous programs that just used one. The player variable will store a Rect object that keeps track of where and how big the player is. The player variable doesn't contain the player's image, just the player's size and location. At the beginning of the program, the top left corner of the player will be located at (300, 100) and the player will have a height and width of 40 pixels to start.

The second variable that represents the player will be playerImage. The pygame.image.load() function is passed a string of the filename of the image to load. The return value of pygame.image.load() is a Surface object that has the image in the image file drawn on its surface. We store this Surface object inside of playerImage.

The pygame.transform.scale() Function

On line 20, we will use a new function in the pygame.transform module. The pygame.transform.scale() function can shrink or enlarge a sprite. The first argument is a pygame.Surface object with the image drawn on it. The second argument is a tuple for the new width and height of the image in the first argument. The pygame.transform.scale() function returns a pygame.Surface object with the image drawn at a new size. We will store the original image in the playerImage variable but the stretched image in the playerStretchedImage variable.

On line 21, we call pygame.image.load() again to create a Surface object with the cherry image drawn on it.

Be sure that you have the player.png and cherry.png file in the same directory as the spritesAndSounds.py file, otherwise Pygame will not be able to find them and will give an error.

The Surface objects that are stored in playerImage and foodImage are the same as the Surface object we use for the window. In our game, we will blit these surfaces onto the window's surface to create the window that the user sees. This is exactly the same as the when we got a Surface object returned from the render() method for Font objects in our Hello World program. In order to actually display the text, we had to blit this Surface object (which the text was drawn on) to the window's Surface object. (And then, of course, call the update() method on the window's Surface object.)

Setting Up the Music and Sounds

# set up music
pickUpSound = pygame.mixer.Sound('pickup.wav')
pygame.mixer.music.load('background.mid')
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True
Next we need to load the sound files. There are two modules for sound in Pygame. The pygame.mixer module is responsible for playing short sound effects during the game. The pygame.mixer.music module is used for playing the background music.

We will call the pygame.mixer.Sound() constructor function to create a pygame.mixer.Sound object (which we will simply call a Sound object). This object has a play() method that when called will play the sound effect.

On line 39 we call pygame.mixer.music.load() to load the background music. We will start playing the background music immediately by calling pygame.mixer.music.play(). The first parameter tells Pygame how many times to play the background music after the first time we play it. So passing 5 will cause Pygame to play the background music 6 times over. If you pass -1 for the first parameter, the background music will repeat itself forever.

The second parameter to pygame.mixer.music.play() tells at what point in the sound file to start playing. Passing 0.0 will play the background music starting from the very beginning. If you passed 2.5 for the second parameter, this will cause the background music to start playing two and half seconds after the start of the music.

Finally, we have a simple Boolean variable named musicPlaying that will tell our program if it should play the background music and sound effects or not. It is nice to give the player the option to run the program without the sound playing.

Toggling the Sound On and Off

            if event.key == ord('m'):
                if musicPlaying:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                musicPlaying = not musicPlaying
We will check if the user has pressed the M key. The M key will turn the background music on or off. If musicPlaying is set to True, then that means the background music is currently playing and we should stop the music by calling pygame.mixer.music.stop(). If musicPlaying is set to False, then that means the background music is not currently playing and should be started by calling pygame.mixer.music.play(). The parameters we pass to the pygame.mixer.music.play() function are the same as we passed on line 40.

Finally, no matter what, we want to toggle the value in musicPlaying. Toggling a Boolean value means we set it to the opposite of its current value. The line musicPlaying = not musicPlaying will set the variable to False if it is currently True or set it to True if it is currently False. Think of toggling as what happens when you flip a light switch on or off.

Toggling the value in musicPlaying will ensure that the next time the user presses the M key, it will do the opposite of what it did before.

Drawing the Player on the Window

    # draw the block onto the surface
    windowSurface.blit(playerStretchedImage, player)
Remember that the value stored in playerStretchedImage is a Surface object. "Blitting" is the process of drawing the contents of one Surface object to another Surface object. In this case, we want to draw the sprite of the player onto the window's Surface object (which is stored in windowSurface). (Also remember that the surface used to display on the screen is the Surface object that is returned by pygame.display.set_caption().)

The second parameter to the blit() method is a Rect object that specifies where the sprite should be blitted. The Rect object stored in player is what keeps track of the position of the player in the window.

Checking if the Player Has Collided with Cherries

        if player.colliderect(food):
            foods.remove(food)
            player = pygame.Rect(player.left, player.top, player.width + 2, player.height + 2)
            playerStretchedImage = pygame.transform.scale(playerImage, (player.width, player.height))
            if musicPlaying:
                pickUpSound.play()
This code is similar to the code in the previous programs. But here we are adding a couple of new lines. We want to call the play() method on the Sound object stored in the pickUpSound variable. But we only want to do this if musicPlaying is set to True (which tells us that the sound turned on).

When the player eats one of the cherries, we are going to enlarge the size of the player by two pixels in height and width. On line 116, we create a new Rect object to store in the player variable which will have the same sizes as the old Rect object stored in player. Except the width and height of the new Rect object will be 2 pixels larger.

When the Rect object that represents the position and size of the player, but the image of the player is stored in a playerStretchedImage as a Surface object. We want to create a new stretched image by calling pygame.transform.scale(). Be sure to pass the original Surface object in playerImage and not playerStretchedImage. Stretching an image often distorts it a little. If we keep restretching a stretched image over and over, the distortions add up quickly. But by stretching the original image to the new size, we only distort the image once. This is why we pass playerImage as the first argument for pygame.transform.scale().

Draw the Cherries on the Window

    # draw the food
    for food in foods:
        windowSurface.blit(foodImage, food)
In our previous programs, we called the pygame.draw.rect() function to draw a green square for each Rect object stored in the foods list. However, in this program we want to draw the cherry sprites instead. We will call the blit() method and pass the Surface object stored in foodImage. (This is the surface that has the image of cherries drawn on it.)

We only use the food variable (which contains each of the Rect objects in foods on each iteration through the for loop) to tell the blit() method where to draw the foodImage.

Summary: Games with Graphics and Sounds

This game has added even more advanced graphics and introduced using sound in our games. The images (called sprites) look much better than the simple drawing primitives used in our previous programs. The game presented in this chapter also has music playing in the background while also playing sound effects.

Sprites can be scaled (that is, stretched) to a larger or smaller size. This way we can display sprites at any size we want. This will come in handy in the game presented in the next chapter.

Now that we know how to create a GUI window, display sprites and drawing primitives, collect keyboard and mouse input, play sounds, and implement collision detection, we are now ready to create a graphical game in Pygame. The next chapter brings all of these elements together for our most advanced game yet.
