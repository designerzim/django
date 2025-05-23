from django.contrib import admin

from .models import Choice, Question


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInLine]
    list_display = ["question_text", "pub_date", "was_published_recently"]


# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)