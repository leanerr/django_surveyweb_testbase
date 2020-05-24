from django.shortcuts import render , redirect
from .models import Survey, SurveyAnswer, QuestionAnswer, Choice, Question, Survey
from django.contrib.auth import authenticate, login

def index(request):
    ctx = {}
    return render(request, 'main.html', ctx)

#showing survey
def survey_view(request, survey_id=None):
    try:
        #get the survey and question by using the survey_id that user enters to the form
        survey = Survey.objects.get(id=survey_id)
        question = survey.question_set.all()
        ctx = {
            'survey':survey,
            'questions':question,
               }
    except:
        return render(request, 'surveynotfound-error.html', {'sv_id':survey_id})

    return render(request, 'survey-take.html', ctx)

#get the survey id and redirect to survay_detail (exam)
def load_survey(request):
    #the name of the input is survey_view that equels to survey_id
    sv_to_load = request.POST['survey_view']
    return redirect('survey_detail', survey_id=sv_to_load)

#feel the answers that user is choosing
def survey_fill(request):
    answer = SurveyAnswer()
    #'survey_id' is what the hidden input feel by its name on the template
    orig_survey = Survey.objects.get(id=request.POST['survey_id'])
    #now we cleare for SurveyAnswer model that the particular survey is orig_survey that we we got from Survey model based on the id
    answer.orig_survey = orig_survey
    answer.save()
    #lets get all the questions from that orig_seurvey
    #remember you can use a question set or any particular object set that's related the foreign key and dot all
    #in order to get all of the related foreign key objects.
    questions = orig_survey.question_set.all()
    #we got all the question and put them in questions.

#***
    #lets get question IDs from the post request then save these original IDs to our DB.
    for question in questions:
        question_post = request.POST['question'+str(question.id)]
        QA = QuestionAnswer()
        #set question answer answer so what choice of the
        QA.answer.answer = Choice.objects.get(id=int(question_post))
        QA.survey_answer = answer
        QA.save()
    answer.save()
    return render(request, 'survey-complete.html', {})

def admin_login(request):
    admin_usname = request.POST['username']
    admin_password = request.POST['password']
    user = authenticate(username=admin_usname, password=admin_password)
    if user is not None:
        login(request, user)
        return redirect('admin-panel')
    return render(request, 'main.html', {'login':False})
def admin_panel(request):
    surveys = Survey.objects.all()
    ctx = {'surveys': surveys}
    return render(request, 'admin-panel.html', ctx)
def survey_delete(request):
    #the name of the hidden input is 'sv_delete' and the value is survey,id
    survey_deleteion = request.POST['sv_delete']
    #based the id that sent , we should get it from DB
    sv_del = Survey.objects.get(id=int(survey_deleteion))
    sv_del.delete()
    return redirect('admin-panel')

#***
#see the answers based on a particualr survey id
def admin_answers(request, survey_id):
    #r'^admin_panel/survey/(?P<survey_id>\d+)/$
    #the survey_id is in the url
    survey = Survey.objects.get(id=survey_id)
    answers = survey.surveyanswer_set.all()
    ctx = {
        'answers': answers,
        'survey': survey,
    }
    return render(request, 'admin-survey-detail.html', ctx)

#we need to give the admin , th ability to creates surveys
def survey_create_view(request):
    return render(request, 'survey-create.html', {})

def question_add_view(request):
    return render(request, 'question-add.html', {})

def choice_add_view(request):
    #get the id from the session and populate Question
    question = Question.objects.get(id=int(request.session['current_survey']))
    return render(request, 'choice-add.html', {'question': question})

def survey_create(request):
    newSurvey = Survey()
    #survey title is the name in the input that pass title
    newSurvey.title = request.POST['survey_title']
    newSurvey.save()
    #then let set our session the current survey to new surveys ID
    #we save the id to the session , then we can add question to this special survey by calling the content of this session(id)
    request.session['current_survey'] = newSurvey.id
    return redirect('admin-question-add-view')


#adding question to the particular  survey
def question_add(request):
    #lets get the survey we are working with from the session
    survey_add = Survey.objects.get(id= int(request.session['current_survey']))
    new_question = Question()
    new_question.question_text = request.POST['question_text']
    #use the survey_add and ,add a question to the survey -> question set like this
    survey_add.question_set.add(new_question)
    new_question.save()
    survey_add.save()
    #then make sure to pass the current question to the session
    request.session['current_question'] = new_question.id
    return redirect('admin-choice-add-view')

def choice_add(request):
    #lets now get the question object from the session
    question = Question.objects.get(id=int(request.session['current_question']))
    #we are using the session here to pass the question id
    newChoice = Choice()
    newChoice.choice_text = request.POST['choice_text']
    question.choice_set.add(newChoice)
    newChoice.save()
    question.save()
    return redirect('admin-choice-add-view')
