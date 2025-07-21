from django.shortcuts import render,HttpResponse,redirect
from home.models import Register,CallRecording
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from datetime import datetime
# Create your views here.

def register(requests):
    if requests.method == 'POST':
        name = requests.POST.get('name')
        username = requests.POST.get('username')
        password = requests.POST.get('password')

        if Register.objects.filter(username=username).exists():
            return render(requests, 'register.html', {
                'error': "Username already exists"
            })

        try:
            validate_password(password)
        except ValidationError as e:
            return render(requests, 'register.html', {
                'error': e.messages[0]
            })

        register = Register(name=name, username=username, password=password)
        #print("Form submitted:", name, username)
        register.save()
        return redirect('homepage')

    return render(requests, 'register.html')


def log_in(requests):
    if requests.method == 'POST':
        username = requests.POST['username']
        password = requests.POST['password']
        
        try:
            user = Register.objects.get(username=username)

            if user.password == password:
                requests.session['user'] = username
                return redirect('homepage')
            else:
                return render(requests, 'log_in.html', {
                'error': "Username or password is incorrect"
            })

        except Register.DoesNotExist:
            return render(requests, 'log_in.html', {
                'error': "Username or password is incorrect"
            })
    
    return render(requests, 'log_in.html')

def homepage(requests):
    #return HttpResponse("this is about page")
    return render(requests,'homepage.html')

def upload_call(request):
    if 'user' not in request.session:
        return redirect('log_in')
        
    if request.method == 'POST':
        try:
            user = Register.objects.get(username=request.session['user'])
            recording = request.FILES['recording']
            
            # Validate file size (e.g., 50MB limit)
            if recording.size > 10 * 1024 * 1024:
                return render(request, 'homepage.html', {
                    'error': 'File too large (max 10MB)'
                })
            
            # Validate file type
            if not recording.name.lower().endswith(('.mp3', '.wav')):
                return render(request, 'homepage.html', {
                    'error': 'Only audio files (MP3, WAV) are allowed'
                })
            
            call = CallRecording.objects.create(
                user=user,
                audio_file=recording,
                upload_date=datetime.now(),
                #caller_number=request.POST.get('caller_number', ''),
                #status='PROCESSING'
            )

            return redirect('myuploads')
            
        except Exception as e:
            return render(request, 'homepage.html', {
                'error': f'Upload failed: {str(e)}'
            })
    
    return redirect('homepage')

def myuploads(requests):
    return render(requests,'myuploads.html')

def reports(requests):
    return HttpResponse("this is contacts page")