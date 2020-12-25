from django.contrib.admin import ModelAdmin, register
from django.utils.html import format_html
from filebrowser.settings import ADMIN_THUMBNAIL

from common.models import Example


class BaseModelAdmin(ModelAdmin):
    readonly_fields = ('created', 'updated')


class SlugableModelAdmin(ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


CREATED_UPDATED = (
    'Created / Modified',
    {
        'classes': ('grp-collapse grp-closed',),
        'fields': ('created', 'modified'),
        'description': 'Info about the time this entry was added here or updated',
    },
)


@register(Example)
class ExampleAdmin(ModelAdmin):
    change_list_template = 'admin/change_list_filter_sidebar.html'
    change_list_filter_template = 'admin/filter_listing.html'
    fieldsets = (
        (None, {'fields': ('name', 'image', 'status', 'status_changed', 'published_at')}),
        CREATED_UPDATED,
    )
    list_display = ('name', 'status', 'status_changed', 'published_at', 'image_thumbnail')
    list_filter = ('created', 'modified')
    list_editable = ('status',)
    readonly_fields = ('created', 'modified', 'status_changed', 'published_at')

    @staticmethod
    def image_thumbnail(obj):
        if obj.image and obj.image.filetype == 'Image':
            return format_html(f'<img src="{obj.image.version_generate(ADMIN_THUMBNAIL).url}" />')
        return ''

    image_thumbnail.allow_tags = True
    image_thumbnail.short_description = 'Thumbnail'
