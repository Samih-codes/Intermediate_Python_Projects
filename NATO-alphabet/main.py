import pandas

nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic_dict = {row.letter:row.code for (index, row) in nato_data_frame.iterrows()}
print(nato_phonetic_dict)

while True:
	try:
		word = input("Enter a word: ").upper()
		output = [nato_phonetic_dict[letter] for letter in word]
		print(output)
	except KeyError:
		print("Sorry, we only accept letters from the alphabet")
