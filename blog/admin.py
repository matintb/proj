from django.contrib import admin
from blog.models import post,Category,comments
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
# @admin.register(post)
# class PostAdmin(admin.ModelAdmin):
    
    
class PostAdmin(SummernoteModelAdmin):
    # dar site admin mitavan bar asas zaman sakht negah kard
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    # faghat title ghabel moshahede bashe dar admin
    # fields = (title,)
    # exclude = (title,)
    list_display = ('title','author','status','login_require','created_date','published_date')
    list_filter = ('status','author')
    # list_filter = ('status',)
    # ordering = ('created_date',)
    search_fields = ('title','content')
    # ordering = ('-created_date',)
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name','Post','approved','created_date')
    list_filter = ('Post','approved')
    search_fields = ('name','Post')

admin.site.register(comments,CommentAdmin)
admin.site.register(post,PostAdmin)
admin.site.register(Category)