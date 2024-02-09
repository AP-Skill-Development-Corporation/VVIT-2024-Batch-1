from django.shortcuts import render,redirect
from .forms import UsregForm

# Create your views here.
def home(request):
	return render(request,'html/home.html')

def usregister(request):
	if request.method == "POST":
		t = UsregForm(request.POST)
		if t.is_valid():
			t.save()
			return redirect('/')	
	t = UsregForm()
	return render(request,'html/register.html',{'p':t})