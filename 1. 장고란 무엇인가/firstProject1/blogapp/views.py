from django.shortcuts import render, redirect
from .forms import CreateBlog

# Create your views here.

def index(request):
    return render(request, 'index.html')

def blogMain(request):
    return render(request, 'blogMain.html')

def createBlog(request):
    form = CreateBlog()

    if request.method == 'POST':
        print("성공")
        form = CreateBlog(request.POST)

        if form.is_valid():
            print("1")
            form.save()
            return redirect('blogMain')

        else:
            print("2")
            return redirect('index')

    else:
        print("3")
        form = CreateBlog()
        return render(request, 'createBlog.html', {'form': form})

