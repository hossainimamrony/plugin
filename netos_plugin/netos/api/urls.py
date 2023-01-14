from netbox.api.routers import NetBoxRouter

from . import views

app_name = 'netos'
router = NetBoxRouter()
router.register('hardware_inventory',  views.NetosHardwareInventoryViewSet)
router.register('hardware_eol',        views.NetosHardwareEolViewSet)
router.register('software_inventory',  views.NetosSoftwareInventoryViewSet)
router.register('software_bug',        views.NetosSoftwareBugViewSet)
router.register('software_cve',        views.NetosSoftwareCVEViewSet)
router.register('software_eol',        views.NetosSoftwareEolViewSet)
router.register('cve_change_history',  views.NetosCVEChangeHistoryViewSet)
router.register('export_compliance',   views.NetosComplianceViewSet)
router.register('hardware_ccc',        views.NetosHardwareCCCViewSet)
router.register('report_hardware',     views.NetosReportHardwareViewSet)

urlpatterns = router.urls
