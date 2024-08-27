from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . forms import IssueForm
from . models import Issue






@login_required(login_url='user-login')
def index(request):
    return render(request, "dashboard_template/index.html")
@login_required(login_url='user-login')
def issuePage(request):
    items = Issue.objects.all() #object relational model
    # items  = Product.objects.raw('SELECT * FROM dashboard_product')
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('dashboard-index')
    else:
        form = IssueForm() 
    context = {
        'items': items,
        'form': form,
    }
    return render(request, "dashboard_template/issue.html", context)
