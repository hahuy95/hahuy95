from django.shortcuts import render
import os
# Create your views here.

os.chdir("static/images/portfolio")
current_dir = os.getcwd()

img = []
folders = []

for file_name in os.listdir(current_dir):
    folders.append(file_name)
    try:
        name = os.listdir(file_name)[0]
        path = f"{file_name}/{name}"
        img.append(path)
                
    except Exception as e:
        continue

def index(request):
    context = {
        "imgs": img,
        "folders": folders,
    }
    return render (request, 'index.html', context=context)

def folder(request, folderName):
    folder_dir = folderName
    filesName = []
    for file_name2 in os.listdir(folder_dir):
        filesName.append(file_name2)
    context = {
        "imgs": img,
        "folderName": folderName,
        "filesName": filesName,
    }
    return render(request, 'ProjectPage.html', context=context)
