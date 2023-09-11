import cat
class Ocelot(cat.Cat):

  def feed(self,player):
    """Feed the cat based on the state of the cat’s hunger level"""
    if self.hunger <= 2:
      self.update_hunger(5) # updates the cat's hunger
      player.take_damage(7) # updates the player's damage
      print(self.name + " is so hungry that when you set down the piece of meat "+ self.name +" takes a chunk of your arm. You take 7 damage")
    elif self.hunger <= 5:
      self.update_hunger(5)
      player.take_damage(5)
      print(self.name + " is pretty hungry and tackles you. You take 5 damage.")
    elif self.hunger <= 8:
      self.update_hunger(1)
      print(self.name + " is not that hungry but still eats the meat you set down for them.")
    else:
      self.update_hunger(-3) #update hunger 
      print(self.name+" is not hungry.") #return description

  def play(self,player):
    """Play with the cat based on the state of the cat’s hunger level"""
    if self.hunger <= 2:
      self.update_hunger(-1) # updates the cat's hunger
      player.take_damage(6) # updates the player's damage
      print(self.name + " is starving and doesn't want to play. Since "+self.name+" is hungry they stalk you and tackle you to the floor. You take 6 damage")
    elif self.hunger <= 5:
      self.update_hunger(3)
      player.take_damage(4)
      print("You throw a ball at "+self.name+" but since they're hungry they become angry and hit you. You take 4 damage")
    elif self.hunger <= 8:
      self.update_hunger(-2)
      print(self.name + " does not want to play. "+self.name+" is full. ")
    else:
      self.update_hunger(-4) #update hunger 
      print(self.name+" does not want to play. However it seems like they want to be pet.") #return description

  def pet(self,player):
    """Pet the cat based on the state of the cat’s hunger level """
    if self.hunger <= 2:
      self.update_hunger(2) # updates the cat's hunger
      player.take_damage(9) # updates the player's damage
      print(self.name + " sheds a tear because of how hungry they are. "+self.name+" does not let you pet them. They take a chunk of your legs. You take 9 damage ")
    elif self.hunger <= 5:
      self.update_hunger(-2)
      print(self.name +" is hungry but they enjoy you petting them. ")
    elif self.hunger <= 8:
      self.update_hunger(-4)
      print(self.name + " is full and purrs happily.")
    else:
      self.update_hunger(-6) #update hunger 
      print(self.name+" does not let you pet them.") #return description