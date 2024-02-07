from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def demo(request):
	return HttpResponse("Welcome to APSSDC Workshop")

def greet(sd,n):
	return HttpResponse(f"Hi Welcome {n}")

def stdnt(request,a,b,c="VVIT"):
	return HttpResponse(f"College Name: {c}<br/>Student Name: {a} <br>Student Age: {b}")

def ky(s):
	return HttpResponse("<h3>Welcome User</h3>")

def my(sd,n):
	return HttpResponse(f"<h1>hi <span style='color:red'>{n}</span></h1>")

def emp(t,es,en):
	# print(es,type(es))
	return HttpResponse("<style>#w{color:blue}</style><h2>Welcome <span style='color:red'>"+en+"</span></h2><h3>Salary: <span id='w'>"+str(es)+"</span></h3>")

def ry(self):
	return HttpResponse("<script>alert('Hi welcome');</script>")

def mg(self,m):
	return HttpResponse(f"<script>alert('hi {m}')</script>")

def student(self,sname,branch,year,rollNo):
	return HttpResponse(f"<script>alert('hi {sname}')</script>"+
		f'<table border="1"><tr><td>Name</td><td>{sname}</td><tr><td>Branch</td><td>{branch}</td></tr><tr><td>Year</td><td>{year}</td></tr><tr><td>RollNo</td><td>{rollNo}</td></tr></table>'
		)

def np(request):
	return render(request,'sample.html')

def fun(request,a):
	return render(request,'example.html',{'z':a})

def display(request,a,s,c,d):
	return render(request,'sample2.html',{'a':a,'b':s,'c':c,'d':d})

def dr(request):
	if request.method == "POST":
		a = request.POST['rn']
		b = request.POST['sn']
		c = request.POST['sy']
		d = request.POST['sb']
		return render(request,'stdata.html',{'x':a,'y':b,'z':c,'p':d})
	return render(request,'std.html')