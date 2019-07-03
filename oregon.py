# Used in main loop
from time import sleep
import random
import threading

###################################
# Graphics imports, constants and structures
###################################
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw

# this is the size of ONE of our matrixes. 
matrix_rows = 64
matrix_columns = 64 

# how many matrixes stacked horizontally and vertically 
matrix_horizontal = 1 
matrix_vertical = 1

total_rows = matrix_rows * matrix_vertical
total_columns = matrix_columns * matrix_horizontal

options = RGBMatrixOptions()
options.rows = matrix_rows 
options.cols = matrix_columns 
options.chain_length = matrix_horizontal
options.parallel = matrix_vertical 
options.hardware_mapping = 'adafruit-hat-pwm'  # If you have an Adafruit HAT: 'adafruit-hat'
#options.gpio_slowdown = 2

matrix = RGBMatrix(options = options)

image = Image.open("./oregon/OregonO_green.jpg").convert('RGB')
imageX = 0
imagey = 0
dirX = 0
dirY = 0


###################################
# Background
###################################
def background():
  temp_image = Image.new("RGB", (64,64))
  temp_draw = ImageDraw.Draw(temp_image)
  temp_draw.rectangle((0,0,64,64), fill= (255,255,255))
  matrix.SetImage(temp_image,0,0)

###################################
# newImage
###################################
def newImage():
  global image
  global imageX
  global imageY
  global dirX
  global dirY
  pickImage = random.randint(1,5)
  if pickImage == 1:
    image = Image.open("./oregon/Oregon.jpg").convert('RGB')
  elif pickImage == 2:
    image = Image.open("./oregon/OregonDuck.jpg").convert('RGB')
  elif pickImage == 3:
    image = Image.open("./oregon/OregonDuck2.jpg").convert('RGB')
  elif pickImage == 4:
    image = Image.open("./oregon/OregonO_green.jpg").convert('RGB')
  else:
    image = Image.open("./oregon/OregonO_yellow.jpg").convert('RGB')    
  
  #image = image.rotate(180)
  image = image.resize((40,40))
  imageX = random.randint(0,24)
  imageY = random.randint(0,24)
  dirX = random.randint(1,3)
  dirY = random.randint(1,3)

###################################
# Main loop 
###################################
background()
while True:
  #timer = threading.Timer(5.0,newImage)
  #timer.start()
  matrix.SetImage(image, imageX + dirX, imageY + dirY)
  sleep(.25)
  if ((imageX > 24) or (imageX < 0)):
    dirX = -dirX
  if ((imageY > 24) or (imageY < 0)):
    dirY = -dirY
    
  imageX = imageX + dirX
  imageY = imageY + dirY
  background()

try:
  print("Press CTRL-C to stop")
  while True:
    sleep(100)
except KeyboardInterrupt:
  exit(0)

