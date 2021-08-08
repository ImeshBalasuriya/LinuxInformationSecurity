import hashlib
import sys

if __name__ == "__main__":

	#Make sure arguments are correct
	if (len(sys.argv) != 2):
		print(f"Usage:\n  {sys.argv[0]} <string>")
		sys.exit()

	#Generate Hash
	key = hashlib.pbkdf2_hmac('sha512', sys.argv[1].encode('utf-8'), b'Km5d5ivMy8iexuHcZrsD', 200000)

	#Print Hash
	print(key.hex())
