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

#create an instance of the image object to allow for it to be used globally in functions and main loop
imageSize = 50
image = Image.open("./pigs/flying-pig-03.jpg").convert('RGB')
image = image.resize((imageSize,imageSize))

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
# Main loop 
###################################
background()
while True:
  for x in range(11):
    if x == 0:
      image = Image.open("./pigs/flying-pig-01.jpg").convert('RGB')
      image = image.resize((imageSize,imageSize))
    elif x == 1:
      image = Image.open("./pigs/flying-pig-03.jpg").convert('RGB')
      image = image.resize((imageSize,imageSize))
    elif x == 2:
      image = Image.open("./pigs/flying-pig-05.jpg").convert('RGB')
      image = image.resize((imageSize,imageSize))
    elif x == 3:
      image = Image.open("./pigs/flying-pig-07.jpg").convert('RGB')
      image = image.resize((imageSize,imageSize))
    elif x == 4:
      image = Image.open("./pigs/flying-pig-09.jpg").convert('RGB')
      image = image.resize((imageSize,imageSize))
    elif x == 5:
      image = Image.open("./pigs/flying-pig-11.jpg").convert('RGB')
      image = image.resize((imageSize,imageSize))
    elif x == 6:
      image = Image.open("./pigs/flying-pig-13.jpg").convert('RGB')
      image = image.resize((imageSize,imageSize))
    elif x == 7:
      image = Image.open("./pigs/flying-pig-15.jpg").convert('RGB')
      image = image.resize((imageSize,imageSize))
    elif x == 8:
      image = Image.open("./pigs/flying-pig-17.jpg").convert('RGB')
      image = image.resize((imageSize,imageSize))
    elif x == 9:
      image = Image.open("./pigs/flying-pig-19.jpg").convert('RGB')
      image = image.resize((imageSize,imageSize))
    elif x == 10:
      image = Image.open("./pigs/flying-pig-21.jpg").convert('RGB')
      image = image.resize((imageSize,imageSize))
    else:
      image = Image.open("./pigs/flying-pig-23.jpg").convert('RGB')
      image = image.resize((imageSize,imageSize))
    matrix.SetImage(image,0,0)
    sleep(.1)
  
try:
  print("Press CTRL-C to stop")
  while True:
    sleep(100)
except KeyboardInterrupt:
  exit(0)

