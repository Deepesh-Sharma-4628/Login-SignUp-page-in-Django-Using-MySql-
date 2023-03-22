from django.shortcuts import render
import mysql.connector as sql
from django.http import HttpResponse
from decouple import config
# Create your views here.
def loginaction(request):
    m=sql.connect(host='localhost',user='root',passwd=config('passwd'),database=config('database'))
    cursor=m.cursor()
    if request.method=="POST":
        em=request.POST.get('email',' ')
        pw=request.POST.get('password',' ')
        if em and pw:
            c="select * from users where email='{}' and password='{}'".format(em,pw)
            cursor.execute(c)
            t=tuple(cursor.fetchall())
            if t==():
                return HttpResponse("<h1>Wrong Credentials</h1>")
            else:  return HttpResponse("<h1>Welcome!!</h1>")
    return render(request,'login.html')