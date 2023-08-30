from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

# Users model
from .models import User, UserImage

# Rest api add
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser

from django.http import FileResponse
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
from django.db.models import Q

from .serializers import UserSerializer, UserIdSerializer, UserImageSerializer, UserUploadImageSerializer
from .forms import UserForm, UserImageForm

import json

def index(request):
    return HttpResponse("hello world~~~~")

# user def add 2308231034

# showUserList
@api_view(["GET"])
def show_users(request):
    users = User.objects.order_by('-user_reg_date')
    
    #print('%y %m %d 테스트')
    
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            users = users.filter(
                Q(user_name__icontains=keyword)
            )
            serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

# showUser
@api_view(["GET"])
def show_user(request, user_id):
    user = User.objects.get(id=user_id)
    serializer = UserSerializer(user)
    return Response(serializer.data)
    #return Response(status=200)

# registerUser
@api_view(["POST"])
def register_user(request):
    # request post data form object
    # print("test-------")
    # print(request)
    # print(request.POST)
    print(request.data)
    
    form = UserForm(request.data)
    
    # form valid check
    if form.is_valid():
        # form valid -> DB insert
        user = form.save(commit=False)
        user.user_reg_date = timezone.now()
        user.save()
        print("테스트중: ",user.id)
        serializer = UserIdSerializer(user)
        return Response(serializer.data)
    
    # print("test--")
    # form invalid -> error response
    return Response(status=400)

# modifyUser
@api_view(["POST"])
def modify_user(request):
    
    # request post data form object
    form = UserForm(request.data)
    
    # form valid check
    if form.is_valid():
        user = User.objects.get(id=request.POST.get('id'))
        user.user_name = request.POST.get('user_name')
        user.user_age = request.POST.get('user_age')
        user.user_reg_date = timezone.now()
        user.save()
        return Response(status=200)
    
    # form invalid
    return Response(status=400)
     
# showUserImage
@api_view(['GET'])
@parser_classes([MultiPartParser, FormParser])
def show_user_image(request):
    
    #################
    image = UserImage.objects.filter(user_id=request.GET.get('user_id'))
    imageCount = image.count()
    
    if imageCount == 0 :
        image = None

    # 이미지가 있을시
    if image is not None:
        print(request.GET.get('user_id'))
        print(image.get().image_url)
        print(image.get().image_url.path)
        file_path = image.get().image_url.path
        fs = FileSystemStorage(file_path)
        return FileResponse(fs.open(file_path, 'rb'))
    
    # 이미지가 없을시
    return FileResponse(status=200)

# registerUserImage
@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def register_user_image(request):
    
    print(request.data)
    
    # axios로 받은 데이터 직렬화
    serializer = UserUploadImageSerializer(data=request.data)
    
    # 직렬화 한 데이터 유효성 검사
    if serializer.is_valid():
        imageFile = serializer.save()
        print("테스트중: ",imageFile.id)
        imageFile.image_reg_date = timezone.now()
        imageFile.save()
        print('파일이 정상적으로 등록됨.')
        return Response(status=200)
    
    print('파일형태가 이상해요')
    return Response(status=400)

####2222222