from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from processing.forms import UploadForm
from processing.models import Video


class UploadFile(View):

    def get(self, request):
        return render(request, 'upload_file.html', {})

    def post(self, request):
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Video(upload=request.FILES['file'])
            instance.save()
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=422)
