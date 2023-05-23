from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, ArticleScope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        # super().clean()
        for form in self.forms:
            cleaned_form = form.cleaned_data
            print(cleaned_form)
            if not form:
                raise ValidationError('Тут всегда ошибка')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = ScopeInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    list_filter = ['published_at']
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
