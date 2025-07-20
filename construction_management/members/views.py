from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

from django.http import FileResponse

def download_pdf(request):
    # File path
    file_path = 'file.pdf'
    # Create the FileResponse object with the PDF file
    response = FileResponse(open(file_path, 'rb'))
    # Set the appropriate PDF headers
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = 'attachment; filename="myfile.pdf"'
    return response