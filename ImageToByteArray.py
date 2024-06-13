from PIL import Image
import numpy as np

img = Image.open(input("Image Path: "))
with open('hahaballs.cpp', 'w+') as f:
	f.write('const unsigned char image[] = {\n\t')
	f.write(', '.join(f'0x{byte:02x}' for byte in np.array(img).tobytes()))
	f.write('\n};')