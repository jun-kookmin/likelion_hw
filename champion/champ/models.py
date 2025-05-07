from django.db import models

# Create your models here.
class Line(models.Model):
    line = models.CharField(max_length=100)
    
class Champ(models.Model):
    name = models.CharField(max_length=100) 
    gender = models.CharField(max_length=10)
    role = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='sub_roles')
    position = models.ManyToManyField(Line, blank=True) # charfield로 구현할 경우 중복값 입력 불가능
    release_date = models.DateField() # 출시일 
    created_at = models.DateTimeField(auto_now_add=True)    
    updated_at = models.DateTimeField(auto_now=True) # 수정일자에는 auto_now 사용 수정 시 마다 시간 반영 
    