from django.contrib import admin

from .models import Poll, Choice, Vote


class ChoiceInline(admin.TabularInline):
    model = Choice


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('owner', 'text', 'pub_date', 'active')
    inlines = (ChoiceInline,)
    fieldsets = (
        ('general', {'fields': ('owner',)}),
        ('other', {'fields': ('text', 'pub_date', 'active')})
    )


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('poll', 'choice_text')


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'poll', 'choice')
