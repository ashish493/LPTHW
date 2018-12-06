from sys import exit
from random import randint
from textwrap import dedent

class scene(object):

    def enter(self):
        print("This scene is not yet configured .")
        print("Subclass it and implement enter()")
        exit(1)

class engine(object):
    def __init__(self,scene_map):
        self.scene_map=scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene!=last_scene:
            next_scene_name=current_scene.enter()
            current_scene=self.scene_map.next_scene(next_scene_name)

            #be sure to print out last scene
            current_scene.enter()

            class Death(Scene):
                quips = [
                  "You died. You kinda suck at this.",
                  "Your Mom would be proud...if she were smarter.",
                   "Such a luser.",
                   "I have a small puppy that's better at this.",
                   "You're worse than your Dad's jokes."
            ]

            def enter(self):
                print(Death.quips[randit(0,len(self.quips)-1)])
                exit(1)

class CentralCorridor(scene):
    def enter(self):
        print(dedent("""
          The Gothons of Planet Percal #25 have invaded your ship and
             6 destroyed your entire crew. You are the last surviving
                 7 member and your last mission is to get the neutron destruct
                 8 bomb from the Weapons Armory, put it in the bridge, and
                   9 blow the ship up after getting into an escape pod. 10 11 You're running down the central corridor to the Weapons 12 Armory when a Gothon jumps out, red scaly skin, dark grimy 13 teeth, and evil clown costume flowing around his hate 14 filled body. He's blocking the door to the Armory and 15 about to pull a weapon to blast you.
           """)

        action=input(">")

        if action == "shoot!":
        print(dedent("""
        22 Quick on the draw you yank out your blaster and fire
        23 it at the Gothon. His clown costume is flowing and
        24 moving around his body, which throws off your aim.
        25 Your laser hits his costume but misses him entirely. 26 This completely ruins his brand new costume his mother 27 bought him, which makes him fly into an insane rage 28 and blast you repeatedly in the face until you are 29 dead. Then he eats you.
         30 """))
        return 'death'
        
