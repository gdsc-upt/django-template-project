from django.db.models import Model, BooleanField, SlugField, DateTimeField, CharField
from django.utils.html import format_html


class PublishableModel(Model):
    is_published = BooleanField(db_index=True)

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


class Example(CreatedUpdatedModel):
    name = CharField(max_length=300)
    is_published = BooleanField()

    class Meta:
        db_table = 'examples'
