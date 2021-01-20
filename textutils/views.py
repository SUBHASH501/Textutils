from  django.http import HttpResponse
from django.shortcuts import  render
"""
def index(request):
    return HttpResponse('''<h1>This is website link of code with herry<h1><a href="https://codewithharry.com/videos/python-django-tutorials-hindi-5">Django code with harry</a>''')
def about(request):
    return HttpResponse("about Subhash Ishwar bhai")"""
"""
#code for pipelineing

def index(request):
    return HttpResponse("Home")
    
def removepunc(request):
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("capitallizefirst")

def newlinermove(request):
    return HttpResponse("new line move")

def spaceremove(request):
    return HttpResponse("space remover <a href='/'>back button</a>")

def charcount(request):
    return HttpResponse("charcount")
"""

#code for templates
def index(request):
   # prams={'name':'subhash','place':'India'} #dictnory
    return render(request, 'index.html')  # render takes first argument request and second template name

def analyze(request):
    #get the text
    djtext=request.POST.get('text','nothing is written')#text is that we will write in our text area

    #checkbox value
    removepunc = request.POST.get('removepunc', 'off') #at the place of POST we also able to use GET but the
                                                       #data we write in GET it will be visible to URL ans that is
                                                       #not safe
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount= request.POST.get('charcount', 'off')


    #print(removepunc)
    #print(djtext)
    #analyse the text
    #return HttpResponse("remove punc")
    #analyzed=djtext

    #check which check box is on
    if removepunc=="on":
       punctuations='''!@#$%^&*()_{}:;"'?<>\/[].,-+'~'''
       analyzed=""
       for char in djtext:
           if char not in punctuations:
               analyzed =analyzed+char
       params={'purpose':'removed punctuations','analyzed_text':analyzed}
       djtext=analyzed
       #return render(request ,'analyze.html',params)

    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed +char.upper()
        params = {'purpose': 'Changed to uppercase', 'analyzed_text': analyzed}
        #analyzed the text in upper case
        djtext =analyzed
        #return render(request, 'analyze.html', params)

    elif(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
               analyzed = analyzed + char
        params = {'purpose': 'Removed new lines', 'analyzed_text': analyzed}
        # analyzed the text in upper case
        djtext=analyzed
        #return render(request, 'analyze.html', params)

    if (extraspaceremover =="on"):
         analyzed = ""
         for index ,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] ==" "):
                analyzed = analyzed + char
         params = {'purpose': 'Extra space  lines', 'analyzed_text': analyzed}
        # analyzed the text in upper case
         djtext = analyzed
         #return render(request, 'analyze.html', params)

    if (charcount == "on"):
         analyzed = 0
         while analyzed < len(djtext):
             analyzed += 1
         params = {'purpose': 'Number of char', 'analyzed_text': analyzed}
        # analyzed the text in upper case
         djtext = analyzed
         #return render(request, 'analyze.html', params)

    if(removepunc !='on' and extraspaceremover !='on' and fullcaps !='on' and newlineremover !='on'):
       return render(request,'error.html')

    return render(request, 'analyze.html', params)


