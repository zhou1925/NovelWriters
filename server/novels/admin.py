from django.contrib import admin
from .models import Novel, Chapter


class ChapterInline(admin.StackedInline):
    model = Chapter

@admin.register(Novel)
class NovelAdmin(admin.ModelAdmin):
    inlines = [ChapterInline]


