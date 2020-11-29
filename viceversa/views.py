from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	user_text = request.GET['usertext']
	reversed_text = user_text[::-1]
	#print(reversed_text)
	return render(request, 'reverse.html', {'userText':user_text, 'reversedText':reversed_text})