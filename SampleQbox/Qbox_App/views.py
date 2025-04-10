from django.shortcuts import render, redirect, get_object_or_404
from .forms import Login_Form, RegistrationForm, AddQuestionsForm, AddAnswersForm
from django.contrib.auth.models import User
from .models import Questions, Answers, Likes
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.


def RegistrationView(request):
    form = RegistrationForm(request.POST or None)
    print(request.POST, "ffff")
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(
                username=username, password=password, email=email)
            user.save()
            return redirect('login')
    return render(request, 'register.html', {'form': form})


def Login_view(request):
    form = Login_Form(request.POST or None)
    ErrorMessage = ""
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('QboxHome')
            else:
                ErrorMessage = "Given username or password is not valid"
    return render(request, 'login.html', {'form': form, 'ErrorMessage': ErrorMessage})


def Logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def QboxHome_View(request):
    all_questions = Questions.objects.all().prefetch_related(
        'answers__likes').order_by('-created_at')
    user_liked_answer_ids = Likes.objects.filter(
        user=request.user).values_list('answers_id', flat=True)

    # user = request.user
    return render(request, 'QboxHome.html', {
        "user": request.user,
        "all_questions": all_questions,
        "user_liked_answer_ids": list(user_liked_answer_ids),
    })


@login_required(login_url='login')
def AddQuestionsView(request):
    form = AddQuestionsForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            questions = form.save(commit=False)
            questions.user = request.user
            questions.save()
            return redirect('QboxHome')
    return render(request, 'Add_Question.html', {'form': form})

@login_required(login_url='login')
def AddAnswerView(request, question_id):
    question = get_object_or_404(Questions, id=question_id)
    form = AddAnswersForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            ans = form.save(commit=False)
            ans.user = request.user
            ans.questions = question
            ans.save()
            return redirect('QboxHome')
    return render(request, 'AddAnswer.html', {'form': form, 'question': question})

@login_required(login_url='login')
def Like_Answers(request, answer_id):
    answer = get_object_or_404(Answers, id=answer_id)
    like, created = Likes.objects.get_or_create(
        user=request.user, answers=answer)
    if not created:
        like.delete()
        liked = False
    else:
        liked = True

    return JsonResponse({
        'liked': liked,
        'like_count': answer.likes.count(),
    })
