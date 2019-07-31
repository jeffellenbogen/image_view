
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

imageSize = 80
angle = 0

#create an instance of the image object to allow for it to be used globally in functions and main loop
image = Image.open("./logos/RedHotChiliPeppers.png").convert('RGB')
image = image.resize((imageSize,imageSize))
backgroundColor = (0,0,0)

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
  matrix.SetImage(image,(total_columns - imageSize)/2,(total_rows - imageSize)/2)
  sleep(.05)


try:
  print("Press CTRL-C to stop")
  while True:
    sleep(100)
except KeyboardInterrupt:
  exit(0)

