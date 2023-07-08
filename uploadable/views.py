from django.shortcuts import render,redirect
from .form import ImageForm
from .models import datas

# Create your views here.
def home(request):
    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            return redirect("/")
    else:
        form=ImageForm()
    img=datas.objects.all().order_by("-id")
    return render(request,"home.html",{"img":img,"form":form})