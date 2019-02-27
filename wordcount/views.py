from django.shortcuts import render

# Create your views here.

def home (request):
    ##render (request, ~.html 템플릿 이름,사전형 객체)
    return render(request,'home.html',)
    
def about (request):
    return render(request,'about.html')

def result (request):
    text = request.GET['fulltext']
    words = text.split()
    word_list = {}
    for word in words:
        if word in word_list:
            word_list[word]+=1
        else:
            word_list[word]=1

    ## 세번째 인자는 사전형으로 이용한다 키값:value
    # 총 단어 수  =  len(words)
    return render(request,'result.html', {'full': text, 'total': len(words),'list': word_list.items()})