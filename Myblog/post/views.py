from django.shortcuts import render,redirect
from .models import MyPost
from .forms import MyPostForm
def index(request):
	posts=MyPost.objects.order_by("-id")
	post_number=posts.count()
	header="{} posts".format(post_number)
	if post_number<=1:
		header=header="{} post".format(post_number)
	content={
	'posts':posts,
	"header":header
	}
	return render(request,'pages/index.html',content)

def show(request,id):
	post=MyPost.objects.get(id=id)
	return render(request,'pages/show.html',{"post":post})

def new(request):
	if request.method=="POST":
		form=MyPostForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect("post:index")
	else:
		form=MyPostForm()
	context={
		'form':form,
	}
	return render(request,'pages/new.html',context)

def update(request,id):
	post=MyPost.objects.get(id=id)

	if request.method=="POST":
		form=MyPostForm(request.POST,request.FILES,instance=post)
		if form.is_valid():
			form.save()
			return redirect("post:index")
	else:
		form=MyPostForm(instance=post)

	return render(request, 'pages/update.html',{'post':post,'form':form})