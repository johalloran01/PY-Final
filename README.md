# PY-Final




YouTube Video: https://youtu.be/mtkniZG81f4



Josh Trimble, Khanh Nguyen, & Josh O'Halloran
We originally set out with incredibly lofty goals! 
Some of our goals included: 
  sprite interactions 
  items pick up
  combat 
  close ranged and ranged attacks 
  multiple maps 
  and more .
In the process of learning pygame, we realized that acheiving all of these goals in the 3-4 week period that we had, while simultaneously taking other classes and working full time, proved that our goals we a little too lofty. 

First challenge we ran into was the process of understanding how to create a map, and then apply impact to that map. Josh O'Halloran found a tile based design program to design maps and Khanh designed the map. He later then went through the process of adding impact, which virtually meant making the map have boundaries and collision. 

The next challenge was taking the asset sprite sheets that we had found via itch.io as public domain, and animating them using a spritesheet format. Josh Trimble spent time understanding and applying spritesheet animations to the "hero" sprite, however through research we discovered another method for animation which was applied in the code. The code is as follows: 
	def import_player_assets(self):
		character_path = '../graphics/playertest/'
		self.animations = {
			'left':[],'right':[],'left_idle':[],'right_idle':[],'left_attack':[],'right_attack':[]
		}
		for animation in self.animations.keys():
			full_path = character_path + animation
			self.animations[animation] = import_folder(full_path)
 This code creates different dictionaries, and applies a seperate image into those dictionaries which creates the animation for the character. It's also how we implement attack animations and direction based code later on. 
 
 The last leg of this journey we spent time trying to load in NPCs however animating them while "idle" proved to be difficult. Given more time we would have used the sprite sheet format, implemented by Josh Trimble, to animate idle NPC's. We also have code in our program that would have taken the absolute value of the location of the character, in relation to the NPC, and activated a speech bubble effect. As you can see we have a ghostly NPC we have named "Rosen NPC" which was to be the guide to the story. 
 
 The learning curve for pygame is steap. If there isn't already a gaming format out there, that has already been developed, developing your own original idea from scratch is both time consuming and involves many layers and moving parts. It felt similar to working with Nodes in blender. 
 
 Aspects of the project we enjoyed thoroughly: 
    The success of animating a sprite 
    Working with a team to help each other out 
    The over all unique-ness of our project and how it looks 
    Learning about classes in python, and how to implement them. 
    Learning about file pathing and calling. 
    
Aspects of the project that we had DIFFICULTY on: 
    Everything. At no point in time were we ever "comfortable" with this project. Which speaks volumes to the challenges of coding and a career in technology. I think  every one of us had to break out of their comfort zones and relearn how to apply their problem solving skills. 
    
