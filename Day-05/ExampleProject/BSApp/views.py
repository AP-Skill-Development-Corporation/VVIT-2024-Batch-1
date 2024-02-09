from django.shortcuts import render,redirect
from .models import Student,Employee
from .forms import EmForm
from django.contrib import messages

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
	u = Employee.objects.all()
	if request.method == "POST":
		r = EmForm(request.POST)
		if r.is_valid():
			r.save()
			messages.success(request,"Employee Created Successfully")
			return redirect('/empl')
	r = EmForm()
	return render(request,'empy.html',{'d':r,'ud':u})

def emupd(request,z):
	a = Employee.objects.get(id=z)
	if request.method == "POST":
		n = EmForm(request.POST,instance=a)
		if n.is_valid():
			n.save()
			messages.info(request,"Employee Data Updated Successfully")
			return redirect('/empl')
	n = EmForm(instance=a)
	return render(request,'emupdate.html',{'b':n})

def emdt(request,d):
	p = Employee.objects.get(id=d)
	if request.method == "POST":
		p.delete()
		messages.warning(request,"Employee record deleted Successfully")
		return redirect('/empl')
	return render(request,'emdt.html',{'e':p})

