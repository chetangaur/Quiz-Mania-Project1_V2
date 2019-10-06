from django.shortcuts import render
from django.http import HttpResponseRedirect
from login_register.views import *  # this is imported to work with User database of Django
from .models import *
from django.contrib.auth.models import User
# Create your views here.


# displays the Questions from the Docker table
def Docker_B(request):
    if request.user.is_authenticated:
        table_name = request.POST['table']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)
        context = {
            'test': Docker_B.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.username
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == Docker_B.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++
        
        # NEEDS TO BE CHANGED/REMOVED
        if context['score'] == 2:
            return render(request,'result.html',context)

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        if context['wrong'] == 1:
            return HttpResponseRedirect('logout')
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")

def AWS_B(request):
    if request.user.is_authenticated:
        table_name = request.POST['table']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)
        context = {
            'test': AWS_B.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.username
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == AWS_B.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++
        
        # NEEDS TO BE CHANGED/REMOVED
        if context['score'] == 2:
            return render(request,'result.html',context)

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        if context['wrong'] == 1:
            return HttpResponseRedirect('logout')
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")

# displays the Questions from the table
def Redhat_B(request):
    if request.user.is_authenticated:
        table_name = request.POST['table']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)
        context = {
            'test': Redhat_B.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.username
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == Redhat_B.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++
        
        # NEEDS TO BE CHANGED/REMOVED
        if context['score'] == 2:
            return render(request,'result.html',context)

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        if context['wrong'] == 1:
            return HttpResponseRedirect('logout')
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")

# displays the Questions from the table
def Python_B(request):
    if request.user.is_authenticated:
        table_name = request.POST['table']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)
        context = {
            'test': Python_B.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.username
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == Python_B.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++
        
        # NEEDS TO BE CHANGED/REMOVED
        if context['score'] == 2:
            return render(request,'result.html',context)

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        if context['wrong'] == 1:
            return HttpResponseRedirect('logout')
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")

# displays the Questions from the table
def Tensorflow_B(request):
    if request.user.is_authenticated:
        table_name = request.POST['table']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)
        context = {
            'test': Tensorflow_B.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.username
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == Tensorflow_B.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++
        
        # NEEDS TO BE CHANGED/REMOVED
        if context['score'] == 2:
            return render(request,'result.html',context)

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        if context['wrong'] == 1:
            return HttpResponseRedirect('logout')
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")

# displays the Questions from the table
def ComputerVision_B(request):
    if request.user.is_authenticated:
        table_name = request.POST['table']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)
        context = {
            'test': ComputerVision_B.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.username
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == ComputerVision_B.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++
        
        # NEEDS TO BE CHANGED/REMOVED
        if context['score'] == 2:
            return render(request,'result.html',context)

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        if context['wrong'] == 1:
            return HttpResponseRedirect('logout')
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")

# displays the Questions from the table
def Kubernetes_B(request):
    if request.user.is_authenticated:
        table_name = request.POST['table']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)
        context = {
            'test': Kubernetes_B.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.username
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == Kubernetes_B.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++
        
        # NEEDS TO BE CHANGED/REMOVED
        if context['score'] == 2:
            return render(request,'result.html',context)

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        if context['wrong'] == 1:
            return HttpResponseRedirect('logout')
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")

# displays the Questions from the table
def ScikitLearn_B(request):
    if request.user.is_authenticated:
        table_name = request.POST['table']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)
        context = {
            'test': ScikitLearn_B.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.username
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == ScikitLearn_B.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++
        
        # NEEDS TO BE CHANGED/REMOVED
        if context['score'] == 2:
            return render(request,'result.html',context)

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        if context['wrong'] == 1:
            return HttpResponseRedirect('logout')
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")

# displays the Questions from the table
def Docker_I(request):
    if request.user.is_authenticated:
        table_name = request.POST['table']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)
        context = {
            'test': Docker_I.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.username
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == Docker_I.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++
        
        # NEEDS TO BE CHANGED/REMOVED
        if context['score'] == 2:
            return render(request,'result.html',context)

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        if context['wrong'] == 1:
            return HttpResponseRedirect('logout')
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")

# displays the Questions from the table
def AWS_I(request):
    if request.user.is_authenticated:
        table_name = request.POST['table']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)
        context = {
            'test': AWS_I.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.username
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == AWS_I.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++
        
        # NEEDS TO BE CHANGED/REMOVED
        if context['score'] == 2:
            return render(request,'result.html',context)

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        if context['wrong'] == 1:
            return HttpResponseRedirect('logout')
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")
# displays the Questions from the table
def Redhat_I(request):
    if request.user.is_authenticated:
        table_name = request.POST['table']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)
        context = {
            'test': Redhat_I.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.username
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == Redhat_I.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++
        
        # NEEDS TO BE CHANGED/REMOVED
        if context['score'] == 2:
            return render(request,'result.html',context)

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        if context['wrong'] == 1:
            return HttpResponseRedirect('logout')
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")

# displays the Questions from the table
def Python_I(request):
    if request.user.is_authenticated:
        table_name = request.POST['table']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)
        context = {
            'test': Python_I.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.username
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == Python_I.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++
        
        # NEEDS TO BE CHANGED/REMOVED
        if context['score'] == 2:
            return render(request,'result.html',context)

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        if context['wrong'] == 1:
            return HttpResponseRedirect('logout')
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")

# displays the Questions from the table
def Tensorflow_I(request):
    if request.user.is_authenticated:
        table_name = request.POST['table']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)
        context = {
            'test': Tensorflow_I.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.username
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == Tensorflow_I.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++
        
        # NEEDS TO BE CHANGED/REMOVED
        if context['score'] == 2:
            return render(request,'result.html',context)

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        if context['wrong'] == 1:
            return HttpResponseRedirect('logout')
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")

# displays the Questions from the table
def ComputerVision_I(request):
    if request.user.is_authenticated:
        table_name = request.POST['table']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)
        context = {
            'test': ComputerVision_I.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.username
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == ComputerVision_I.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++
        
        # NEEDS TO BE CHANGED/REMOVED
        if context['score'] == 2:
            return render(request,'result.html',context)

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        if context['wrong'] == 1:
            return HttpResponseRedirect('logout')
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")
# displays the Questions from the table
def Kubernetes_I(request):
    if request.user.is_authenticated:
        table_name = request.POST['table']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)
        context = {
            'test': Kubernetes_I.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.username
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == Kubernetes_I.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++
        
        # NEEDS TO BE CHANGED/REMOVED
        if context['score'] == 2:
            return render(request,'result.html',context)

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        if context['wrong'] == 1:
            return HttpResponseRedirect('logout')
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")

# displays the Questions from the table
def ScikitLearn_I(request):
    if request.user.is_authenticated:
        table_name = request.POST['table']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)
        context = {
            'test': ScikitLearn_I.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.username
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == ScikitLearn_I.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++
        
        # NEEDS TO BE CHANGED/REMOVED
        if context['score'] == 2:
            return render(request,'result.html',context)

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        if context['wrong'] == 1:
            return HttpResponseRedirect('logout')
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")

# displays the Questions from the table
def Docker_A(request):
    if request.user.is_authenticated:
        table_name = request.POST['table']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)
        context = {
            'test': Docker_A.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.username
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == Docker_A.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++
        
        # NEEDS TO BE CHANGED/REMOVED
        if context['score'] == 2:
            return render(request,'result.html',context)

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        if context['wrong'] == 1:
            return HttpResponseRedirect('logout')
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")

# displays the Questions from the table
def AWS_A(request):
    if request.user.is_authenticated:
        table_name = request.POST['table']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)
        context = {
            'test': AWS_A.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.username
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == AWS_A.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++
        
        # NEEDS TO BE CHANGED/REMOVED
        if context['score'] == 2:
            return render(request,'result.html',context)

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        if context['wrong'] == 1:
            return HttpResponseRedirect('logout')
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")

# displays the Questions from the table
def Redhat_A(request):
    if request.user.is_authenticated:
        table_name = request.POST['table']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)
        context = {
            'test': Redhat_A.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.username
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == Redhat_A.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++
        
        # NEEDS TO BE CHANGED/REMOVED
        if context['score'] == 2:
            return render(request,'result.html',context)

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        if context['wrong'] == 1:
            return HttpResponseRedirect('logout')
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")

# displays the Questions from the table
def Python_A(request):
    if request.user.is_authenticated:
        table_name = request.POST['table']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)
        context = {
            'test': Python_A.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.username
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == Python_A.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++
        
        # NEEDS TO BE CHANGED/REMOVED
        if context['score'] == 2:
            return render(request,'result.html',context)

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        if context['wrong'] == 1:
            return HttpResponseRedirect('logout')
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")

# displays the Questions from the table
def Tensorflow_A(request):
    if request.user.is_authenticated:
        table_name = request.POST['table']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)
        context = {
            'test': Tensorflow_A.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.username
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == Tensorflow_A.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++
        
        # NEEDS TO BE CHANGED/REMOVED
        if context['score'] == 2:
            return render(request,'result.html',context)

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        if context['wrong'] == 1:
            return HttpResponseRedirect('logout')
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")

# displays the Questions from the table
def ComputerVision_A(request):
    if request.user.is_authenticated:
        table_name = request.POST['table']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)
        context = {
            'test': ComputerVision_A.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.username
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == ComputerVision_A.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++
        
        # NEEDS TO BE CHANGED/REMOVED
        if context['score'] == 2:
            return render(request,'result.html',context)

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        if context['wrong'] == 1:
            return HttpResponseRedirect('logout')
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")

# displays the Questions from the table
def Kubernetes_A(request):
    if request.user.is_authenticated:
        table_name = request.POST['table']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)
        context = {
            'test': Kubernetes_A.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.username
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == Kubernetes_A.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++
        
        # NEEDS TO BE CHANGED/REMOVED
        if context['score'] == 2:
            return render(request,'result.html',context)

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        if context['wrong'] == 1:
            return HttpResponseRedirect('logout')
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")

# displays the Questions from the table
def ScikitLearn_A(request):
    if request.user.is_authenticated:
        table_name = request.POST['table']
        answer = request.POST.get('opsi')           # option selected by user
        value = request.POST['question_value']      # used to fetch question from database
        value = int(value)+1
        score = request.POST['score']               # marks scored
        score = int(score)
        wrong = request.POST['wrong']               # incorrect options selected
        wrong = int(wrong)
        context = {
            'test': ScikitLearn_A.objects.get(id=value),
            'value' : value,
            'answer' : answer,
            'score' : score,
            'wrong' : wrong,
            'username' : request.user.username
        }
        
        # this is jugaad... to make sure proper answers and questions can be represented
        if context['value'] == 1:
            return render(request,'testpage.html',context)
        
        # check if the answer selected by user is correct or not
        if str(answer) == ScikitLearn_A.objects.get(id=value-1).Answer:
            context['score'] += 1  # if answer is right score ++
        else:
            context['wrong'] += 1  # if answer is wrong then wrong ++
        
        # NEEDS TO BE CHANGED/REMOVED
        if context['score'] == 2:
            return render(request,'result.html',context)

        # IF LIMIT OOF QUESTIONS GETS WRONG...do the changes
        if context['wrong'] == 1:
            return HttpResponseRedirect('logout')
        
        # SHOW THE TEST PAGE
        return render(request,'testpage.html',context)
    else:
        # If user is not logged in.. redirect to login page
        return HttpResponseRedirect("login_page")