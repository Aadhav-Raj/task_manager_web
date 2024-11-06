import datetime

from django.contrib.auth import authenticate
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task,User
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from sms import send_sms
from .forms import AddTaskForm
from . import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
@api_view(['GET'])
@permission_classes([AllowAny])
def ListTasks(request):
    """task=Task.objects.all()
    id=Task.objects.filter()
    task_serializer=TaskSerializer(task,many=True)
    return Response(task_serializer.data)"""
    api=request.headers.get("Authorization")
    print("Api : ",api)
    task=Task.objects.filter(completed=False,user=request.user)
    #task=Task.objects.all()
    task_serializer=serializers.TaskListSerializer(task,many=True)
    return Response(task_serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def ListTasks2(request):
    """task=Task.objects.all()
    id=Task.objects.filter()
    task_serializer=TaskSerializer(task,many=True)
    return Response(task_serializer.data)"""

    #task1=Task.objects.filter(completed=False)
    task2=Task.objects.filter(completed=True)
    #task_serializer1=serializers.TaskListSerializer(task1,many=True)
    task_serializer2=serializers.TaskListSerializer(task2,many=True)
    #data={"pending": task_serializer1.data, "completed": task_serializer2.data}
    #data=[[task_serializer1],[task_serializer2]]
    #data={task_serializer1.data, task_serializer2.data}
    return Response(task_serializer2.data,status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def AddTask(request):
    #task_head=request.POST.get('head')
    #task_desc=request.POST.get('desc')
    #task=Task(head="",desc="")
    #if  not  task_desc or  not task_desc:
     #   return Response({'error': 'Head and description are required. {}'.format()}, status=status.HTTP_400_BAD_REQUEST)


    #task={"head":task_head,"desc":task_desc}
    serializer=serializers.TaskAddSerializer(data=request.data)


    if serializer.is_valid():
        #task=serializer.save()
        task = serializer.save(user=request.user)
        return Response({"id":task.id},status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@api_view(['PATCH'])
def complete(request,pk):
    task=Task.objects.get(id=pk)
    task.completed=(not task.completed)
    task.save()
    serializer=serializers.TaskCompletionSerializer(task)
    return Response(task.id,status=status.HTTP_200_OK)


@api_view(['POST'])
@csrf_exempt
def createUser(request):
    serializer=serializers.UserSerializer(data=request.data)
    if serializer.is_valid():
       """ user=User.objects.create_user(
            serializer.init_data['email'],
            serializer.init_data['username'],
            serializer.init_data['password']
        )"""

       rand=random.randint(100000,999999)

       user=serializer.save(otp=rand)
       if False:
           return JsonResponse({
               "message":"Success"
           },status=status.HTTP_201_CREATED)
       else:
           payload={
               'email':user.email,
               "exp":datetime.datetime.utcnow()+datetime.timedelta(days=2),
               "user_id":user.pk
           }

           #html=create_html_template(payload)
           html=create_html_template(rand)
           send_mail(
               "Yov "+user.username,#"Email verification",
               "",
               settings.EMAIL_HOST_USER,
               [user.email],
               html_message=html
           )
           print("Mail sent to "+user.email)
           return JsonResponse({
               "message":"Success",
               "id":int(user.pk)
           },status=status.HTTP_201_CREATED)
           #return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
        return JsonResponse({
            "message": "Failure",
        },status=status.HTTP_400_BAD_REQUEST)
        #Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
import jwt
from cryptography import fernet
#key=fernet.Fernet.generate_key()
cipher_suite=fernet.Fernet(settings.FERNET_KEY)
import random
def create_html_template(payload):
    #token=jwt.encode(payload,"qwerty",algorithm='HS256')
    #encrypted_token=cipher_suite.encrypt(token.encode()).decode()
    html_upper='''
    <!DOCTYPE html>
    <html>
    <head>
    <style>
            .button {
                display: inline-block;
                padding: 10px 20px;
                color: #fff;
                background-color: #007bff;
                text-decoration: none;
                border-radius: 5px;
            }
            .footer {
                margin-top: 20px;
            }
        </style>
        </head>
    '''
    #< h4 > Email verification < / h4 >
    html_lower='''
<h4>Vanakkam di mapla </h4>
<body>


<p>Here's the otp</p>

<p>__otp__</p>

<br>
<br>
<a href="http://192.168.58.119:8000/api/authentication/?token=__token__" class="button">Verify Email</a>
<br>


<p>Thank you for joining Task Manager</p>
<p>If you did not signup for this account ,please  ignore this email </p>
</div>

</body>
</html>
'''
   # return html_upper+html_lower.replace('__token__',encrypted_token)
    return html_upper+html_lower.replace('__otp__',str(payload))
from django.core.exceptions import ObjectDoesNotExist


@api_view()
@api_view(['GET'])
@csrf_exempt
@permission_classes([AllowAny])
def verify_email(request):
        enc_token=request.GET.get('token')
    #try:
        decrypt_token=cipher_suite.decrypt(enc_token.encode()).decode()
        payloadd=jwt.decode(decrypt_token,"qwerty",algorithms=['HS256'])
        pkk = payloadd["user_id"]
      #  print("verified is called")
        uu=User.objects.get(pk=pkk)
        uu.email_verified=True
        uu.save()
        print("Verified is called -- "+str(pkk)+" -- "+str(uu) +" -- "+str(uu.email_verified))
        return JsonResponse({
            "message":"success",
            "id":uu.pk
        }, status=201)
        """
        
        
        {
    "email": "technical.aadhav.raj@gmail.com",
    "username": "Tech_Raj",
    "first_name": "Tech",
    "last_name": "Raj",
    "gender": "MALE",
    "occupation": "STUDENT",
    "phone_number": "7904367287",
    "password1": "Qwerty@123",
    "password2": "Qwerty@123"
}
"""

        '''
        if pk:
            #Payload=payloadd['payload']
            user_profile=User.objects.get(id=pk)
            user_profile.email_verified=True
            print(user_profile.email + "Verified Successfully")
            user_profile.save()

            return JsonResponse({
                        'mssg':"Email verification  Successful...",
                        'status':True,
                        'user':user_profile
                    },
                    status=201)
    except jwt.ExpiredSignatureError:
        return JsonResponse({'msg': 'Token has expired.', 'status': False,"w":1}, status=400)
    except jwt.InvalidTokenError:
        return JsonResponse({'msg': 'Invalid token.', 'status': False,"w":2}, status=400)
    except ObjectDoesNotExist:
        return JsonResponse({'msg': 'User not found.', 'status': False,"w":3}, status=404)
    except Exception as e:
        return JsonResponse({'msg': str(e), 'status': False,"w":4}, status=500)
        '''


import smtplib
from email.mime.text import MIMEText
import random

@api_view(['POST'])
@permission_classes([AllowAny])
def verify_otp(request):
    if request.method=='POST':

        id=request.data.get("id")
        otp=request.data.get("otp")
        user=User.objects.get(pk=id)
        if int(user.otp)==int(otp):
            user.email_verified = True
            user.save()
            return JsonResponse({
                "message":"Success"
            },status=status.HTTP_200_OK)
        else:
            return JsonResponse({
                "message": "Invalid OTP"
            }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    if request.method == 'POST':
        try:
            #username = request.data.get('username')
            email = request.data.get('email')
            password = request.data.get('password')
            print(f"email : {email} \n password : {password}",format(email,password))
        except  :
            print("exception")

        """user = None
        if email and '@' in email:
            try:
                user = User.objects.get(email=email,password=password)
                print("email")
            except ObjectDoesNotExist:
                pass

        #if not user:
        else:
            user = authenticate(username=username, password=password)
            print("username")
"""
        if email is None or password is None:
            return Response({'error': 'Please provide both email and password'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(email=email, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            '''send_mail(
                f"Hey {user.username}, ",
                "You Logged into Task Manager",
                settings.EMAIL_HOST_USER,
                [user.email]
            )'''

            '''
            
        'att': '@txt.att.net',
    'verizon': '@vtext.com',
    't-mobile': '@tmomail.net',
    'sprint': '@messaging.sprintpcs.com',
    '''


            return Response({'token': token.key}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    #if request.method == 'POST':
        try:
            # Delete the user's token to logout
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

from rest_framework.permissions import AllowAny
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    if request.method=="GET":
        email=request.GET.get("email")
        password=request.GET.get("password")
        api=request.headers.get("Authorization")
        print(email,"--",password,"--",api)
        #user=User.objects.filter(username=username,password=password)
        #serializer=serializers.userProfileSerializer(user)
        #return Response(serializer.data,status=status.HTTP_200_OK)
        user = authenticate(email=email, password=password)

        if user:
            serializer = serializers.userProfileSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



    if request.method == "POST":
        email = request.data.get("email")
        password = request.data.get("password")

        if email is None or password is None:
            return Response({'error': 'Please provide both email and password'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(email=email, password=password)

        if user:
            serializer = serializers.userProfileSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

