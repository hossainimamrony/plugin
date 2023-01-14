from netbox.api.viewsets import NetBoxModelViewSet

from .. import filtersets, models
from . import serializers


class NetosHardwareInventoryViewSet(NetBoxModelViewSet):
    queryset = models.NetosHardwareInventory.objects.all()
    serializer_class = serializers.NetosHardwareInventorySerializer
    filterset_class = filtersets.NetosHardwareInventoryFilterSet


class NetosHardwareEolViewSet(NetBoxModelViewSet):
    queryset = models.NetosHardwareEol.objects.all()
    serializer_class = serializers.NetosHardwareEolSerializer
    filterset_class = filtersets.NetosHardwareEolFilterSet


class NetosSoftwareInventoryViewSet(NetBoxModelViewSet):
    queryset = models.NetosSoftwareInventory.objects.all()
    serializer_class = serializers.NetosSoftwareInventorySerializer
    filterset_class = filtersets.NetosSoftwareInventoryFilterSet


class NetosSoftwareCVEViewSet(NetBoxModelViewSet):
    queryset = models.NetosSoftwareCVE.objects.all()
    serializer_class = serializers.NetosSoftwareCVESerializer
    filterset_class = filtersets.NetosSoftwareCVEFilterSet


class NetosCVEChangeHistoryViewSet(NetBoxModelViewSet):
    queryset = models.NetosCVEChangeHistory.objects.all()
    serializer_class = serializers.NetosCVEChangeHistorySerializer
    filterset_class = filtersets.NetosCVEChangeHistoryFilterSet


class NetosSoftwareBugViewSet(NetBoxModelViewSet):
    queryset = models.NetosSoftwareBug.objects.all()
    serializer_class = serializers.NetosSoftwareBugSerializer
    filterset_class = filtersets.NetosSoftwareBugFilterSet


class NetosComplianceViewSet(NetBoxModelViewSet):
    queryset = models.NetosExportCompliance.objects.all()
    serializer_class = serializers.NetosExportComplianceSerializer
    filterset_class = filtersets.NetosExportComplianceFilterSet


class NetosHardwareCCCViewSet(NetBoxModelViewSet):
    queryset = models.NetosHardwareCCC.objects.all()
    serializer_class = serializers.NetosHardwareCCCSerialzier
    filterset_class = filtersets.NetosHardwareCCCFilterSet


class NetosReportHardwareViewSet(NetBoxModelViewSet):
    queryset = models.NetosReportHardware.objects.all()
    serializer_class = serializers.NetosReportHardwareSerializer
    filterset_class = filtersets.NetosReportHardwareFilterSet

class NetosSoftwareEolViewSet(NetBoxModelViewSet):
    queryset = models.NetosSoftwareEol.objects.all()
    serializer_class = serializers.NetosSoftwareEolSerializer
    filterset_class = filtersets.NetosSoftwareEolFilterSet
