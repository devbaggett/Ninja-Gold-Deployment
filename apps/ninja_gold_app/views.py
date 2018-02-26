from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
	if 'activity' not in request.session:
		request.session['activity'] = ''

	if 'gold_score' not in request.session:
		request.session['gold_score'] = 0
	print request.session['activity']
	print type(request.session['gold_score'])
	return render(request, 'ninja_gold_app/index.html')

def gold(request):
	if request.POST['action'] == 'farm':
		request.session['number'] = random.randrange(10, 21)
		request.session['activity'] += '\n' + 'Earned {} gold from the the farm!'.format(request.session['number'])
		request.session['gold_score'] += request.session['number'] 
	elif request.POST['action'] == 'cave':
		request.session['number'] = random.randrange(5, 11)
		request.session['activity'] += '\n' + 'Earned {} gold from the the cave!'.format(request.session['number'])
		request.session['gold_score'] += request.session['number']
	elif request.POST['action'] == 'house':
		request.session['number'] = random.randrange(2, 6)
		request.session['activity'] += '\n' + 'Earned {} gold looting the house!'.format(request.session['number'])
		request.session['gold_score'] += request.session['number']
	elif request.POST['action'] == 'casino':
		request.session['number'] = random.randrange(0, 51)
		flip = random.randint(0, 1)
		# print flip
		if(flip == 1):
			request.session['activity'] += '\n' + 'You successfully stole {} gold from the the casino!'.format(request.session['number'])
			request.session['gold_score'] += request.session['number']	
		elif(flip == 0):
			request.session['activity'] += '\n' + 'Awww shucks! You lost {} gold playing dice in an alleyway with some crackheads. Still got your pants though!'.format(request.session['number'])
			request.session['gold_score'] -= request.session['number']
	return redirect('/')

def reset(request):
	request.session.pop('gold_score')
	request.session.pop('activity')
	return redirect('/')


