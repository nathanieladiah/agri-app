from django.shortcuts import render

# layer page
def layer_home(request):
	context = {}
	return render(request, 'layers/home.html', context)

# 