from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Event,Fotd,Ootd,Tag,Totd,Motd,Profile,Like_Fotd,Like_Ootd
from django.contrib.auth.models import User
from django.contrib import auth
import datetime
from django.contrib.auth.decorators import login_required
import calendar
from .calendar import Calendar_F,Calendar_M,Calendar_O,Calendar_T
from django.utils.safestring import mark_safe
from .forms import EventForm

# Create your views here.

def home_ootd(request):
    today = get_date(request.GET.get('month'))

    prev_month_var = prev_month(today)
    next_month_var = next_month(today)

    cal = Calendar_O(today.year, today.month)
    html_cal = cal.formatmonth(withyear=True)
    result_cal = mark_safe(html_cal)

    context = {'calendar' : result_cal, 'prev_month' : prev_month_var, 'next_month' : next_month_var}

    return render(request, 'ootd_home.html', context)

def home_fotd(request):
    today = get_date(request.GET.get('month'))

    prev_month_var = prev_month(today)
    next_month_var = next_month(today)

    cal = Calendar_F(today.year, today.month)
    html_cal = cal.formatmonth(withyear=True)
    result_cal = mark_safe(html_cal)

    context = {'calendar' : result_cal, 'prev_month' : prev_month_var, 'next_month' : next_month_var}

    return render(request, 'fotd_home.html', context)

def home_totd(request):
    today = get_date(request.GET.get('month'))

    prev_month_var = prev_month(today)
    next_month_var = next_month(today)

    cal = Calendar_T(today.year, today.month)
    html_cal = cal.formatmonth(withyear=True)
    result_cal = mark_safe(html_cal)

    context = {'calendar' : result_cal, 'prev_month' : prev_month_var, 'next_month' : next_month_var}

    return render(request, 'totd_home.html', context)


def home_motd(request):
    today = get_date(request.GET.get('month'))

    prev_month_var = prev_month(today)
    next_month_var = next_month(today)

    cal = Calendar_M(today.year, today.month)
    html_cal = cal.formatmonth(withyear=True)
    result_cal = mark_safe(html_cal)

    context = {'calendar' : result_cal, 'prev_month' : prev_month_var, 'next_month' : next_month_var}

    return render(request, 'motd_home.html', context)

#현재 달력을 보고 있는 시점의 시간을 반환
def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime.date(year, month, day=1)
    return datetime.datetime.today()

#현재 달력의 이전 달 URL 반환
def prev_month(day):
    first = day.replace(day=1)
    prev_month = first - datetime.timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

#현재 달력의 다음 달 URL 반환
def next_month(day):
    days_in_month = calendar.monthrange(day.year, day.month)[1]
    last = day.replace(day=days_in_month)
    next_month = last + datetime.timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

#새로운 Event의 등록 혹은 수정
def new(request, event_id=None):
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
    
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return redirect('calendar')
    return render(request, 'input.html', {'form': form})

def main_detail(request,year,month,day):
    fotds = Fotd.objects.filter(day__year=year, day__month = month, day__day=day)
    ootds = Ootd.objects.filter(day__year=year, day__month = month, day__day=day)
    motds = Motd.objects.filter(day__year=year, day__month = month, day__day=day)
    totds = Totd.objects.filter(day__year=year, day__month = month, day__day=day)
    return render(request, 'main_detail.html' , {'fotds':fotds,'ootds':ootds,'motds':motds,'totds':totds})

def new_fotd(request):
    
# def new_ootd():
# def new_motd():
# def new_totd():
# def detail_fotd():
# def detail_ootd():
# def detail_motd():
# def detail_totd():
# def edit_fotd():
# def edit_ootd():
# def edit_motd():
# def edit_totd():
# def delete_fotd():
# def delete_ootd():
# def delete_motd():
# def delete_totd():
