from django.shortcuts import render

# Create your views here.
def index_view(request):
	
	return render(request,'lightcontrol/index.html')

#def home_view(request):
	
#	return render(request,'lightcontrol/home.html')
