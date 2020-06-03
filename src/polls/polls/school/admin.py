from django.contrib import admin

from .models import Student, Courses, Client, Reprezentant
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'an')
    search_fields = ('title', 'username', 'email')
    fieldsets = [
                (None, {
										'fields': ['title', ],
										#'classes': ('collapse', )
                }), 
                ('Advanced Options', {
										'fields': ['an'],
										'classes': ('collapse', )
                })
                ]
    hidden_fields = ('an', )
    #exclude = ('an', )
    list_filter = ('an', )

class ClientInline(admin.TabularInline):
    model = Client


class RepAdmin(admin.ModelAdmin):
    inlines = [ClientInline]


admin.site.register(Student)
admin.site.register(Courses, CourseAdmin)
admin.site.register(Client)
admin.site.register(Reprezentant, RepAdmin)
