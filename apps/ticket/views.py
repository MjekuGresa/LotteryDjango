from django.shortcuts import render, redirect, HttpResponse
from ..user.models import User
from .models import Ticket
from ..winning_numbers import *
import datetime
from datetime import date, timedelta
import ast

def week_range():
    week_start = date.today()
    week_start -= timedelta(days=week_start.weekday())
    week_end = week_start + timedelta(days=7)
    return week_start, week_end

def drawDay():
    draw_day = False
    now = datetime.datetime.now()
    day, hour = now.weekday(), now.hour
    if day == 6 and hour in range(10,15):
        draw_day = True
    return draw_day

def index(request):
    context = {
        'user': User.objects.get(id=request.session['user_id']), 
        'loop': range(1,40),
        'draw_day': drawDay()
    }
    if 'user_id' not in request.session:
        return redirect('user:index')
    return render(request, 'ticket/index.html', context)

def all(request):
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'tickets': Ticket.objects.order_by('-created_at'),
        'check_no_tickets':  Ticket.objects.filter(creator=request.session['user_id']).count()
    }
    if 'user_id' not in request.session:
        return redirect('user:index')
    return render(request, 'ticket/my_tickets.html', context)

def new(request):
    Ticket.objects.create_ticket(request.POST.getlist('numbers_selected'), request.session['user_id'])
    return redirect('ticket:all')

def notify(request):  
    week_start, week_end = week_range()
    tickets_weekly_char = ""
    tickets_weekly = []
    for ticket in Ticket.objects.filter(created_at__range=(week_start,week_end)):
        tickets_weekly_char += ticket.numbers_selected + ','
    
    #bad_chars = ["'"] 
    #for i in bad_chars : 
    #tickets_weekly_char = tickets_weekly_char.replace("'", '')
    tickets_weekly = ast.literal_eval(tickets_weekly_char.replace("'",''))  
    if drawDay():
        #draw_numbers = winning_nums()
        guessed_numbers = winning_ticket([1,3,5,7,9,11,13], tickets_weekly)
    else:
        #draw_numbers = []
        guessed_numbers = []

    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'tickets_weekly': Ticket.objects.filter(created_at__range=(week_start,week_end)),
        'draw_day':  drawDay(),
        'draw_numbers': [1,3,5,7,9,11,13],
        'guessed_numbers': guessed_numbers
    }
    if 'user_id' not in request.session:
        return redirect('user:index')
    return render(request, 'ticket/notification.html', context)

