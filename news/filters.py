import django_filters

from django.forms import DateTimeInput
from django_filters import FilterSet, DateTimeFilter
from .models import Post


class PostFilter(FilterSet):
    categoryType = django_filters.ChoiceFilter(choices=Post.CATEGORY_CHOISES)
    added_after = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
        }