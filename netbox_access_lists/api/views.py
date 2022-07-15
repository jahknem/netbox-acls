from django.db.models import Count

from netbox.api.viewsets import NetBoxModelViewSet

from .. import filtersets, models
from .serializers import AccessListSerializer, AccessListExtendedRuleSerializer, AccessListStandardRuleSerializer


class AccessListViewSet(NetBoxModelViewSet):
    queryset = models.AccessList.objects.prefetch_related(
        'device', 'tags'
    ).annotate(
        rule_count=Count('rules')
    )
    serializer_class = AccessListSerializer
    filterset_class = filtersets.AccessListFilterSet


class AccessListStandardRuleViewSet(NetBoxModelViewSet):
    queryset = models.AccessListStandardRule.objects.prefetch_related(
        'access_list', 'source_prefix', 'tags'
    )
    serializer_class = AccessListStandardRuleSerializer
    filterset_class = filtersets.AccessListStandardRuleFilterSet


class AccessListExtendedRuleViewSet(NetBoxModelViewSet):
    queryset = models.AccessListExtendedRule.objects.prefetch_related(
        'access_list', 'source_prefix', 'destination_prefix', 'tags'
    )
    serializer_class = AccessListExtendedRuleSerializer
    filterset_class = filtersets.AccessListExtendedRuleFilterSet
