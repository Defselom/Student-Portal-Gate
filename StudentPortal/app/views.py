from django.shortcuts import redirect, render,HttpResponse
from . forms import *
from youtubesearchpython import VideosSearch 

# import messages
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    username = request.user.username
    
    return render(request, 'app/home.html', {'username': username})

@login_required
def cours(request):
    return render(request, 'app/cours.html')

@login_required
def hackathon(request):
    return render(request, 'app/hackathon.html')

def youtube(request):
    if request.method == "POST":
        form = youtubeform(request.POST)
        text = request.POST['text']
        video = VideosSearch(text, limit = 15)
        result_list = []
        for i in video.result()['result']:
            result_dict = {
                'input':text,
                'title':i['title'],
                'duration':i['duration'],
                'thumbnail':i['thumbnails'][0]['url'],
                'channel':i['channel']['name'],
                'link':i['link'],
                'views':i['viewCount']['short'],
                'published':i['publishedTime'],
            }
            desc = ""
            if i['descriptionSnippet']:
                for j in i['descriptionSnippet']:
                    desc += j['text']
            result_dict['description'] = desc
            result_list.append(result_dict)
            context = {
                'form':form,
                'results':result_list
                }
        
        return render(request,'app/youtube.html',context)
    else:
    
        # if form.is_valid():
        #     text = form.cleaned_data['text']
        #     print(text)
        form =  youtubeform()
    context = {'form':form}
    return render(request, 'app/youtube.html',context)

@login_required
def Dev_Club_community(request):
    return render(request, 'app/Dev_Club_community.html')


# def register(request):
#     form = UserRegistrationForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'app/register.html', context)
    # return render(request, 'app/register.html', {'form': form})
    

def registerPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
       
        if pass1!=pass2:
             #faire une page web dedier a ca. et utiliser render
            # return HttpResponse("Your password and confirm are not the same ")
            return render(request, 'app/401page.html')

        else: 
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('youtube')
    # return HttpResponse("User Created Succefull")
    # print(uname,email,pass1,pass2)
    return render(request, 'app/register.html')
        
    
        
        
    
        


def accueil(request):
    return render(request, 'app/accueil.html')

# def  RegisterForm(request):
#     form =  RegisterForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'app/register.html', context)

def loginPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(username=uname, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('accueil')
        else:
            #faire une page pour ca aussi
            return render(request, 'app/404page.html')
    return render(request, 'app/login.html')


def newbase(request):
    return render(request, 'app/newbase.html')




def about(request):
    return render(request, 'app/about.html')

def contact(request):
    return render(request, 'app/contact.html')