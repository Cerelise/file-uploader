from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import UploadForm

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action, api_view
from rest_framework.views import APIView

from .serializers import DocumentSerializer,MultipleDocSerializer
from .models import Document

# django原生
@csrf_exempt
# @ensure_csrf_cookie
def multiply_upload(request):
    if request.FILES:
        print(request.FILES)  # 检查上传的文件
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            documents = request.FILES.getlist('document')
            form.save_multiple(documents)

    return JsonResponse({'message': 'success'})


# Rest-Framework实现
class FilesViewSet(ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def create(self,request):
        serializer = MultipleDocSerializer(data=request.FILES or None)
        serializer.is_valid(raise_exception=True)
        files = serializer.validated_data.get("documents")
        file_list = []
        for file in files:
            file_list.append(Document(document=file))

        if file_list:
            Document.objects.bulk_create(file_list)

        return Response({'message':'success'})


