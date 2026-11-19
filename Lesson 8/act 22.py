# magic (sparkle)
magic_word = str(input("Enter a word, sentence or smth lke that: "))
mw2 = ""

for i in magic_word:
	mw2 = i + mw2

print(f"The Original was {magic_word} \n but now we did sum magic and it is {mw2}!")
