from rest_framework import serializers
from .models import AddStudent

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=50)
    number=serializers.IntegerField()
    address=serializers.CharField(max_length=50)
    
class AddStudentSerializer(serializers.Serializer):
    
    # Validators:
    # def start_with_r(value):
    #     if value[0].lower()!='r':
    #         raise serializers.ValidationError("Name Should Start with R..")

    name=serializers.CharField(max_length=50) # if want to use validators put in name field validators=[start_with_r]
    num=serializers.IntegerField()
    city=serializers.CharField(max_length=50)
    pin_code=serializers.IntegerField()
    
    def create(self,validated_data):
        return AddStudent.objects.create(**validated_data)
  
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.city=validated_data.get('city',instance.city)
        instance.num=validated_data.get('num',instance.num)
        instance.pin_code=validated_data.get('pin_code',instance.pin_code)
        instance.save()
        return instance
    
    # Field Level validation:
    def validate_num(self, value):
        count=0
        while(value>0):
            count=count+1
            value=value//10
        if(count>10):
            raise serializers.ValidationError('Number Should be 10 Digit')
        return value
    
    # Object level validation:
      
    # def validate(self, data):
    #     nm=data.get('name')
    #     ct=data.get('city')
    #     if nm.lower()=='robbin' and ct.lower()!='dubai':
    #         raise serializers.ValidationError('Should Leave in Dubai..')   
    #     return data 
    
        
    