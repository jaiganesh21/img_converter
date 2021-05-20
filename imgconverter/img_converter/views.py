import mimetypes
import os
from urllib.request import urlretrieve
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from PIL import Image

new_name = ""

# Create your views here.

def convert(request):
    context = {}
    return render(request, 'converter.html', context)

def upload_convert(request):
    global new_name
    context = {"upload": True}
    if request.method == "POST":
        try:
            file_value = request.FILES['file']
            file_newext = request.POST['slct2']
            file_currext = request.POST['slct']
            upload_save(file_value)
            context["file_data"] = [file_value, file_newext]
            context["status_msg"] = "File Upload Success !"
            c_status, new_name = convert_file(file_value, file_currext, file_newext)
            context["status_msg"] = c_status
            print(new_name)
            print("SUCCESS!!")

        except Exception as e:
            print("File Upload Failed !!")
            print("EX : ", e)

    return render(request, 'converter.html', context)

def upload_save(f):
    with open('static/upload/' + f.name, 'wb+') as destination: #write binary
        for chunk in f.chunks():
            destination.write(chunk)


def convert_file(file_var, fromext, toext):
    name = ""
    if toext == "jpeg":
        name = convertto_jpeg(file_var)
        return "Converted !!", name

    elif toext == "png":
        name = convertto_png(file_var)
        return "Converted !!", name

    elif toext == "gif":
        name = convertto_gif(file_var)
        return "Converted !!", name

    elif toext == "jpg":
        name = convertto_jpg(file_var)
        return "Converted !!", name

    elif toext == "tiff":
        name = convertto_tiff(file_var)
        return "Converted !!", name

    elif toext == "ico":
        name = convertto_ico(file_var)
        return "Converted !!", name

    elif toext == "bmp":
        name = convertto_bmp(file_var)
        return "Converted !!", name

    elif toext == "webp":
        name = convertto_webp(file_var)
        return "Converted !!", name

    else:
        return "Convertion Failed !!", name

def convertto_jpeg(file_var):
    curr_file = 'static/upload/' + file_var.name
    new_file = 'static/Converted/'
    Image.open(curr_file).convert('RGB').save(new_file + 'converted.jpeg')
    return 'converted.jpeg'

def convertto_png(file_var):
    curr_file = 'static/upload/' + file_var.name
    new_file = 'static/Converted/'
    Image.open(curr_file).convert('RGB').save(new_file + 'convert.png')
    return 'convert.png'

def convertto_gif(file_var):
    curr_file = 'static/upload/' + file_var.name
    new_file = 'static/Converted/'
    Image.open(curr_file).convert('RGB').save(new_file + 'img.gif')
    return 'img.gif'

def convertto_jpg(file_var):
    curr_file = 'static/upload/' + file_var.name
    new_file = 'static/Converted/'
    Image.open(curr_file).convert('RGB').save(new_file + 'convertable.jpg')
    return 'convertable.jpg'

def convertto_tiff(file_var):
    curr_file = 'static/upload/' + file_var.name
    new_file = 'static/Converted/'
    Image.open(curr_file).convert('RGB').save(new_file + 'x.tiff', format='TIFF', compression='tiff_lzw')
    return 'x.tiff'

def convertto_ico(file_var):
    curr_file = 'static/upload/' + file_var.name
    new_file = 'static/Converted/'
    Image.open(curr_file).convert('RGB').save(new_file + 'y.ico')
    return 'y.ico'

def convertto_bmp(file_var):
    curr_file = 'static/upload/' + file_var.name
    new_file = 'static/Converted/'
    Image.open(curr_file).convert('RGB').save(new_file + 'z.bmp')
    return 'z.bmp'

def convertto_webp(file_var):
    curr_file = 'static/upload/' + file_var.name
    new_file = 'static/Converted/'
    Image.open(curr_file).convert('RGB').save(new_file + 'xyz.webp')
    return 'xyz.webp'


def download_file(request):
    global new_name
    context = {}
    
    if new_name != "":
    

            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            filename = new_name
            filepath = BASE_DIR + '/static/Converted/' + filename

            image_buffer = open(filepath, "rb").read()

            mime_type, _ = mimetypes.guess_type(filepath)
            print(mime_type)

            # Set the return value of the HttpResponse
            response = HttpResponse(image_buffer, content_type=mime_type)
            # Set the HTTP header for sending to browser
            response['Content-Disposition'] = "attachment; filename=%s" % filename
            # Return the response value
            return response
            
    else:
        print("New Name Error !!")
        return render(request, 'converter.html', context)
    return render(request, 'converter.html', context)

    


