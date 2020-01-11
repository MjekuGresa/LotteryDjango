from django.shortcuts import render, redirect, HttpResponse
from ..user.models import User
from .models import Ticket
from ..winning_numbers import winning_nums
import datetime

now = datetime.datetime.now()

def index(request):
    global now
    day, hour, min = now.day, now.hour, now.min
    if day == 4 and hour == 20 and min == 0: #draw_day = Friday
        draw_day = True
    else:
        draw_day = False
    context = {
        'user': User.objects.get(id=request.session['user_id']), 
        'loop': range(1,40),
        'draw_day': draw_day
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
    global now
    day, hour, min = now.day, now.hour, now.min
    if day == 4 and hour == 20 and min == 0: #draw_day = Friday
        draw_day = True
        draw_numbers = winning_nums()
    else:
        draw_day = False
        draw_numbers = []

    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'tickets': Ticket.objects.order_by('-created_at'),
        'draw_day':  draw_day,
        'draw_numbers': draw_numbers,
        'draw_numbers_compare': sorted(draw_numbers),
        'result': False
    }
    if 'user_id' not in request.session:
        return redirect('user:index')
    return render(request, 'ticket/notification.html', context)

