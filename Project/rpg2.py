# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 13:33:07 2019

@author: Grace
"""

#!/bin/python3
import random
def showInstructions():
    #print a main menu and the commands
    print('''
RPG Game
========

Get to the Garden with a key and a potion and a scroll
Avoid the monsters!

Commands:
  go [direction]
  get [item]
''')

def showStatus():
    
    #with open("C:\Users\Grace\Desktop\MAP.txt") as f:
        #for x in f.read():
            #print x
    fo=open("C:\Users\Grace\Desktop\Project\MAP.txt")
    str1=fo.read()
    print str1
  #print the player's current status
    print('\n---------------------------')
    if currentRoom=='Garden':
        print("You are in the Garden but you don't have the required items go back to get them...")
    else:
        print('You are in the ' + currentRoom)
  #print the current inventory
    print("Inventory : " + str(inventory))
  #print an item if there is one
    if "item" in rooms[currentRoom]:
        if currentRoom=='Kitchen':
            print("You see a box")
        else:    
            print('You see a ' + (rooms[currentRoom]['item']))
      
      
    print("---------------------------")

#an inventory, which is initially empty
inventory = []
prize=['monster','gemstone','10 gold coins','chicken']
chest=random.choice(prize)
#a dictionary linking a room to other room positions
rooms = {

            'Hall' : { 'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'west'  : 'Garden',
                  'item'  : 'key'
                },        

            'Kitchen' : { 'north' : 'Hall',
                         'east' : 'Basement',
                  'item'  : chest
                },
                
            'Dining Room' : { 'west'  : 'Hall',
                  'south' : 'Basement',
                  'item'  : 'potion'
              
                },
                
            'Garden' : { 'east' : 'Hall' },
            'Basement' : {'north':'Dining Room',
                          'west' : 'Kitchen',
                        'item':'scroll'
                       }

         }

#start the player Randomly
currentRoom = random.choice(rooms.keys())

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':  
    move = raw_input('>')
    
  move = move.lower().split()

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
      print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
      if 'item' in rooms[currentRoom] and chest in rooms[currentRoom]['item'] and move[1]=="box":
              if chest=='monster':    
                  print('A monster has got you... GAME OVER!')    
                  break
              else:
                  inventory+=[chest]
                  print(chest + ' got!')
      #delete the item from the room
                  del rooms[currentRoom]['item']
      
          
    #if the room contains an item, and the item is the one they want to get
      elif 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
          if 'item' in rooms[currentRoom] and 'scroll' in rooms[currentRoom]['item']:
              print("---------------------------")  
              print ("Its a riddle...\n\n What's the most ancient way to see through walls...???")
              move1=raw_input('>')
              if(move1=='Window' or move1=='window'):
                  inventory +=[move[1]]
                  print("Correct Answer !!!  "+move[1] + ' got!')
      #delete the item from the room
                  del rooms[currentRoom]['item']
              else:
                  print("Answer is wrong can't get scroll")
              
      #add the item to their inventory
          else:
              
      #add the item to their inventory
      
              inventory += [move[1]]
      #display a helpful message
              print(move[1] + ' got!')
      #delete the item from the room
              del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
      else:
      #tell them they can't get it
        print('Can\'t get ' + move[1] + '!')

  # player loses if they enter a room with a monster
  

  # player wins if they get to the garden with a key and a shield
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory and 'scroll' in inventory  or 'gemstone' in inventory:
    print('You escaped the house... YOU WIN!')
    break
  