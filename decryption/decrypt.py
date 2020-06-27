"""
INPUT FORMAT:
python3 decrypt.py [output text file] [output image]



By Prabhat
"""


def convertRGBto1char(listRGB):
	#instead of 'b' put '0'
	#this guarantees atleast 3 length as 0b1 -> 001
	part1 = bin(listRGB[0])[-3:]
	part1 = part1.replace('b','0')

	part2 = bin(listRGB[1])[-2:]
	part2 = part2.replace('b','0')

	part3 = bin(listRGB[2])[-3:]
	part3 = part3.replace('b','0')

	bin_str = part1 + part2 + part3
	finalchar = chr( int("0b"+bin_str,2) )
	return finalchar


def decrypt():
	"""We cannot add % of decryption as we donot know the length of the plaintext
	"""
	matrix_RGB = imageio.imread(sys.argv[2])
	WIDTH = len(matrix_RGB)
	HEIGHT = len(matrix_RGB[20])
	print("decryption started")
	plaintext = ""

	for i in range(HEIGHT):
		for j in range(WIDTH):
			onechar = convertRGBto1char(matrix_RGB[i][j])
			print(onechar,ord(onechar))
			if(ord(onechar)>129 and ord(onechar)!=8216 and ord(onechar)!=8217): #for edge case: ’ ‘
				print("decryption finished")
				return plaintext
			plaintext += onechar


import imageio
import sys

print("INPUT FORMAT: python3 decrypt.py [output text file] [output image]\n")

plaintext1 = decrypt()
OutputTextFileObj = open(sys.argv[1],'w')
OutputTextFileObj.write(plaintext1)
