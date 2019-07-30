
# Used in main loop
from time import sleep
import random
import time

###################################
# Graphics imports, constants and structures
###################################
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw

# this is the size of ONE of our matrixes. 
matrix_rows = 32 
matrix_columns = 32 

# how many matrixes stacked horizontally and vertically 
matrix_horizontal = 4 
matrix_vertical = 3 

total_rows = matrix_rows * matrix_vertical
total_columns = matrix_columns * matrix_horizontal

options = RGBMatrixOptions()
options.rows = matrix_rows 
options.cols = matrix_columns 
options.chain_length = matrix_horizontal
options.parallel = matrix_vertical 

#options.hardware_mapping = 'adafruit-hat-pwm' 
#options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
options.hardware_mapping = 'regular'  

options.gpio_slowdown = 2

matrix = RGBMatrix(options = options)

imageSize = 50
#create an instance of the image object to allow for it to be used globally in functions and main loop
image = Image.open("./avengers/ironman.jpg").convert('RGB')
image = image.resize((imageSize,imageSize))
backgroundColor = (255,255,255)

###################################
# Background
###################################
def background():
  global backgroundColor
  temp_image = Image.new("RGB", (total_columns - 1,total_rows - 1))
  temp_draw = ImageDraw.Draw(temp_image)
  temp_draw.rectangle((0,0,total_columns,total_rows), fill= backgroundColor)
  matrix.SetImage(temp_image,0,0)


###################################
# Image Setup
###################################
def newImage():
  # used global keyword here to access the object image in the main loop
  global image
  pickImage = random.randint(1,4)
  if pickImage == 1:
    image = Image.open("./avengers/ironman.jpg").convert('RGB')
    image = image.resize((imageSize,imageSize))
  elif pickImage == 2:
    image = Image.open("./avengers/hulk.jpg").convert('RGB')
    image = image.resize((imageSize,imageSize))
  elif pickImage == 3:
    image = Image.open("./avengers/spiderman.jpg").convert('RGB')  
    image = image.resize((imageSize,imageSize))
  else:
    image = Image.open("./avengers/captain.jpg").convert('RGB')
    image = image.resize((imageSize,imageSize))
  


###################################
# Main loop 
###################################
background()
while True:
  matrix.SetImage(image,0,0)
  sleep(3)
  newImage()

try:
  print("Press CTRL-C to stop")
  while True:
    sleep(100)
except KeyboardInterrupt:
  exit(0)

