import random
from PIL import Image



i = 0
while i < 50:
    number = random.randint(0, 255)
    number2 = random.randint(0, 250)
    number3 = random.randint(0, 250)
    img = Image.new("RGB", (600, 600), (number,number2,number3))
    img.save('randomimage/'+str(i)+'.jpg')
    i += 1
