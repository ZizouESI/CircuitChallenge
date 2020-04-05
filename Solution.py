#A solution for the "circuit" challenge by Zine-eddine fodil

def getKthBit(given_num,k):
	return (given_num & (1 << k)) >>k 
def encrypter(char,key):
	"""
		literally the given circuit  "bitwise OP maping" 
	"""
	cipher=0x0
	cipher |= (not (getKthBit(key,0) ^ (getKthBit(char,6) ^ getKthBit(char,1)))) << 0
	cipher |= (not (getKthBit(key,1) ^ (getKthBit(char,7) ^ getKthBit(char,0)))) << 1
	cipher |= (not (getKthBit(key,2) ^ (getKthBit(char,4) ^ getKthBit(char,3)))) << 2
	cipher |= (not (getKthBit(key,3) ^ (getKthBit(char,5) ^ getKthBit(char,2)))) << 3
	cipher |= (not (getKthBit(key,4) ^ getKthBit(char,5))) << 4
	cipher |= (not (getKthBit(key,5) ^ getKthBit(char,4))) << 5
	cipher |= (not (getKthBit(key,6) ^ getKthBit(char,7))) << 6
	cipher |= (not (getKthBit(key,7) ^ getKthBit(char,6))) << 7

	return cipher


def main():
	#reading the content of the file into a string variable and parse it to a list 
	file=open("./secret.enc","r")
	secret_string=file.read()
	secret_string_list=bytearray(secret_string,"windows-1252")
	file.close()	

	#now doing some brutforce to the KEY ^_^ :p 
	#we know that if XOR(P,key)=C then XOR(C,key)=P
	#in this case it is not really XOR only, but the function seems to be reversible 
	#"consider the number of inputs and outputs" so this is applicable
	plain_string_list=bytearray("","windows-1252")
	for key in range(256):
		for char in secret_string_list:
			plain_string_list.append(encrypter(char,key))

		plain_string=plain_string_list.decode("windows-1252")
		if "shellmates{" in plain_string :
			print("KEY :{0} , FLAG :{1}".format(key,plain_string))
			break
	

	

if __name__ == '__main__':
	main()