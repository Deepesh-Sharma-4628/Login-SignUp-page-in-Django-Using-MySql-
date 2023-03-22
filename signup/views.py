from django.shortcuts import render
import mysql.connector as sql  
from decouple import config
# Create your views here.
def signupaction(request):
    m=sql.connect(host='localhost',user='root',passwd=config('passwd'),database=config('database'))
    cursor=m.cursor()
    if request.method=="POST":
        fn=request.POST.get('first_name',' ')
        ln=request.POST.get('last_name',' ')
        sex=request.POST.get('sex',' ')
        em=request.POST.get('email',' ')
        pw=request.POST.get('password',' ')
        if fn and ln and sex and em and pw:
            c="insert into users values('{}' , '{}', '{}' , '{}','{}')".format(fn,ln,sex,em,pw)
            cursor.execute(c)
            m.commit()
    return render(request,'signup.html')