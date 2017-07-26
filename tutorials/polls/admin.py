from django.contrib import admin

from polls.models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    pass


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['publish_data', 'question_text']
    fieldsets = [(None,                 {'fields':['question_text']}),
                 ('Date information',   {'fields':['publish_data'], 'classes':
                                         ['collapse']
                                         }),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'publish_data', 'was_published_recently')
    list_filter = ['publish_data']
    search_fields = ['question_text']


class ChoiceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)

# Register your models here.
