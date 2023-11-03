from django.contrib import admin

from .models import Quiz, Question, Answer, Marks_Of_User

admin.site.register(Quiz)

""" class CategoriesAdmin(admin.ModelAdmin):
    inlines = Categories """
class AnswerInLine(admin.TabularInline):
    model = Answer
    
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine]
    
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)

#admin.site.register(CategoriesAdmin)
admin.site.register(Marks_Of_User)