from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.QboxHome_View, name='QboxHome'),
    path("login/", views.Login_view, name='login'),
    path("logout/", views.Logout_view, name='logout'),
    path("register/", views.RegistrationView, name='register'),
    path("addquestion/", views.AddQuestionsView, name='addquestion'),
    path('answer/<int:question_id>', views.AddAnswerView, name='add_answer'),
    path('like-answer/<int:answer_id>/', views.Like_Answers, name='like_answer')


]
