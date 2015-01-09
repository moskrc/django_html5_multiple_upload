from django.shortcuts import render

from forms import UploadForm
from models import File


def index(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():

            for f in form.cleaned_data['files']:
                File.objects.create(file=f)
    else:
        form = UploadForm()

    uploaded_files = File.objects.all()

    return render(request, 'example/index.html', {'form': form, 'uploaded_files': uploaded_files})