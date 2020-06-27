"""
INPUT FORMAT:
python3 encrypt.py [input text file] [input image] [output image]




by Prabhat
3-2-3 to encode 1 byte
R-G-B
We take 2/3 LSB's of each colour and insert our message there

In all cases, we're just replacing last 3 characters so we can never exceed 255 or go below 0
Max ofset is +- 7 (4+2+1=7)
On average/in practice it is generally offest of ~3

If image is of x pixels (3 bytes -> 1 pixel)
You can encode exactly x/3 bytes

Assumption: All charcters to be encoded are from ASCII-128
The code works till 256 also, but just easier to seperate junk values (stop decryption process)
"""


def replace_last_2chars(num1,twobin):
	#binary of num1 gets last 2 chars of threebin
	#and we convert back to int and return the int
	binary_str = format(num1,'b')
	bin_str = '0'*(8-len(binary_str)) + binary_str
	ans_bin = bin_str[:6] + twobin
	ans_int = int("0b"+ans_bin,2)
	return ans_int


def replace_last_3chars(num1,threebin):
	#binary of num1 gets last 3 chars of threebin
	#and we convert back to int and return the int
	binary_str = format(num1,'b')
	bin_str = '0'*(8-len(binary_str)) + binary_str
	ans_bin = bin_str[:5] + threebin
	ans_int = int("0b"+ans_bin,2)
	return ans_int


def convertcharto323(char1):
	binary_str = format(ord(char1),'b')
	bin_str = '0'*(8-len(binary_str)) + binary_str
	output_list = [ bin_str[0:3], bin_str[3:5], bin_str[5:]]
	return output_list


def return_encrypted_matrix(matrix_RGB,plaintext):
	WIDTH = len(matrix_RGB)
	HEIGHT = len(matrix_RGB[20])

	ptr=0

	for i in range(HEIGHT):
		for j in range(WIDTH):
			list3bin = convertcharto323(plaintext[ptr])
			matrix_RGB[i][j][0] = replace_last_3chars(matrix_RGB[i][j][0], list3bin[0])
			matrix_RGB[i][j][1] = replace_last_2chars(matrix_RGB[i][j][1], list3bin[1])
			matrix_RGB[i][j][2] = replace_last_3chars(matrix_RGB[i][j][2], list3bin[2])

			ptr+=1
			perc = (i*WIDTH+j)*100/(len(plaintext))
			print( "Status: " + '{:4.2f}'.format(perc) + "%" , end="\r" )
			if(ptr == len(plaintext)):
				print()
				return matrix_RGB



def encrypt():
	matrix_RGB = imageio.imread(sys.argv[2]) #input image file
	WIDTH = len(matrix_RGB)
	HEIGHT = len(matrix_RGB[20])
	plaintext = open(sys.argv[1],'r').read() #input text file
	
	print("Plaintext: " + str(len(plaintext)) + " bytes")
	print("Image capacity: " + str(HEIGHT*WIDTH) + " bytes")

	if(len(plaintext)>HEIGHT*WIDTH):
		print("Thus, we cannot encrypt your message with the specified image")
		return

	print("encryption started")
	new_mat = return_encrypted_matrix(matrix_RGB,plaintext)
	imageio.imwrite(sys.argv[3], new_mat) #output image file
	print("encryption finished")



import imageio
import sys
import argparse

print("INPUT FORMAT: python3 encrypt.py [input text file] [input image] [output image]\n")

encrypt()
