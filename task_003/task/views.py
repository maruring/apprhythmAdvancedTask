from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image
from .main import delete_media_files, pred, change_img_name

def index(request):
    if request.method == 'POST':
        print('postメソッドです')
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            delete_media_files()
            form.save()
            pred()
            change_img_name()

        content = {
            'form': form
        }
        return render(request, 'index.html', content)

    else:
        print('GETメソッドです')
        form = ImageForm()
        content = {
            'form': form
        }
        return render(request, 'index.html', content)