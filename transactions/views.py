from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return redirect('transactions:dashboard')
    context = {}
    return render(request, "transactions/index.html", context)

class dashboard(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        context={}
        return render(request, "transactions/dashboard.html",context)