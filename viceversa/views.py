from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	user_text = request.GET['usertext']
	reversed_text = user_text[::-1]
	
	# number = 0;
	# for symbol in user_text:
	# 	if (symbol.isspace()):
	# 		number = number + 1
	# print('number = ', number)

	words = user_text.split()
	number_of_words = len(words)

	return render(request, 'reverse.html', 
		{'userText':user_text, 'reversedText':reversed_text, 'numberOfWords':number_of_words})