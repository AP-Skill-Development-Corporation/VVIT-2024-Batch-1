from django.shortcuts import render,redirect
from .models import Student

# Create your views here.
def home(request):
	return render(request,'home.html')

def about(request):
	return render(request,'about.html')

def stdnt(request):
	m = Student.objects.all()
	if request.method == "POST":
		g = request.POST['a']
		k = request.POST['b']
		h = request.POST['c']
		t = Student(rn=g,sn=k,sy=h)
		t.save()
		return redirect('/std')
	return render(request,'stdt.html',{'s':m})

def stdup(request,k):
	c = Student.objects.get(id=k)
	if request.method == "POST":
		c.rn = request.POST['sa']
		c.sn = request.POST['sb']
		c.sy = request.POST['sc']
		c.save()
		return redirect('/std')
	return render(request,'stupd.html',{'v':c})

def stdlt(request,m):
	h = Student.objects.get(id=m)
	if request.method == "POST":
		h.delete()
		return redirect('/std')
	return render(request,'stdlte.html',{'y':h})

def emp(request):
	return render(request,'empy.html')




