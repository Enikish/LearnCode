from django.contrib import admin

# Register your models here.

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Question name", {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Choice text", {"fields": ["choice_text"]}),
        ("Votes", {"fields": ["votes"]}),
        ("Question", {"fields": ["question"], "classes": ["collapse"]}),
    ]
    list_display = ["choice_text", "question", "votes"]
    search_fields = ["choice_text"]
    list_filter = ["question", "votes"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
