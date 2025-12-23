from django.shortcuts import render,redirect
from .models import JobPost,BlogPost
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# Create your views here.
# def home(request):
#     return render(request,"home4.html")
# def typing(request):
#     return render(request,"typing4.html")
def taptap(request):
    if request.method == 'GET':
        test_duration = request.GET.get('test_duration')
        text_type = request.GET.get('text_type')
    else:
        test_duration = request.session.get('test_duration', 60)  # Default to 60 seconds
        text_type = request.session.get('text_type', 'Easy')
    return render(request,"taptap.html",{'test_duration': test_duration,'text_type': text_type})

def GH(request):
    if request.method == 'GET':
        test_duration = request.GET.get('test_duration')
        text_type = request.GET.get('text_type')
    else:
        test_duration = request.session.get('test_duration', 60)  # Default to 60 seconds
        text_type = request.session.get('text_type', 'Easy')
    return render(request,"GH.html",{'test_duration': test_duration,'text_type': text_type})
def S(request):
    if request.method == 'GET':
        test_duration = request.GET.get('test_duration')
        text_type = request.GET.get('text_type')
    else:
        test_duration = request.session.get('test_duration', 60)  # Default to 60 seconds
        text_type = request.session.get('text_type', 'Easy')
    return render(request,"S.html",{'test_duration': test_duration,'text_type': text_type})
def C(request):
    if request.method == 'GET':
        test_duration = request.GET.get('test_duration')
        text_type = request.GET.get('text_type')
    else:
        test_duration = request.session.get('test_duration', 60)  # Default to 60 seconds
        text_type = request.session.get('text_type', 'Easy')
    return render(request,"C.html",{'test_duration': test_duration,'text_type': text_type})
def V(request):
    if request.method == 'GET':
        test_duration = request.GET.get('test_duration')
        text_type = request.GET.get('text_type')
    else:
        test_duration = request.session.get('test_duration', 60)  # Default to 60 seconds
        text_type = request.session.get('text_type', 'Easy')
    return render(request,"V.html",{'test_duration': test_duration,'text_type': text_type})
def ZN(request):
    if request.method == 'GET':
        test_duration = request.GET.get('test_duration')
        text_type = request.GET.get('text_type')
    else:
        test_duration = request.session.get('test_duration', 60)  # Default to 60 seconds
        text_type = request.session.get('text_type', 'Easy')
    return render(request,"ZN.html",{'test_duration': test_duration,'text_type': text_type})
def XM(request):
    if request.method == 'GET':
        test_duration = request.GET.get('test_duration')
        text_type = request.GET.get('text_type')
    else:
        test_duration = request.session.get('test_duration', 60)  # Default to 60 seconds
        text_type = request.session.get('text_type', 'Easy')
    return render(request,"XM.html",{'test_duration': test_duration,'text_type': text_type})
def RI(request):
    if request.method == 'GET':
        test_duration = request.GET.get('test_duration')
        text_type = request.GET.get('text_type')
    else:
        test_duration = request.session.get('test_duration', 60)  # Default to 60 seconds
        text_type = request.session.get('text_type', 'Easy')
    return render(request,"RI.html",{'test_duration': test_duration,'text_type': text_type})
def EO(request):
    if request.method == 'GET':
        test_duration = request.GET.get('test_duration')
        text_type = request.GET.get('text_type')
    else:
        test_duration = request.session.get('test_duration', 60)  # Default to 60 seconds
        text_type = request.session.get('text_type', 'Easy')
    return render(request,"EO.html",{'test_duration': test_duration,'text_type': text_type})
def WP(request):
    if request.method == 'GET':
        test_duration = request.GET.get('test_duration')
        text_type = request.GET.get('text_type')
    else:
        test_duration = request.session.get('test_duration', 60)  # Default to 60 seconds
        text_type = request.session.get('text_type', 'Easy')
    return render(request,"WP.html",{'test_duration': test_duration,'text_type': text_type})
def QU(request):
    if request.method == 'GET':
        test_duration = request.GET.get('test_duration')
        text_type = request.GET.get('text_type')
    else:
        test_duration = request.session.get('test_duration', 60)  # Default to 60 seconds
        text_type = request.session.get('text_type', 'Easy')
    return render(request,"QU.html",{'test_duration': test_duration,'text_type': text_type})
def DL(request):
    if request.method == 'GET':
        test_duration = request.GET.get('test_duration')
        text_type = request.GET.get('text_type')
    else:
        test_duration = request.session.get('test_duration', 60)  # Default to 60 seconds
        text_type = request.session.get('text_type', 'Easy')
    return render(request,"DL.html",{'test_duration': test_duration,'text_type': text_type})
def FK(request):
    if request.method == 'GET':
        test_duration = request.GET.get('test_duration')
        text_type = request.GET.get('text_type')
    else:
        test_duration = request.session.get('test_duration', 60)  # Default to 60 seconds
        text_type = request.session.get('text_type', 'Easy')
    return render(request,"FK.html",{'test_duration': test_duration,'text_type': text_type})
def AJ(request):
    if request.method == 'GET':
        test_duration = request.GET.get('test_duration')
        text_type = request.GET.get('text_type')
    else:
        test_duration = request.session.get('test_duration', 60)  # Default to 60 seconds
        text_type = request.session.get('text_type', 'Easy')
    return render(request,"AJ.html",{'test_duration': test_duration,'text_type': text_type})
def BottomRowPractce(request):
    if request.method == 'GET':
        test_duration = request.GET.get('test_duration')
        text_type = request.GET.get('text_type')
    else:
        test_duration = request.session.get('test_duration', 60)  # Default to 60 seconds
        text_type = request.session.get('text_type', 'Easy')
    return render(request,"BottomRowPractce.html",{'test_duration': test_duration,'text_type': text_type})
def X(request):
    if request.method == 'GET':
        test_duration = request.GET.get('test_duration')
        text_type = request.GET.get('text_type')
    else:
        test_duration = request.session.get('test_duration', 60)  # Default to 60 seconds
        text_type = request.session.get('text_type', 'Easy')
    return render(request,"X.html",{'test_duration': test_duration,'text_type': text_type})
def Z(request):
    if request.method == 'GET':
        test_duration = request.GET.get('test_duration')
        text_type = request.GET.get('text_type')
    else:
        test_duration = request.session.get('test_duration', 60)  # Default to 60 seconds
        text_type = request.session.get('text_type', 'Easy')
    return render(request,"Z.html",{'test_duration': test_duration,'text_type': text_type})
def CM(request):
    if request.method == 'GET':
        test_duration = request.GET.get('test_duration')
        text_type = request.GET.get('text_type')
    else:
        test_duration = request.session.get('test_duration', 60)  # Default to 60 seconds
        text_type = request.session.get('text_type', 'Easy')
    return render(request,"CM.html",{'test_duration': test_duration,'text_type': text_type})
def BB(request):
    if request.method == 'GET':
        test_duration = request.GET.get('test_duration')
        text_type = request.GET.get('text_type')
    else:
        test_duration = request.session.get('test_duration', 60)  # Default to 60 seconds
        text_type = request.session.get('text_type', 'Easy')
    return render(request,"BB.html",{'test_duration': test_duration,'text_type': text_type})
def VN(request):
    if request.method == 'GET':
        test_duration = request.GET.get('test_duration')
        text_type = request.GET.get('text_type')
    else:
        test_duration = request.session.get('test_duration', 60)  # Default to 60 seconds
        text_type = request.session.get('text_type', 'Easy')
    return render(request,"VN.html",{'test_duration': test_duration,'text_type': text_type})
def topRowPractice(request):
    if request.method == 'GET':
        test_duration = request.GET.get('test_duration')
        text_type = request.GET.get('text_type')
    else:
        test_duration = request.session.get('test_duration', 60)  # Default to 60 seconds
        text_type = request.session.get('text_type', 'Easy')
    return render(request,"topRowPractice.html",{'test_duration': test_duration,'text_type': text_type})
def QP(request):
    if request.method == 'GET':
        test_duration = request.GET.get('test_duration')
        text_type = request.GET.get('text_type')
    else:
        test_duration = request.session.get('test_duration', 60)  # Default to 60 seconds
        text_type = request.session.get('text_type', 'Easy')
    return render(request,"QP.html",{'test_duration': test_duration,'text_type': text_type})
def WO(request):
    if request.method == 'GET':
        test_duration = request.GET.get('test_duration')
        text_type = request.GET.get('text_type')
    else:
        test_duration = request.session.get('test_duration', 60)  # Default to 60 seconds
        text_type = request.session.get('text_type', 'Easy')
    return render(request,"WO.html",{'test_duration': test_duration,'text_type': text_type})
def EI(request):
    if request.method == 'GET':
        test_duration = request.GET.get('test_duration')
        text_type = request.GET.get('text_type')
    else:
        test_duration = request.session.get('test_duration', 60)  # Default to 60 seconds
        text_type = request.session.get('text_type', 'Easy')
    return render(request,"EI.html",{'test_duration': test_duration,'text_type': text_type})
def RU(request):
    if request.method == 'GET':
        test_duration = request.GET.get('test_duration')
        text_type = request.GET.get('text_type')
    else:
        test_duration = request.session.get('test_duration', 60)  # Default to 60 seconds
        text_type = request.session.get('text_type', 'Easy')
    return render(request,"RU.html",{'test_duration': test_duration,'text_type': text_type})
def TY(request):
    if request.method == 'GET':
        test_duration = request.GET.get('test_duration')
        text_type = request.GET.get('text_type')
    else:
        test_duration = request.session.get('test_duration', 60)  # Default to 60 seconds
        text_type = request.session.get('text_type', 'Easy')
    return render(request,"TY.html",{'test_duration': test_duration,'text_type': text_type})
def homeRowPractice(request):
    if request.method == 'GET':
        test_duration = request.GET.get('test_duration')
        text_type = request.GET.get('text_type')
    else:
        test_duration = request.session.get('test_duration', 60)  # Default to 60 seconds
        text_type = request.session.get('text_type', 'Easy')
    return render(request,"homeRowPractice.html",{'test_duration': test_duration,'text_type': text_type})
def A(request):
    if request.method == 'GET':
        test_duration = request.GET.get('test_duration')
        text_type = request.GET.get('text_type')
    else:
        test_duration = request.session.get('test_duration', 60)  # Default to 60 seconds
        text_type = request.session.get('text_type', 'Easy')
    return render(request,"A.html",{'test_duration': test_duration,'text_type': text_type})
def SL(request):
    if request.method == 'GET':
        test_duration = request.GET.get('test_duration')
        text_type = request.GET.get('text_type')
    else:
        test_duration = request.session.get('test_duration', 60)  # Default to 60 seconds
        text_type = request.session.get('text_type', 'Easy')
    return render(request,"SL.html",{'test_duration': test_duration,'text_type': text_type})
def DK(request):
    if request.method == 'GET':
        test_duration = request.GET.get('test_duration')
        text_type = request.GET.get('text_type')
    else:
        test_duration = request.session.get('test_duration', 60)  # Default to 60 seconds
        text_type = request.session.get('text_type', 'Easy')
    return render(request,"DK.html",{'test_duration': test_duration,'text_type': text_type})
def FJ(request):
    if request.method == 'GET':
        test_duration = request.GET.get('test_duration')
        text_type = request.GET.get('text_type')
    else:
        test_duration = request.session.get('test_duration', 60)  # Default to 60 seconds
        text_type = request.session.get('text_type', 'Easy')
    return render(request,"FJ.html",{'test_duration': test_duration,'text_type': text_type})

def start_test(request):
    return render(request, 'home2.html')


def FAQ(request):
    return render(request, 'FAQ.html')
def typingGame(request):
    return render(request, 'typingGame.html')
def policy(request):
    return render(request, 'policy.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def jobs(req):
    jobposts= JobPost.objects.all()
    print(jobposts)
    return render(req,"jobPost.html",{'jobposts':jobposts})

def job_details(req,pk):
    job= JobPost.objects.get(id=pk)
    return render(req,"jobs.html",{'job_details':job})

def blogs(req):
    blogposts= BlogPost.objects.all()
    
    return render(req,"blogsPost.html",{'blogposts':blogposts})

def blog_details(req,pk):
    blog= BlogPost.objects.get(id=pk)
    return render(req,"blogs.html",{'blog_details':blog})

def base(req):
    return render(req,"base2.html")
def police(req):
    return render(req,"police.html")

def typingLession(req):
    return render(req,'typingL.html')

from .forms import JobPostForm,BlogPostForm
@login_required
def JobpostForm(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('jobs')  # or wherever you'd like to go after posting
    else:
        form = JobPostForm()
    return render(request, 'jobPostform.html', {'form': form})
@login_required
def blogpostForm(request):
    if request.user.is_staff and request.user.is_authenticated:
        if request.method == 'POST':
            form = BlogPostForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
            return redirect('blogs_list')  # or wherever you'd like to go after posting
        else:
            form = BlogPostForm()
    
    return render(request, 'blogPostform.html', {'form': form})

@login_required
def blog_list(request):
    if not request.user.is_staff:
        return redirect('login')
    posts = BlogPost.objects.all()  # adjust based on your model
    return render(request, 'blog_list.html', {'posts': posts})
from django.shortcuts import get_object_or_404

@login_required
def blog_detail(request, pk):
    if not request.user.is_staff:
        return redirect('login')
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog_detail.html', {'post': post})
@login_required
def blog_update(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', pk=pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blogPostform.html', {'form': form, 'update': True})
@login_required
def blog_delete(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        post.delete()
        return redirect('blogs')
    return render(request, 'blog_confirm_delete.html', {'post': post})



