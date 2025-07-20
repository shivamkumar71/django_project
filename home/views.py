from django.shortcuts import render , redirect
import requests , os, requests
from django.contrib import messages
from django.conf import settings

# from .models import Contact

import datetime
# from datetime import datetime
from django.http import HttpResponse
from home.models import Contact
from django.contrib.auth.models import User
from .forms import RegistrationForm


# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is home page")

# Example view
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("its about page")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("its services page")




# ...existing code...
def search_files(request):
    query = request.GET.get('query', '').lower()  # Get search query
    results = []  # Store matching files

    if query:
        folder_path = os.path.join(settings.BASE_DIR, 'hello', 'static')  # Folder where files are stored
        for file_name in os.listdir(folder_path):
            if query in file_name.lower():
               results.append({'name': file_name,'url': '/static/' + file_name})

    return render(request, 'search_results.html', {'query': query, 'results': results})




def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # date_time = datetime.now()
        
        # contact = Contact(name=name, email=email, phone=phone, message = message, date = date_time)
        # contact.save()
      
        

        # Redirect to avoid resubmission on refresh
       

        # ✅ Get current date and time
        now = datetime.datetime.now()
        formatted_datetime = now.strftime("%d-%m-%y / %I:%M:%S %p")

        # ✅ Set file path
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(BASE_DIR, 'hello', 'contact_data.txt')

        # ✅ Save contact data with date & time
        with open(file_path, 'a', encoding='utf-8') as f:
           
            f.write(f"Date-Time: {formatted_datetime}\n")
            f.write(f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}\n")
            f.write("---------------------------------\n")
           
   
    return render(request, 'contact.html')


  
    

def index(request):
    access_key = "ZaPFNltWwLFFAAS7bH17wQn6hEh58Wn8nuXAk5qFQKg"
    query = "nature"
    url = f"https://api.unsplash.com/search/photos?query={query}&client_id={access_key}&per_page=8"
    response = requests.get(url)
    data = response.json()
    images = data.get('results', [])
    return render(request, 'index.html', {'images': images})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegistrationForm()
    return render(request, 'createaccount.html', {'form': form})