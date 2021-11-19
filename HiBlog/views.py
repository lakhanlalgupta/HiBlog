from django.shortcuts import render,redirect, HttpResponse
from django.core.exceptions import SuspiciousOperation
from .models import Data, NewSubjects, User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
def home(request):
	subjects = NewSubjects.objects.all()
	subject_id = request.GET.get('subject')
	single_subject_new = {}
	if subject_id:
		single_subject = Data.objects.filter(subject=int(subject_id))
		subject_name = NewSubjects.objects.get(id=int(subject_id))
		single_subject_new = {}
		for i in single_subject:
			single_subject_new[i.heading] = i.paragraph.split('<>')
	else:
		single_subject = Data.objects.filter(subject=1)
		subject_name = NewSubjects.objects.get(id=1)
		single_subject_new = {}
		for i in single_subject:
			single_subject_new[i.heading] = i.paragraph.split('<>')
	return render(request,'home.html',{'subjects':subjects, 'single_subject':single_subject_new,'subject_name':subject_name})
@login_required(login_url='/login')
def welcome(request):
	subjects = NewSubjects.objects.all()
	subject_id = request.GET.get('subject')
	single_subject_new = {}
	if subject_id:
		single_subject = Data.objects.filter(subject=int(subject_id))
		subject_name = NewSubjects.objects.get(id=int(subject_id))
		single_subject_new = {}
		for i in single_subject:
			single_subject_new[i.heading] = i.paragraph.split('<>')
	else:
		single_subject = Data.objects.filter(subject=1)
		subject_name = NewSubjects.objects.get(id=1)
		single_subject_new = {}
		for i in single_subject:
			single_subject_new[i.heading] = i.paragraph.split('<>')
	return render(request,'welcome.html',{'subjects':subjects, 'single_subject':single_subject_new,'subject_name':subject_name})


@login_required(login_url='/login')
def teacher(request):
	subject_list = NewSubjects.objects.filter(user=request.user)
	if request.method=='POST':
		heading = request.POST['Heading']
		subject = request.POST['Subject']
		paragraph = request.POST['Paragraph']
		subject_id = NewSubjects.objects.get(id=int(subject))
		content = Data(heading=heading,paragraph=paragraph,subject=subject_id)
		content.save()
		return redirect('/teacher')
	return render(request, 'teacher_form.html',{'subject_list':subject_list})

@login_required(login_url='/login')
def new_subject(request):
	if request.method=='POST':
		new_subject = request.POST['new_subject']
		description = request.POST['description']
		user = request.user
		print(user)
		subject_data = NewSubjects(user = user,name=new_subject,description=description)
		subject_data.save()
		return redirect('/teacher')
		print("Saved")
	return render(request, 'new_subject.html')

def testing(request):
	data= "Hello my name is Lakhanlal Gupta, I am a Data Scientist at Vkonex AI Research, It is one of the best company ever, It is in Mumbai"
	data = data.split(',')
	return render(request, 'testing.html',{'data':data})

def signup(request):
	if request.method=='POST':
		fname=request.POST['fname']
		lname=request.POST['lname']
		email=request.POST['email']
		uname=request.POST['username']
		passwd=request.POST['psw']
		conf_passwd = request.POST['psw_repeat']
		try:
			u=User(first_name=fname,last_name=lname,email=email,username=uname,password=make_password(passwd))
			u.save()
			return redirect('/login')
		except:
			messages.error(request, 'Username already exists at HiBlog.', extra_tags='safe')

	return render(request,'reg.html')


def login_call(request):
	if request.method=='POST':
		uname=request.POST['uname']
		passwd=request.POST['psw']
		currentUser=authenticate(username=uname,password=passwd)
		if currentUser:
			login(request,currentUser)
			print("Login done!")
			return redirect('/welcome')
		else:
			print("oops,Wrong password!")
			messages.error(request, 'Ooops, Wrong username or password.', extra_tags='safe')
	return render(request, 'login.html')

def logout_call(request):
	logout(request)
	return redirect('/')