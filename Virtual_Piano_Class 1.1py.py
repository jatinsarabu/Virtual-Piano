import pygame
pygame.init()
class Piano_Key:
  def __init__(self,key,file_name,Channel_ID):
    self.key = key
    self.file_name = file_name
    self.Channel_ID = Channel_ID
  def play(self):
    file_play = pygame.mixer.Sound(self.file_name)
    pygame.mixer.Channel(self.Channel_ID).set_volume(1.05)
    pygame.mixer.Channel(self.Channel_ID).play(file_play)
  def stop(self):
    pygame.mixer.Channel(self.Channel_ID).fadeout(300)
def find_piano_key(piano_key):
  for character in keys:
      if character.key == piano_key:
        return character
keys = []
# a keys
keys.append(Piano_Key("escape", "converted_wav_notes/_a0.wav",0))
keys.append(Piano_Key("1","converted_wav_notes/_a1.wav",1))
keys.append(Piano_Key("2","converted_wav_notes/_a2.wav",2))
keys.append(Piano_Key("3", "converted_wav_notes/_a3.wav",3))
keys.append(Piano_Key("4","converted_wav_notes/_a4.wav",4))
keys.append(Piano_Key("5","converted_wav_notes/_a5.wav",5))
keys.append(Piano_Key("6","converted_wav_notes/_a6.wav",6))
keys.append(Piano_Key("7","converted_wav_notes/_a7.wav",7))
# a sharp keys
keys.append(Piano_Key("8", "converted_wav_notes/_a0sharp.wav",8))
keys.append(Piano_Key("9","converted_wav_notes/_a1sharp.wav",9))
keys.append(Piano_Key("0","converted_wav_notes/_a2sharp.wav",10))
keys.append(Piano_Key("-", "converted_wav_notes/_a3sharp.wav",11))
keys.append(Piano_Key("=","converted_wav_notes/_a4sharp.wav",12))
keys.append(Piano_Key("backspace","converted_wav_notes/_a5sharp.wav",13))
keys.append(Piano_Key("tab","converted_wav_notes/_a6sharp.wav",14))
keys.append(Piano_Key("q","converted_wav_notes/_a7sharp.wav",15))
# b keys
keys.append(Piano_Key("w", "converted_wav_notes/_b0.wav",16))
keys.append(Piano_Key("e","converted_wav_notes/_b1.wav",17))
keys.append(Piano_Key("r","converted_wav_notes/_b2.wav",18))
keys.append(Piano_Key("t", "converted_wav_notes/_b3.wav",19))
keys.append(Piano_Key("y","converted_wav_notes/_b4.wav",20))
keys.append(Piano_Key("u","converted_wav_notes/_b5.wav",21))
keys.append(Piano_Key("i","converted_wav_notes/_b6.wav",22))
keys.append(Piano_Key("o","converted_wav_notes/_b7.wav",23))
# c keys
keys.append(Piano_Key("[", "converted_wav_notes/_c1.wav",24))
keys.append(Piano_Key("]","converted_wav_notes/_c2.wav",25))
keys.append(Piano_Key("a","converted_wav_notes/_c3.wav",26))
keys.append(Piano_Key("s", "converted_wav_notes/_c4.wav",27))
keys.append(Piano_Key("d","converted_wav_notes/_c5.wav",28))
keys.append(Piano_Key("f","converted_wav_notes/_c6.wav",29))
keys.append(Piano_Key("g","converted_wav_notes/_c7.wav",30))
keys.append(Piano_Key("h","converted_wav_notes/_c8.wav",31))
# c sharp keys
keys.append(Piano_Key("j","converted_wav_notes/_c1sharp.wav",32))
keys.append(Piano_Key("k","converted_wav_notes/_c2sharp.wav",33))
keys.append(Piano_Key("l", "converted_wav_notes/_c3sharp.wav",34))
keys.append(Piano_Key(";","converted_wav_notes/_c4sharp.wav",35))
keys.append(Piano_Key("'","converted_wav_notes/_c5sharp.wav",36))
keys.append(Piano_Key("return","converted_wav_notes/_c6sharp.wav",37))
keys.append(Piano_Key("left shift","converted_wav_notes/_c7sharp.wav",38))
# d keys
keys.append(Piano_Key("z", "converted_wav_notes/_d1.wav",39))
keys.append(Piano_Key("x","converted_wav_notes/_d2.wav",40))
keys.append(Piano_Key("c","converted_wav_notes/_d3.wav",41))
keys.append(Piano_Key("v", "converted_wav_notes/_d4.wav",42))
keys.append(Piano_Key("b","converted_wav_notes/_d5.wav",43))
keys.append(Piano_Key("n","converted_wav_notes/_d6.wav",44))
keys.append(Piano_Key("m","converted_wav_notes/_d7.wav",45))
# d sharp keys
keys.append(Piano_Key(",","converted_wav_notes/_d1sharp.wav",46))
keys.append(Piano_Key(".","converted_wav_notes/_d2sharp.wav",47))
keys.append(Piano_Key("/", "converted_wav_notes/_d3sharp.wav",48))
keys.append(Piano_Key("p","converted_wav_notes/_d4sharp.wav",49))
keys.append(Piano_Key("P","converted_wav_notes/_d5sharp.wav",50))
keys.append(Piano_Key("right shift","converted_wav_notes/_d6sharp.wav",51))
keys.append(Piano_Key("left ctrl","converted_wav_notes/_d7sharp.wav",52))
# e notes
keys.append(Piano_Key("right ctrl", "converted_wav_notes/_e1.wav",53))
keys.append(Piano_Key("left alt","converted_wav_notes/_e2.wav",54))
keys.append(Piano_Key("right alt","converted_wav_notes/_e3.wav",55))
keys.append(Piano_Key("enter", "converted_wav_notes/_e4.wav",56))
keys.append(Piano_Key("space","converted_wav_notes/_e5.wav",57))
keys.append(Piano_Key("\\","converted_wav_notes/_e6.wav",58))
keys.append(Piano_Key("up","converted_wav_notes/_e7.wav",59))
# f notes
keys.append(Piano_Key("down", "converted_wav_notes/_f1.wav",60))
keys.append(Piano_Key("[7]","converted_wav_notes/_f2.wav",61))
keys.append(Piano_Key("left","converted_wav_notes/_f3.wav",62))
keys.append(Piano_Key("[1]", "converted_wav_notes/_f4.wav",63))
keys.append(Piano_Key("[2]","converted_wav_notes/_f5.wav",64))
keys.append(Piano_Key("[3]","converted_wav_notes/_f6.wav",65))
keys.append(Piano_Key("[4]","converted_wav_notes/_f7.wav",66))
# f sharp notes
keys.append(Piano_Key("[5]","converted_wav_notes/_f1sharp.wav",67))
keys.append(Piano_Key("[6]","converted_wav_notes/_f2sharp.wav",68))
keys.append(Piano_Key("right", "converted_wav_notes/_f3sharp.wav",69))
keys.append(Piano_Key("[8]","converted_wav_notes/_f4sharp.wav",70))
keys.append(Piano_Key("[9]","converted_wav_notes/_f5sharp.wav",71))
keys.append(Piano_Key("[0]","converted_wav_notes/_f6sharp.wav",72))
keys.append(Piano_Key("[.]","converted_wav_notes/_f7sharp.wav",73))
# g notes
keys.append(Piano_Key("[*]", "converted_wav_notes/_g1.wav",74))
keys.append(Piano_Key("[-]","converted_wav_notes/_g2.wav",75))
keys.append(Piano_Key("`","converted_wav_notes/_g3.wav",76))
keys.append(Piano_Key("[+]", "converted_wav_notes/_g4.wav",77))
keys.append(Piano_Key("[/]","converted_wav_notes/_g5.wav" , 78))
keys.append(Piano_Key("delete","converted_wav_notes/_g6.wav",79))
keys.append(Piano_Key("page up","converted_wav_notes/_g7.wav",80))
# g sharp notes
keys.append(Piano_Key("caps lock","converted_wav_notes/_g1sharp.wav",81))
keys.append(Piano_Key("print screen","converted_wav_notes/_g2sharp.wav",82))
keys.append(Piano_Key("end", "converted_wav_notes/_g3sharp.wav",83))
keys.append(Piano_Key("","converted_wav_notes/_g4sharp.wav",84))
keys.append(Piano_Key("page down","converted_wav_notes/_g5sharp.wav",85))
keys.append(Piano_Key("insert","converted_wav_notes/_g6sharp.wav",86))
keys.append(Piano_Key("home","converted_wav_notes/_g7sharp.wav",87))

win = pygame.display.set_mode((1300, 700))
pygame.mixer.set_num_channels(88)
#dpygame.display.set_caption("Virtual Piano by Jatin Sarabu")
#piano = pygame.image.load("piano 1.jpg")
#piano = pygame.transform.scale(piano,(1300,200))
#piano_x = 0
#piano_y = 500
#win.fill((255,255,255))
#win.blit(piano, (piano_x, piano_y))
pygame.display.update()
while True:
  try:
      pygame.event.pump()

      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          keyname = pygame.key.name(event.key)
          pressed_key = find_piano_key(keyname)
          pressed_key.play()
          pygame.display.update()
        if event.type == pygame.KEYUP:
          keyupname = pygame.key.name(event.key)
          released_key = find_piano_key(keyupname)
          released_key.stop()
          pygame.display.update()
  except KeyError:
    print("There is a key error")