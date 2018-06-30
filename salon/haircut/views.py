from django.shortcuts import render

def home_page(request):

	if request.method == "GET":
			return render(request, 'haircut/home_page.html')
	if request.method == "POST":
			comment = request.POST.get("comment")
			username = request.POST.get("username")
			context = {'comment': comment, 'username': username}

			return render(request, 'haircut/home_page.html', context)

# Create your views here.
