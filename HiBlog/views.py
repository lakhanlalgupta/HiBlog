from django.shortcuts import render,redirect, HttpResponse

from .models import Data, NewSubjects

def home(request):
	subjects = NewSubjects.objects.all()
	subject_id = request.GET.get('subject')
	single_subject_new = {}

	if subject_id:
		single_subject = Data.objects.filter(subject=int(subject_id))
		single_subject_new = {}
		for i in single_subject:
			single_subject_new[i.heading] = i.paragraph.split('<>')
	else:
		single_subject = Data.objects.filter(subject=1)
		single_subject_new = {}
		for i in single_subject:
			single_subject_new[i.heading] = i.paragraph.split('<>')
	return render(request,'home.html',{'subjects':subjects, 'single_subject':single_subject_new})

def teacher(request):
	subject_list = NewSubjects.objects.all()
	if request.method=='POST':
		heading = request.POST['Heading']
		subject = request.POST['Subject']
		paragraph = request.POST['Paragraph']
		try:
			subject_id = NewSubjects.objects.get(id=int(subject))
		except:
			return redirect('/teacher')
		try:
			content = Data(heading=heading,paragraph=paragraph,subject=subject_id)
			print(content)
			content.save()
			return redirect('/teacher')
		except:
			return redirect('/teacher')
	return render(request, 'teacher_form.html',{'subject_list':subject_list})


def new_subject(request):
	if request.method=='POST':
		new_subject = request.POST['new_subject']
		description = request.POST['description']
		subject_data = NewSubjects(name=new_subject,description=description)
		subject_data.save()
		return redirect('/teacher')
	return render(request, 'new_subject.html')

def testing(request):
	data= "Hello my name is Lakhanlal Gupta, I am a Data Scientist at Vkonex AI Research, It is one of the best company ever, It is in Mumbai"
	data = data.split(',')
	return render(request, 'testing.html',{'data':data})