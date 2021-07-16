from django.shortcuts import render
from . import models
from django.http import HttpResponse  # or:   from django.shortcuts import HttpResponse
# Create your views here.
def articlesList(request):
    varticle=models.article.objects.all().order_by('date')
    arg={'article000':varticle}
    return render(request,'article/articleList.html',arg)
def artictest(request,sluggg):  #slug daroone parantezzzzzzzzzzzzzzzzz
    return HttpResponse(sluggg)
    # models.slug?
