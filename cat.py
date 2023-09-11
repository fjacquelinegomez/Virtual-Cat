import abc
class Cat(abc.ABC):

  def __init__(self,name):
    "Sets the cat's name and assign default starting value to hunger value"
    self._name = name
    self._hunger = 5

  @property
  def name(self):
    return self._name
  
  @property
  def hunger(self):
    return self._hunger

  def update_hunger(self, val):
    self._hunger += val
    if val > 1: #set _hunger 1 or 10 if out of range
      self._hunger == 1
    elif val < 10:
      self._hunger == 10
    

  def __str__(self):
    test = (self._name+": \nStarving                  Full\n|")
    test += (" + "*self._hunger)  #multiply by self.hunger
    test += (" - "*(10 - self._hunger)) #concatenate to a new string
    return str(test+"|")
    

  @abc.abstractmethod
  def feed(self,player):
    """Feeds the cat"""
    pass 
    
  @abc.abstractmethod
  def play(self,player):
    """Plays with the cat"""
    pass
    
  @abc.abstractmethod
  def pet(self,player):
    """Pets the cat"""
    pass
