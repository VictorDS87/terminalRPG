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
  
  def take_damage(self, damage):
     self.__life -= damage
     if self.__life < 0:
       self.__life = 0

  def attack(self, target):
    damage = self.__level * 2
    self.take_damage(damage)
    print(f"{self.get_name()} atacou {target.get_name()} e causou {damage} de dano!")

class Heroi(Personagem):
  def __init__(self, name, life, level, skill):
    super().__init__(name, life, level)
    self.__skill = skill
  
  def get_skill(self):
    return self.__skill
  
  def show_details(self):
    return f"{super().show_details()}\nTipo: {self.get_skill()}"
  
  def special_attack(self, target):
    damage = self.get_level() * 5 # Dano aumentado
    target.take_damage(damage)
    print(f"{self.get_name()} usou a habilidade especial {self.get_skill()} em {target.get_name()} e causou {damage} de dano!")


class Inimigo(Personagem):
  def __init__(self, name, life, level, type):
    super().__init__(name, life, level)
    self.__type = type
  
  def get_type(self):
    return self.__type
  
  def show_details(self):
    return f"{super().show_details()}\nTipo: {self.get_type()}"

class Jogo:
  """ Classe orquestradora do jogo """
 
  def __init__(self):
    self.heroi = Heroi(name="Herói", life=100, level=5, skill="Super Força")
    self.inimigo = Inimigo(name="Morcego", life=50, level=3, type="Voador")

  def iniciar_batalha(self):
    """ Fazer a gestão da batalha em turnos """
    print("Iniciando batalha!")
    while self.heroi.get_life() > 0 and self.inimigo.get_life() > 0:
      print("\nDetalhes dos Personagens:")
      print(self.heroi.show_details())
      print(self.inimigo.show_details())

      input("Pressione Enter para atacar...")
      escolha = input("Escolha (1 - Ataque Normal, 2 - Ataque Especial): ")

      if escolha == '1':
        self.heroi.attack(self.inimigo)
      elif escolha == '2':
        self.heroi.special_attack(self.inimigo)
      else:
        print("Escolha inválida. Escolha novamente.")

      if self.heroi.get_life() > 0:
        # Inimigo ataca o heroi
        self.inimigo.attack(self.heroi)

      if self.heroi.get_life() > 0:
        print("\nParabéns você venceu a batalha!")
      else:
        print("\nVocê foi derrotado!")
 
# Criar instância do jogo e iniciar batalha
jogo = Jogo()
jogo.iniciar_batalha()