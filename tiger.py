import cat
class Tiger(cat.Cat):

  def feed(self,player):
    """Feed the cat based on the state of the cat’s hunger level"""
    if self.hunger <= 2:
      self.update_hunger(5) # updates the cat's hunger
      player.take_damage(5) # updates the player's damage
      print(self.name + " is so hungry that when you set down the steak,"+ self.name +"mistakes you for food and bites you for 5 damage.")
      #return description
    elif self.hunger <= 5:
      self.update_hunger(5)
      player.take_damage(2)
      print(self.name + "is pretty hungry and accidentally bites you when you when it takes the steak from your hand.  ")
      #return description
    elif self.hunger <= 8:
      self.update_hunger(1)
      print(self.name +" is a little hungry and only takes a few bites of his steak. ")
    else:
      print(self.name +" is extremly full and walks away when you set down the steak.")


  def play(self,player):
    """Play with the cat based on the state of the cat’s hunger level"""
    if self.hunger <= 2: 
      self.update_hunger(5) # updates the cat's hunger
      player.take_damage(8) # updates the player's damage
      print(self.name +" is starving and doesn't want to play right now." +self.name+ " suddenly pounces on you and bites out a big chunk out of your leg for 8 damage." ) #return description
      
    elif self.hunger <= 5: 
      self.update_hunger(-3)
      player.take_damage(3)
      print(self.name + " is hungry and doesn't want to play with the ball you threw." +self.name+ " begins to chase you and bites your arm for 3 damage.")

    elif self.hunger <= 8: 
      self.update_hunger(-2)
      player.take_damage(2)
      print(self.name + " happily plays with the giant ball you threw, but accidently scratches you with his sharp claw when you got to pick the ball back up.")

    else: 
      self.update_hunger(-1)
      print(self.name +" is too full to play, he heads to his favorite spot to take a nap, ignoring the ball that you threw.")
      
  def pet(self,player):
    """Pet the cat based on the state of the cat’s hunger level """
    if self.hunger <= 2: 
      self.update_hunger(5) # updates the cat's hunger
      player.take_damage(8) # updates the player's damage
      print(self.name +" is extremely hungry and bites off your pinky finger as you try to pet them." ) #return description

    elif self.hunger <= 5: 
      self.update_hunger(-3)
      player.take_damage(3)
      print(self.name + " is hungry, they pounce on you as you walk over to pet them because they thought you were their dinner.")

    elif self.hunger <= 8: 
      self.update_hunger(-1)
      print(self.name + " happily purrs and  allows you to pet them.")

    else: 
      self.update_hunger(-1)
      print(self.name +" is incredibly full and purrs happily as they drift off to sleep.") #return description