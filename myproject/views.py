#i have created this file Utkarsh
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   return  render(request,'index.html')

def analyze(request):
   djtext = request.POST.get('text','default')
   removepunc = request.POST.get('removepunc','default')
   Uppercase = request.POST.get('Uppercase','default')
   Newlineremover = request.POST.get('Newlineremover','default')
   Analyzed =""
   # print(djtext)
   print(removepunc)
   punctuations='''"<>,.;:!"£$%^&*()#@'()[]{}/'''
   if removepunc == 'on':
    for char in djtext:
        if char not in punctuations:
          Analyzed = Analyzed+char
          params = {'purpose':'Removepunc','Analysed_text':Analyzed}
          djtext=Analyzed
   #  return render(request,'analyze.html',params)
   elif Uppercase=='on':
      Analyzed=""
      for char in djtext:
         Analyzed = Analyzed+char.upper()
         params = {'purpose':'Changed in uppercase','Analysed_text':Analyzed}
         djtext=Analyzed
      # return render(request,'analyze.html',params)
   elif Newlineremover=='on':
      Analyzed=""
      for char in djtext:
        if(char!='\n' and char!='\r') :
         Analyzed = Analyzed + char
         params = {'purpose':'Newline removed','Analysed_text':Analyzed}
         djtext=Analyzed
      # return render(request,'analyze.html',params)
   # else:
   #    return HttpResponse('error')
   return render(request,'analyze.html',params)