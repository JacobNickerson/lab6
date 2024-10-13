def encode(password: str) -> str:
	"""
	Encodes a password

	This function accepts a numerical string password and encodes it by shifting each digit up by 3.

	Args:
		password: A numerical string representing a password

	Returns:
		encoded_password str:
			The password after being encoded

	Example:
	>>> encode("123456789")
	"456789012"
	"""
	encoded_password = ""
	for i in range(len(password)):
		digit = ord(password[i]) + 3 - ord('0')
		digit %= 10
		encoded_password += chr(digit + ord('0'))
	return encoded_password

def decode():  #TODO: Implement decoding function
    ...


def print_menu():
	"""
	Prints the password encoder/decoder menu
	"""
	print("""Menu
-------------
1. Encode
2. Decode
3. Quit""")

def main():
	raw_password = ""
	encoded_password = ""
	while True:
		print_menu()
		while True:
			try:
				user_input = input("Please enter an option: ").strip()
				break
			except ValueError:
				print("Error: Invalid selection")
		match user_input:
			case "1":
				while True:
					try:
						raw_password = input("Please enter your password to encode: ")
						int(raw_password)
						encoded_password = encode(raw_password)
						print("Your password has been encoded and stored!")
						break
					except ValueError:
						print("Error: Password contained invalid characters")
			case "2":
				if encoded_password == "":
					print("Error: No password stored!")
				else:
					print(f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.")  # TODO: Implement decode function
			case "3":
				return 0
			case _:
				print("Error: Invalid selection")
	
	
if __name__ == "__main__":
	main()
