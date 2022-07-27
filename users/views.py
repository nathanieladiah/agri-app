from django.contrib.auth import get_user_model
from django.shortcuts import render


User = get_user_model()

# @login_required
def dashboard(request):
	context = {}
	return render(request, 'users/dashboard.html', context)