from django.contrib import admin
from .models import Song, Choice

# Register your models here.
admin.site.site_header = "Admin"
admin.site.site_title = "Admin Area"
admin.site.index_title = "Welcome to the Band Admin Area"

class ChoiceInLine(admin.TabularInline):
    """
    Inline editing for Choices associated with a Song.

    :param Model model: The model to be edited inline.
    :param int extra: The number of empty forms to display for adding additional choices.
    """
    model = Choice
    extra = 3

class SongAdmin(admin.ModelAdmin):
    """
    Admin interface customization for the Song model.

    :ivar tuple fieldsets: Sets of fields to be displayed in the admin interface.
    :ivar list inlines: List of Inline classes to be included in the admin interface.
    """
    fieldsets = [(None, {'fields': ['song_text']}), ('Date Information', {'fields':
                ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInLine]

admin.site.register(Song, SongAdmin)
