color =  0xF0384E
red = (color >> 16)
print(red)
green = color >> 8 & 0xff
print(hex(green))
blue = color & 0xff
print(hex(blue))