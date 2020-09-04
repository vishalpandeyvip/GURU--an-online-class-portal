from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse
from django.db.models import *

from basic.models import *
from basic.views import member_check
from .forms import *
from .models import *

def filter_fun(key):
	return key!=""

@login_required
def home(request,unique_id):
	classroom = Classroom.objects.get(unique_id=unique_id)
	if member_check(request.usermclassroom):
		polls = Poll.objects.all()

		#handling forms of poll and its choice
		if request.method=='POST':
			form = QuestionForm(request.POST or None)
			choice_list = request.POST.getlist('check')
			choice_list = list(filter(filter_fun,choice_list))

			if form.is_valid():
				form = form.save(commit=False)
				form.classroom = classroom
				form.announce_at = request.POST.get('date')
				form.created_by = request.user
				form.save()

				for i in choice_list:
					choice=Choice()
					choice.poll = Poll.objects.get(id=form.id)
					choice.choice_text = i
					choice.save()
				return redirect(reverse('home'))
		else:
			form = QuestionForm()
		params = {
			'pollform':form,
			'polls':polls,
			'classroom':classroom
			}
		return render(request,'poll/form.html',params)

def poll_page(request,unique_id, poll_id):
	classroom = Classroom.objects.get(unique_id = unique_id)
	if member_check(request.user,classroom):

		#poll list and voting page.
		poll = Poll.objects.get(id=poll_id)
		choices = Choice.objects.all().filter(poll=poll)
		message = winner = None
		if poll.voters.filter(username=request.user.username).exists():
			message = 'You have already voted !!!!'
			choices = choices.order_by('-votes')
			winner = Choice.objects.aggregate(Max('votes'))
		params = {
			'details':poll.poll_details,
			'choices' : choices,
			'poll':poll,
			'classroom':classroom,
			'message':message,
			'winner':choices.first()
		}
		return render(request,'poll/poll_page.html',params)

def voting(request,unique_id,poll_id,choice_id):
	if member_check(request.user,classroom):
		message = None
		poll=Poll.objects.get(id=poll_id)
		choice = Choice.objects.all().filter(poll=poll)
		classroom = Classroom.objects.get(unique_id = unique_id)
		if not poll.voters.filter(username=request.user.username).exists():
			choice=Choice.objects.get(id=choice_id)
			choice.votes += 1
			poll.voters.add(request.user)
			choice.save()
			return redirect(f'/polls/{unique_id}')
		else:
			message = 'You have already voted !!!!'
		params = {
			'poll':poll,
			'choices' : choice,
			'message': message,
			'classroom':classroom
		}
		return render(request,'poll/poll_page.html',params)



