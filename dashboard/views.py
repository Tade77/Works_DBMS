from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . forms import IssueForm, UserFeedBackForm
from . models import Issue, UserFeedback






@login_required(login_url='user-login')
def index(request):
    reports = Issue.objects.all()
    context = {
        'reports': reports
    }
    
    return render(request, "dashboard_template/index.html", context)
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


def issueFeedback(request):
    report = UserFeedback.objects.all()
    if request.method == 'POST':
        form = UserFeedBackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-index')
    else:
        form = UserFeedBackForm()
    context = {
        'report': report,
        'form': form,

        }
    
        
    return render(request, "dashboard_template/feedback.html", context)