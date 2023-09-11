class Player:
  """Creates the player's hit points, tracking and updating their damage."""
  def __init__(self):
    hp = 25
    self._hp = hp

  @property
  def hp(self):
    return self._hp

  def take_damage(self, dmg):
    """subtracts the damage from the player's hp"""
    self._hp -= dmg
    if self._hp < 0:
      self._hp = 0 

  def __str__(self):
    return "\nYou have " +str(self._hp)+ " hp."