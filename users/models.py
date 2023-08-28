from django.db import models
# Create your models here.

# date
from datetime import datetime
# uuid
import uuid

# user model add
# userName : 유저 이름
# userAge : 유저 나이
# userRegDate : 유저 등록일
class User(models.Model):
    user_name = models.CharField(max_length=50)
    user_age = models.DecimalField(max_digits=4, decimal_places=0)
    user_reg_date = models.DateTimeField()

# user image model add
# FK / user_id : 유저 외래키 
# uuid : 이미지 uuid 
# path : 이미지 경로

# jango에서 지원하는 필드로 구현이 가능한건가?
# image_url : 이미지 업로드 url
 
# imageRegDate : 이미지 등록일

# path uuid func
def upload_to(instance,filename):
    path = datetime.now().strftime('%y/%m/%d')
    
    uuid_file_name = uuid.uuid1()
    extension = filename.split('.')[1]

    filename_uuid = '{filename}.{extension}'.format(filename=uuid_file_name, extension=extension)
    return 'images/{path}/{filename}'.format(path=path,filename=filename_uuid)
    #return 'images/{filename}'.format(filename=filename)

class UserImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #uuid = models.UUIDField()
    #path = models.FilePathField()
    
    # file name fix -> uuid
    image_url = models.ImageField(upload_to=upload_to)
    
    # file name no fix
    #image_url = models.ImageField(upload_to='images/%y/%m/%d/')
    
    image_reg_date = models.DateTimeField(null=True)    
    