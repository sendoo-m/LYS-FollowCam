import django_filters
from .models import Follow

class FollowFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(lookup_expr='icontains')
    created_at = django_filters.DateTimeFilter(lookup_expr='icontains')
    building = django_filters.CharFilter(lookup_expr='icontains')
    dvr = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Follow
        fields = ['user', 'created_at', 'building', 'dvr']
