from django.shortcuts import render
from djang0.contrib.auth.decorators import login_required


# Create dashboard
@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')
