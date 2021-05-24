from typing import Tuple, Dict

from django.contrib.admin import ModelAdmin, register

from common.models import Example


class BaseModelAdmin(ModelAdmin):
    list_filter: Tuple = ("created", "modified")
    readonly_fields: Tuple = ("created", "modified")


class SlugableModelAdmin(ModelAdmin):
    prepopulated_fields: Dict[str, Tuple] = {"slug": ("name",)}


CREATED_MODIFIED = (
    "Created / Modified",
    {
        "fields": ("created", "modified"),
        "description": "Info about the time this entry was added here or updated",
    },
)


@register(Example)
class ExampleAdmin(BaseModelAdmin):
    fieldsets = (
        (None, {"fields": ("name", "status", "status_changed", "published_at")}),
        CREATED_MODIFIED,
    )
    list_display = ("name", "status", "status_changed", "published_at")
    list_editable = ("status",)
    readonly_fields = BaseModelAdmin.readonly_fields + (
        "status_changed",
        "published_at",
    )
