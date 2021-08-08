import hashlib
import os, sys

if __name__ == "__main__":

	#Make sure arguments are correct
	if (len(sys.argv) != 2):
		print(f"Usage:\n  {sys.argv[0]} <string>")
		sys.exit()

	#Generate secure random salt
	salt = os.urandom(32)

	#Generate Hash
	key = hashlib.pbkdf2_hmac('sha512', sys.argv[1].encode('utf-8'), salt, 200000)

	#Print Hash
	print(key.hex())
