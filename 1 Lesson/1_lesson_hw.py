def strrrr():
	text = input("Введите слово а я проверю полиндром это или нет\n").replace(" ", "")

	if text == text[::-1]:
		print('True')
	else:
		print('False')


strrrr()
