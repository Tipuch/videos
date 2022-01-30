from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class UploadFile(View):
    def get(self, request):
        return render(request, 'upload_file.html', {})

    def post(self, request):
        files = request.FILES
        return HttpResponse(200)
