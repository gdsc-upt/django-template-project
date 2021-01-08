from django.contrib.admin import ModelAdmin, register

from common.models import Example


class BaseModelAdmin(ModelAdmin):
    list_filter = ('created', 'modified')
    readonly_fields = ('created', 'modified')


class SlugableModelAdmin(ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


CREATED_MODIFIED = (
    'Created / Modified',
    {
        'fields': ('created', 'modified'),
        'description': 'Info about the time this entry was added here or updated',
    },
)


@register(Example)
class ExampleAdmin(BaseModelAdmin):
    fieldsets = (
        (None, {'fields': ('name', 'status', 'status_changed', 'published_at')}),
        CREATED_MODIFIED,
    )
    list_display = ('name', 'status', 'status_changed', 'published_at')
    list_editable = ('status',)
    readonly_fields = BaseModelAdmin.readonly_fields + ('status_changed', 'published_at')
