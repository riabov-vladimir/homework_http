def get_FR_text():
	with open('FR.txt', 'r', encoding='UTF-8') as file:
		return file.read()


def get_ES_text():
	with open('ES.txt', 'r', encoding='UTF-8') as file:
		return file.read()


def get_DE_text():
	with open('DE.txt', 'r', encoding='UTF-8') as file:
		return file.read()


print(get_ES_text())