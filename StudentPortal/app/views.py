from django.shortcuts import redirect, render
from . forms import *
from youtubesearchpython import VideosSearch 

# import messages
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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


def register(request):
    form = UserRegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'app/register.html', context)
    # return render(request, 'app/register.html', {'form': form})
    

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!!")
            
            return redirect('home')
    else:
        form  = UserRegistrationForm()
    context = {
            'form': form
    }
    return render(request, 'app/register.html', context)

# def profile(request):
#     return render(request, 'app/profile.html')

def accueil(request):
    return render(request, 'app/accueil.html')

# def  RegisterForm(request):
#     form =  RegisterForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'app/register.html', context)