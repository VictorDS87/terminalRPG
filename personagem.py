# Personagem: classe mae
# Heroi: controlado pelo usuario
# Inimigo: adversario do usuario

class Personagem:
  def __init__(self, name, life, level):
    self.__name = name
    self.__life = life
    self.__level = level

  def get_name(self):
    return self.__name
  
  def get_life(self):
    return self.__life
  
  def get_level(self):
    return self.__level

  def show_details(self):
    return f"Name: {self.__name}\nLife: {self.__life}\nLevel: {self.__level}"

class Heroi(Personagem):
  def __init__(self, name, life, level, skill):
    super().__init__(name, life, level)
    self.__skill = skill
  
  def get_skill(self):
    return self.__skill
  
  def show_details(self):
    return f"{super().show_details()}\nTipo: {self.get_skill()}"

class Inimigo(Personagem):
  def __init__(self, name, life, level, type):
    super().__init__(name, life, level)
    self.__type = type
  
  def get_type(self):
    return self.__type
  
  def show_details(self):
    return f"{super().show_details()}\nTipo: {self.get_type()}"

heroi = Heroi(name='Pen Dragon', level="7", life="10", skill="Eclipse Solar")
print(heroi.show_details())
inimigo = Inimigo(name='Goblin', level="12", life="25", type="Humanoide")
print(inimigo.show_details())