# from django.conf.urls import patterns, include, url
# import views
# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'simple_survey.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
#     url(r'^survey/(?P<object_id>\d+)/$', views.survey_view, name = "survey-detail"),
#     url(r'^$', views.index, name="root"),
#     url(r'^survey_fill/$', views.survey_fill, name= "fill-survey"),
#     url(r'^survey_load/$', views.load_survey, name= "load-survey"),
#     url(r'^admin_login/$', views.admin_login, name= "admin-login"),
#     url(r'^admin_panel/$', views.admin_panel, name= "admin-panel"),
#     url(r'^admin_panel/survey/(?P<survey_id>\d+)/$', views.admin_answers , name = "answer-detail"),
#     url(r'^admin_panel/survey_create_view/$', views.survey_create_view, name= "admin-survey-create-view"),
#     url(r'^admin_panel/survey_create/$', views.survey_create, name= "admin-survey-create"),
#     url(r'^admin_panel/question_add_view/$', views.question_add_view, name= "admin-question-add-view"),
#     url(r'^admin_panel/question_add/$', views.question_add, name= "admin-question-add"),
#     url(r'^admin_panel/choice_add_view/$', views.choice_add_view, name= "admin-choice-add-view"),
#     url(r'^admin_panel/choice_add/$', views.choice_add, name= "admin-choice-add"),
#     url(r'^admin_panel/survey_delete/$', views.survey_delete, name= "admin-survey-delete"),
# )


#django 2
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="root"),
    path('survey_load/', views.load_survey, name="load-survey"),
    path('survey/<int:survey_id>/', views.survey_view, name="survey_detail"),
    path('survey_fill/', views.survey_fill, name="fill-survey"),

    # in template
    #url 'answer-detail' survey.id
    path('admin_login/', views.admin_login, name="admin-login"),
    path('admin_panel/', views.admin_panel, name="admin-panel"),
    path('admin_panel/survey_delete/', views.survey_delete, name="admin-survey-delete"),
    path('admin_panel/survey/<int:survey_id>/', views.admin_answers, name="answer-detail"),

    path('admin_panel/survey_create_view/', views.survey_create_view, name="admin-survey-create-view"),
    path('admin_panel/survey_create/', views.survey_create, name="admin-survey-create"),
    path('admin_panel/question_add_view/', views.question_add_view, name="admin-question-add-view"),
    path('admin_panel/question_add/', views.question_add, name="admin-question-add"),
    path('admin_panel/choice_add_view/', views.choice_add_view, name="admin-choice-add-view"),
    path('admin_panel/choice_add/', views.choice_add, name="admin-choice-add"),


]

#we are getting survey.id from hidden input name