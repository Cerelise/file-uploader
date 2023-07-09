from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import UploadForm

# Create your views here.


@csrf_exempt
def multiply_upload(request):
    if request.FILES:
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            documents = request.FILES.getlist('document')
            form.save_multiple(documents)

    return JsonResponse({'message': 'success'})