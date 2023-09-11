import cat
class Tabby(cat.Cat):

  def feed(self,player):
    """Feed the cat based on the state of the cat’s hunger level"""
    if self.hunger <= 2:
      self.update_hunger(5) # updates the cat's hunger
      player.take_damage(2) # updates the player's damage
      print(self.name + " is so hungry that when you set down the Friskies Seafood Sensations, "+ self.name +" bites your finger. You take 2 damage")
    elif self.hunger <= 5:
      self.update_hunger(5)
      player.take_damage(5)
      print(self.name + " is pretty hungry and stratches your arm when you feed them a Delectable Squeeze up. You take 5 damage")
    elif self.hunger <= 8:
      self.update_hunger(1)
      print(self.name + " is not that hungry but still eats the Meow Mix. ")
    else:
      self.update_hunger(-3) #update hunger 
      print(self.name+" is not hungry.") #return description

  def play(self,player):
    """Play with the cat based on the state of the cat’s hunger level"""
    if self.hunger <= 2:
      self.update_hunger(-1) # updates the cat's hunger
      player.take_damage(3) # updates the player's damage
      print(self.name + " is starving and doesn't want to play. Since "+self.name+" is hungry they hiss at you and scratch your eye. You take 3 damage")
    elif self.hunger <= 5:
      self.update_hunger(-3)
      player.take_damage(4)
      print("You play with a string which "+self.name +" follows. "+self.name+" is so excited that he latches onto your arm. You take 4 damage")
    elif self.hunger <= 8:
      self.update_hunger(-2)
      print(self.name + " does not want to play. "+self.name+" is full. ")
    else:
      self.update_hunger(-4) #update hunger 
      print(self.name+" does not want to play. They angrily swat the string") #return description

  def pet(self,player):
    """Pet the cat based on the state of the cat’s hunger level """
    if self.hunger <= 2:
      self.update_hunger(1) # updates the cat's hunger
      player.take_damage(3) # updates the player's damage
      print(self.name + " is really hungry and doesn't let you pet him. "+self.name+" scratches your cheek angrily. You take 3 damage ")
    elif self.hunger <= 5:
      self.update_hunger(-3)
      print(self.name +" happily lets you pet them.")
    elif self.hunger <= 8:
      self.update_hunger(-3)
      print(self.name + " is full and purrs happily as they go to sleep.")
    else:
      self.update_hunger(-5) #update hunger 
      print(self.name+" does not let you pet them.") #return description