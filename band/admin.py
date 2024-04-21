from django.contrib import admin
from .models import Song, Choice

# Register your models here.
admin.site.site_header = "Admin"
admin.site.site_title = "Admin Area"
admin.site.index_title = "Welcome to the Band Admin Area"

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class SongAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['song_text']}), ('Date Information', {'fields':
                ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInLine]

admin.site.register(Song, SongAdmin)
