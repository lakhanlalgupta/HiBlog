from django.shortcuts import render,redirect, HttpResponse
from django.core.exceptions import SuspiciousOperation
from HiBlog.models import Data, NewSubjects, User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url='/login')
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
			single_subject_new[i.pic]=i.pic
			print(i.pic)
	else:
		single_subject = Data.objects.filter(subject=5)
		subject_name = NewSubjects.objects.get(id=5)
		single_subject_new = {}
		for i in single_subject:
			single_subject_new[i.heading] = i.paragraph.split('<>')
	return render(request,'welcome.html',{'subjects':subjects,'single_subject_pic':single_subject, 'single_subject':single_subject_new,'subject_name':subject_name})

@login_required(login_url='/login')
def teacher(request):
	subject_list = NewSubjects.objects.filter(user=request.user)
	if request.method=='POST':
		heading = request.POST['Heading']
		subject = request.POST['Subject']
		paragraph = request.POST['Paragraph']
		try:
			dimage=request.FILES["pic1"]
			print(dimage)
			subject_id = NewSubjects.objects.get(id=int(subject))
			content = Data(heading=heading,paragraph=paragraph,pic=dimage,subject=subject_id)
			content.save()
		except:
			dimage = 'breaker.png'
			subject_id = NewSubjects.objects.get(id=int(subject))
			content = Data(heading=heading,paragraph=paragraph,pic=dimage,subject=subject_id)
			content.save()
		return redirect('/welcome/teacher/')
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
		return redirect('/welcome/teacher/')
		print("Saved")
	return render(request, 'new_subject.html')