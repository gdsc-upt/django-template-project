from typing import final

from django.db.models import Model, BooleanField, SlugField, DateTimeField, CharField
from django.utils.html import format_html
from django.utils.translation import gettext as _


class PublishableModel(Model):
    is_published = BooleanField(_('is published?'), db_index=True)

    class Meta:
        abstract = True


class SlugableModel(Model):
    slug = SlugField(unique=True, db_index=True)

    class Meta:
        abstract = True


class CreatedUpdatedModel(Model):
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def get_change_url(self):
        from django.urls import reverse

        return reverse(
            f'admin:{self._meta.app_label}_{self._meta.model_name}_change',
            args=[str(self.id)],
        )

    def as_href(self):
        return format_html(f"<a href='{self.get_change_url()}'>{self}</a>")


@final
class Example(PublishableModel, CreatedUpdatedModel):
    """
    Example model docstring that should be visible in Django documentation
    """

    name = CharField(
        _('example name'),
        max_length=300,
        help_text=_('Some help text that is shown in documentation'),
    )

    class Meta:
        db_table = 'examples'
