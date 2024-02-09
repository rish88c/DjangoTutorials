from django.shortcuts import render
from django.views import View
from .forms import ContactForm
from django.http import HttpResponse
# Create your views here.

# def homefun(request):
#     return render(request,'school/school.html')

class HomeClassView(View):
    def get(self,request):
        return render(request, 'school/school.html')

############################
class AboutClassView(View):
    def get(self,request):
        context = {'msg':'Welcome TO GeekyShows'}
        return render(request,'school/about.html',context)
    

# def contactfun(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             nm = form.cleaned_data['name']
#             # Logging the name
#             # This will log the name to your console if you're running Django in development mode
#             print(nm)
#             # Returning an HttpResponse
#             return HttpResponse('Thank you, form submitted')
#     else:
#         form = ContactForm()
#     return render(request, 'school/contact.html', {'form': form})


class ContactClassView(View):
    def get(self,request):
        form = ContactForm()
        return render(request, 'school/contact.html', {'form': form})

    def post(self,request):
        form = ContactForm(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            print(nm)
            return HttpResponse('Thank you, form submitted')
