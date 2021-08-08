import hashlib
import os, sys

if __name__ == "__main__":

	#Make sure arguments are correct
	if (len(sys.argv) != 2):
		print(f"Usage:\n  {sys.argv[0]} <string>")
		sys.exit()

	#Generate secure random salt
	salt = os.urandom(32)

	#Generate SHA512 Hash
	key = hashlib.sha512(salt + sys.argv[1].encode('utf-8'))

	#Print Hash
	print(key.hexdigest())
