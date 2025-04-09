from django.contrib import admin
from .models import Questions, Answers, Likes
# Register your models here.
class LikedAdmin(admin.TabularInline):
    model = Likes

class AnswerAdminLikes(admin.ModelAdmin):
    inlines = [LikedAdmin]

admin.site.register(Answers, AnswerAdminLikes)

class AnswersAdmin(admin.TabularInline):
    
    model = Answers

class QuestionsAdmin(admin.ModelAdmin):
    inlines = [AnswersAdmin]

admin.site.register(Questions, QuestionsAdmin)
