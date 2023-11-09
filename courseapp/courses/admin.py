from django.contrib import admin
from .models import Category, Course, Lesson, Tag
from django.utils.html import mark_safe


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk','name')
    search_fields = ['name']
    list_filter = ['id','name']


class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ['img']

    def img(self, course):
        if course:
            return mark_safe(
                '<img src="/static/{url}" width="120" />' \
                    .format(url=course.image.name)
            )
    class Media:
        css =  {
            'all': ('/static/css/style.css',)
        }

            # Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
admin.site.register(Tag)