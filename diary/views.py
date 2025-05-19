from django.shortcuts import render,redirect
from .models import Entry
# Create your views here.
def home(request):
    return render(request,'home.html')
def getAllEntries(request):
    objs = Entry.objects.all().order_by('timestamp')
    context={
        'entries': objs
    }
    return render(request,'viewDiaryEntries.html',context=context)#context is used to pass data fro backend to frontend
def getIndividualEntry(request,id):
    context={}
    try:
        id = int(id)  # Attempt to convert the ID to an integer
    except ValueError:
        # If conversion fails, render the "not found" page
        context['entry'] = 'Invalid ID'
        return render(request, 'notFound.html', context)
    obj=Entry.objects.filter(id=id).first()
    if obj:
        context['entry']=obj
        return render(request,'diaryEntry.html',context)
    else:
        context['entry']='Invalid ID'
        return render(request,'notFound.html', context)
def AddEntry(request):
    if request.method == 'POST':
        heading = request.POST.get('heading')
        entry = request.POST.get('entry')
        obj = Entry.objects.create(header=heading,entry=entry)
        return redirect('/')
    return render(request,'Entry.html')
