from rest_framework import serializers
from .models import Task,User
from rest_framework import generics

class TaskSerializer(serializers.Serializer):
    #id:serializers.CharField()
    head=serializers.CharField()
    desc=serializers.CharField()

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=["id","head","desc"]
class TaskAddSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=[

            "head","desc","user"]

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["email","username","first_name","last_name","gender","occupation","phone_number"]
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def create(self, validated_data):
        user=User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name= validated_data['first_name'],
        last_name= validated_data['last_name'],
        gender= validated_data['gender'],
        occupation= validated_data['occupation'],
        phone_number= validated_data['phone_number'],
            password=validated_data['password'])
        return user

class TaskDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields="__all__"

class TaskCompletionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=["completed"]

class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    otp = serializers.IntegerField(write_only=True, required=False)
    class Meta:
        model=User
        fields=['email', 'username', 'first_name', 'last_name', 'gender', 'occupation', 'phone_number', 'otp','password1', 'password2']

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return data
    def create(self,validated_data):
        password1 = validated_data.pop('password1')
        password2 = validated_data.pop('password2')
        otp = validated_data.pop('otp', None)

        '''if validated_data['password1'] != validated_data['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
'''

        user=User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['last_name'],
            last_name=validated_data['last_name'],
            gender=validated_data['gender'],
            occupation=validated_data['occupation'],
            phone_number=validated_data['phone_number'],
           # password=validated_data['password1'],
            #password2=validated_data['password2'],
        )
        user.set_password(password1)
        if otp:
            user.otp = otp  # Set the OTP to the user object
        user.save()
        #return user
        #user.save()
        return user

class userProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email', 'username', 'first_name', 'last_name', 'gender', 'occupation', 'phone_number']

