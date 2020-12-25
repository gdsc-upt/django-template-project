from typing import final, AnyStr, Final, Optional

from django.db.models import Model, BooleanField, SlugField, CharField
from django.utils.translation import gettext as _
from filebrowser.fields import FileBrowseField
from model_utils import Choices
from model_utils.fields import MonitorField
from model_utils.models import TimeStampedModel, StatusModel


class PublishableModel(Model):
    is_published = BooleanField(_('is published?'), db_index=True)

    class Meta:
        abstract = True


class SlugableModel(Model):
    slug = SlugField(unique=True, db_index=True)

    class Meta:
        abstract = True


class BaseModel(Model):
    class Meta:
        abstract = True

    def get_change_url(self) -> Optional[AnyStr]:
        from django.urls import reverse_lazy

        return reverse_lazy(
            f'admin:{self._meta.app_label}_{self._meta.model_name}_change',
            args=[str(self.id)],
        )

    @property
    def href(self):
        """
        Use this property in admin dashboard to show this object's name as html anchor
        that redirects to object's edit page
        @return:
        """
        from django.utils.html import format_html

        return format_html(f"<a href='{self.get_change_url()}'>{self}</a>")


@final
class Example(TimeStampedModel, StatusModel, BaseModel):
    """
    Example model docstring that should be visible in Django documentation
    """

    STATUS: Final[Choices] = Choices('published', 'reviewed')

    name = CharField(
        _('example name'),
        max_length=300,
        help_text=_('Some help text that is shown in documentation'),
    )
    image = FileBrowseField(_('example image'), max_length=200, blank=True)
    published_at = MonitorField(
        _('publishing datetime'), monitor='status', when=['published'], editable=False
    )

    def __str__(self) -> AnyStr:
        return str(self.name)

    class Meta:
        db_table = 'examples'
