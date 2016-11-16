from PIL import Image, ImageDraw, ImageFont

cc = Image.open("C:\Users\cc332\Desktop\cc.jpg") #打开cc.jpg
ccfont = ImageFont.truetype("C:\Windows\Fonts\Arvo-Regular.ttf",30) #设置字体大小
draw = ImageDraw.Draw(cc)
draw.text((185, 0), "22", font=ccfont, fill=(255,0,0,255))

cc.save("cc_new.jpg")













