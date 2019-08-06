
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
matrix_horizontal = 5 
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

#imageSize = 90
#create an instance of the image object to allow for it to be used globally in functions and main loop
image = Image.open("./fullmatrix_5x3/welcomeToColorfulColorado.jpg").convert('RGB')
matrix.SetImage(image,0,0)
#image = image.resize((imageSize,imageSize))
backgroundColor = (255,255,255)


###################################
# create array of image names in folder
###################################

imageArray = ["boulderFlatirons1.jpg", "mountainLake.jpg", "fireOnTheMountain.jpg", "homeSweetHome4.jpg", "coloradoNeedlepoint.jpg","welcomeColorado.jpg", "flatirons2.jpg","welcomeToColorfulColorado.jpg","denverSkyline.jpg"]
imageArraySize = len(imageArray) 
print (imageArraySize)
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
#background()
while True:
  for i in range (imageArraySize):
    image = Image.open("./fullmatrix_5x3/{}".format(imageArray[i])).convert('RGB')
    sleep(3)
    matrix.SetImage(image,0,0)
  

try:
  print("Press CTRL-C to stop")
  while True:
    sleep(100)
except KeyboardInterrupt:
  exit(0)

