from django.http import HttpResponse
from django.shortcuts import render
from .mechanism import start_process
import os

# Create your views here.
def index(request):
    return render(request, 'app/index.html')


def submit(request):
    if request.method == "POST":
        directory = request.POST['dir_path']
        
        start_process(directory)
            
        return render(request, 'app/index.html', {'rtd': True})
    
    return render(request, 'app/index.html', {'rtd': False})

def download_excel(request):
    output_excel_path = "output.xlsx" 
    with open(output_excel_path, 'rb') as excel_file:
        response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="output.xlsx"'
    os.remove(output_excel_path)
    return response