from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def ex1(request):
    return render(request, 'ex1_solution.html')

def analyze(request):
    
    #Get the text
    djtext = request.POST.get('text','default')
    
    #Check the checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    NewLineRemover = request.POST.get('newlineremover', 'off')
    ExtraSpaceRemover = request.POST.get('spaceremover', 'off')
    CharacterCount = request.POST.get('charactercount', 'off')

    strr = djtext
    purpose = ""

    #Check if checkbox is on
    if removepunc == "on":
        punctuation = '''!()-''[]{};:"",<>./?@#$%^&*_"~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {'purpose':'Remove Punctutaions','analyzed_text':analyzed}
        strr = analyzed
        purpose += "| Remove Punctutaions |"
        # return render(request, 'analyze.html', params)

    if uppercase == "on":
        strr = strr.upper()
        params = {'purpose':'Your capitalized text', 'analyzed_text': strr}
        purpose += "| capitalize |"
        # return render(request, 'analyze.html', params)

    if NewLineRemover == "on":
        analyzed = ""
        for char in strr:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose':'New Lines Removed','analyzed_text':analyzed}
        strr = analyzed
        purpose += "| New line removed |"
        # return render(request, 'analyze.html', params)

    if ExtraSpaceRemover == 'on':
        analyzed = ""
        for index,char in enumerate(strr):
            if not(strr[index] == " " and strr[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose':'Extra Spaces Removed','analyzed_text':analyzed}
        strr = analyzed
        purpose += "| Extra Space Removed |"
        # return render(request, 'analyze.html', params)

    if CharacterCount == 'on':
        count = 0
        for i in strr:
            if not(i == " "):
                count = count + 1
        # t1 = "Your final text " + strr + " has " + count + " number of characters."
        params = {'purpose':'The total number of characters in your string is','analyzed_text':count}
        strr = count
        purpose += "| Character Count |"
        # return render(request, 'analyze.html', params)

    param = {'purpose':purpose,'analyzed_text':strr}

    if removepunc == "on" or uppercase == "on" or NewLineRemover == "on" or ExtraSpaceRemover == "on" or CharacterCount == "on":
        return render(request, 'analyze.html', param)
    else:
        return HttpResponse("Error")






# def analyze(request):
#  data = request.GET.get('text', 'No text entered')

#  remPunc = request.GET.get('punc', 'of')
#  caps = request.GET.get('caps', 'of')
#  newLineRem = request.GET.get('newLineRem', 'of')
#  spaceRem = request.GET.get('spaceRem', 'of')

#  charcount = request.GET.get('charcount', 'of')
#  strr = data
#  purpose = ""

#  if remPunc == 'on':
#   tempStr = ""
#   puns = '''!@#$%^&*();'.,/:?>'''
#   for i in data:
#    if i not in puns:
#     tempStr = tempStr + i
#   params = {'purpose':'remove Punctuations' , 'answer':tempStr}
#   strr = tempStr
#   purpose += " | Remove Punctuations "
#   # return render(request, 'analyze.html', params)
#  if caps == 'on':
#   print("2",strr)
#   strr = strr.upper()
#   params = {'purpose':'Caps' , 'answer':strr}
#   purpose += "| Caps |"
#   # return render(request, 'analyze.html', params)

#  if newLineRem == 'on':
#   tempStr=""
#   for i in strr:
#    if i != '\n':
#     tempStr += i
#   params = {'purpose':'New Line remove' , 'answer':tempStr}
#   strr = tempStr
#   purpose += "| remove new line "
#   # return render(request, 'analyze.html', params)

#  if spaceRem == 'on':
#   tempStr = ""
#   for index, ch in enumerate(strr):
#    if not (strr[index] == " " and strr[index+1]==" "):
#     tempStr += ch
#   params = {'purpose':'spaces remove' , 'answer':tempStr}
#   strr = tempStr
#   purpose += "| Spaces remove |"

#  params = {'purpose':purpose , 'answer':strr}

#  if remPunc == 'on' or caps == 'on' or newLineRem == 'on' or spaceRem == 'on':
#   return render(request, 'analyze.html', params)
#  else:
#   return HttpResponse('error hai bhai')