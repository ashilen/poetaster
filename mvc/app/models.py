from django.db import models
from django.contrib.postgres.fields import JSONField


class Poem(models.Model):
    author = models.ForeignKey('app.Author')
    tags = models.ManyToManyField('app.Tag')

    # needs custom field
    body = JSONField()


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    birth_date = models.DateField()
    death_date = models.DateField(null=True)

    nationality = models.CharField(max_length=100, null=True)


class TagType(models.Model):
    POEM_SCOPE = 'POEM'
    LINE_SCOPE = 'LINE'
    WORD_SCOPE = 'WORD'

    scope = models.CharField(max_length=50, choices=(
        POEM_SCOPE,
        LINE_SCOPE,
        WORD_SCOPE
    ))


class Tag(models.Model):
    tag_type = models.ForeignKey('app.TagType')

    # needs custom field
    span = JSONField()

