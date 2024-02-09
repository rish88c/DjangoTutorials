from django.shortcuts import render, HttpResponseRedirect,get_object_or_404
from .forms import StudentRegistration
from .models import User

#This function will add items and show it
def add_show(request):
    stud = User.objects.all()  # Move the definition outside of the if-else block
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()

    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud})


#this function will update and edit
def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk = id)
        fm  = StudentRegistration(request.POST,instance = pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk = id)
        fm  = StudentRegistration(instance = pi)
    return render(request,'enroll/updatestudent.html',{'form':fm})



#This function will delete
def delete_data(request,id):
    if request.method == 'POST':
        pi = get_object_or_404(User, pk=id)
        pi.delete()
        return HttpResponseRedirect('/')