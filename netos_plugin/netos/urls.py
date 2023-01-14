from django.urls import path
from netbox.views.generic.feature_views import (ObjectChangeLogView,
                                                ObjectJournalView)

from . import models, views

urlpatterns = (
    # NetosHardwareInventory
    path('hardware_inventory/', views.NetosHardwareInventoryListView.as_view(), name='netoshardwareinventory_list'),
    path('hardware_inventory/add', views.NetosHardwareInventoryEditView.as_view(), name='netoshardwareinventory_add'),
    path('hardware_inventory/<int:pk>', views.NetosHardwareInventoryView.as_view(), name='netoshardwareinventory'),
    path('hardware_inventory/<int:pk>/edit/', views.NetosHardwareInventoryEditView.as_view(), name='netoshardwareinventory_edit'),
    path('hardware_inventory/<int:pk>/delete/', views.NetosHardwareInventoryDeleteView.as_view(), name='netoshardwareinventory_delete'),
    ## Components
    path('devices/<int:pk>/hardware_eol/', views.NetosHardwareEolComponentsView.as_view(), name='netoshardwareinventory_eol'),
    path('devices/<int:pk>/export_compliance/', views.NetosExportComplianceComponentsView.as_view(), name='netoshardwareinventory_compliance'),
    ## Changelog
    path('hardware_inventory/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='netoshardwareinventory_changelog', kwargs={'model': models.NetosHardwareInventory}),
    path('hardware_inventory/<int:pk>/journal/', ObjectJournalView.as_view(), name='netoshardwareinventory_journal', kwargs={'model': models.NetosHardwareInventory}),

    # NetosHardwareEol
    path('hardware_eol/', views.NetosHardwareEolListView.as_view(), name='netoshardwareeol_list'),
    path('hardware_eol/add', views.NetosHardwareEolEditView.as_view(), name='netoshardwareeol_add'),
    path('hardware_eol/<int:pk>', views.NetosHardwareEolView.as_view(), name='netoshardwareeol'),
    path('hardware_eol/<int:pk>/edit/', views.NetosHardwareEolEditView.as_view(), name='netoshardwareeol_edit'),
    path('hardware_eol/<int:pk>/delete/', views.NetosHardwareEolDeleteView.as_view(), name='netoshardwareeol_delete'),

    path('hardware_eol/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='netoshardwareeol_changelog', kwargs={'model': models.NetosHardwareEol}),
    path('hardware_eol/<int:pk>/journal/', ObjectJournalView.as_view(), name='netoshardwareeol_journal', kwargs={'model': models.NetosHardwareEol}),

    # NetosComplianceView
    path('export_compliance/', views.NetosComplianceListView.as_view(), name='netosexportcompliance_list'),
    path('export_compliance/add', views.NetosComplianceEditView.as_view(), name='netosexportcompliance_add'),
    path('export_compliance/<int:pk>', views.NetosComplianceView.as_view(), name='netosexportcompliance'),
    path('export_compliance/<int:pk>/edit/', views.NetosComplianceEditView.as_view(), name='netosexportcompliance_edit'),
    path('export_compliance/<int:pk>/delete/', views.NetosComplianceDeleteView.as_view(), name='netosexportcompliance_delete'),

    path('export_compliance/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='netosexportcompliance_changelog', kwargs={'model': models.NetosExportCompliance}),
    path('export_compliance/<int:pk>/journal/', ObjectJournalView.as_view(), name='netosexportcompliance_journal', kwargs={'model': models.NetosExportCompliance}),

    # NetosSoftwareInventory
    path('software_inventory/', views.NetosSoftwareInventoryListView.as_view(), name='netossoftwareinventory_list'),
    path('software_inventory/add', views.NetosSoftwareInventoryEditView.as_view(), name='netossoftwareinventory_add'),
    path('software_inventory/<int:pk>', views.NetosSoftwareInventoryView.as_view(), name='netossoftwareinventory'),
    path('software_inventory/<int:pk>/edit/', views.NetosSoftwareInventoryEditView.as_view(), name='netossoftwareinventory_edit'),
    path('software_inventory/<int:pk>/delete/', views.NetosSoftwareInventoryDeleteView.as_view(), name='netossoftwareinventory_delete'),
      
    ## Components
    path('software_inventory/<int:pk>/software_bug/', views.NetosSoftwareBugComponentsView.as_view(), name='netossoftwareinventory_bugs'),
    path('software_inventory/<int:pk>/software_cve/', views.NetosSoftwareCVEomponentsView.as_view(), name='netossoftwareinventory_cves'),
  
    path('software_inventory/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='netossoftwareinventory_changelog', kwargs={'model': models.NetosSoftwareInventory}),
    path('software_inventory/<int:pk>/journal/', ObjectJournalView.as_view(), name='netossoftwareinventory_journal', kwargs={'model': models.NetosSoftwareInventory}),

    # NetosSoftwareCVE
    path('software_cve/', views.NetosSoftwareCVEListView.as_view(), name='netossoftwarecve_list'),
    path('software_cve/add', views.NetosSoftwareCVEEditView.as_view(), name='netossoftwarecve_add'),
    path('software_cve/<int:pk>', views.NetosSoftwareCVEView.as_view(), name='netossoftwarecve'),
    path('software_cve/<int:pk>/edit/', views.NetosSoftwareCVEEditView.as_view(), name='netossoftwarecve_edit'),
    path('software_cve/<int:pk>/delete/', views.NetosSoftwareCVEDeleteView.as_view(), name='netossoftwarecve_delete'),
    
    path('software_cve/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='netossoftwarecve_changelog', kwargs={'model': models.NetosSoftwareCVE}),
    path('software_cve/<int:pk>/journal/', ObjectJournalView.as_view(), name='netossoftwarecve_journal', kwargs={'model': models.NetosSoftwareCVE}),

    # NetosSoftwareBug
    path('software_bug/', views.NetosSoftwareBugListView.as_view(), name='netossoftwarebug_list'),
    path('software_bug/add', views.NetosSoftwareBugEditView.as_view(), name='netossoftwarebug_add'),
    path('software_bug/<int:pk>', views.NetosSoftwareBugView.as_view(), name='netossoftwarebug'),
    path('software_bug/<int:pk>/edit/', views.NetosSoftwareBugEditView.as_view(), name='netossoftwarebug_edit'),
    path('software_bug/<int:pk>/delete/', views.NetosSoftwareBugDeleteView.as_view(), name='netossoftwarebug_delete'),

    path('software_bug/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='netossoftwarebug_changelog', kwargs={'model': models.NetosSoftwareBug}),
    path('software_bug/<int:pk>/journal/', ObjectJournalView.as_view(), name='netossoftwarebug_journal', kwargs={'model': models.NetosSoftwareBug}),

    # NetosCVEChangeHistoryTable
    path('cve_change_history/', views.NetosCVEChangeHistoryListView.as_view(), name='netoscvechangehistory_list'),
    path('cve_change_history/add', views.NetosCVEChangeHistoryEditView.as_view(), name='netoscvechangehistory_add'),
    path('cve_change_history/<int:pk>', views.NetosCVEChangeHistoryView.as_view(), name='netoscvechangehistory'),
    path('cve_change_history/<int:pk>/edit/', views.NetosCVEChangeHistoryEditView.as_view(), name='netoscvechangehistory_edit'),
    path('cve_change_history/<int:pk>/delete/', views.NetosCVEChangeHistoryDeleteView.as_view(), name='netoscvechangehistory_delete'),

    # NetosHardwareCCC
    path('hardware_ccc/', views.NetosHardwareCCCListView.as_view(), name='netoshardwareccc_list'),
    path('hardware_ccc/add', views.NetosHardwareCCCEditView.as_view(), name='netoshardwareccc_add'),
    path('hardware_ccc/<int:pk>', views.NetosHardwareCCCView.as_view(), name='netoshardwareccc'),
    path('hardware_ccc/<int:pk>/edit/', views.NetosHardwareCCCEditView.as_view(), name='netoshardwareccc_edit'),
    path('hardware_ccc/<int:pk>/delete/', views.NetosHardwareCCCDeleteView.as_view(), name='netoshardwareccc_delete'),
    
    # NetosReportHardware
    path('report_hardware/', views.NetosReportHardwareListView.as_view(), name='netosreporthardware_list'),
    path('report_hardware/add', views.NetosReportHardwareEditView.as_view(), name='netosreporthardware_add'),
    path('report_hardware/<int:pk>', views.NetosReportHardwareView.as_view(), name='netosreporthardware'),
    path('report_hardware/<int:pk>/edit/', views.NetosReportHardwareEditView.as_view(), name='netosreporthardware_edit'),
    path('report_hardware/<int:pk>/delete/', views.NetosReportHardwareDeleteView.as_view(), name='netosreporthardware_delete'),

    # NetosSoftwareEol
    path('software_eol/', views.NetosSoftwareEolListView.as_view(), name='netossoftwareeol_list'),
    path('software_eol/add', views.NetosSoftwareEolEditView.as_view(), name='netossoftwareeol_add'),
    path('software_eol/<int:pk>', views.NetosSoftwareEolView.as_view(), name='netossoftwareeol'),
    path('software_eol/<int:pk>/edit/', views.NetosSoftwareEolEditView.as_view(), name='netossoftwareeol_edit'),
    path('software_eol/<int:pk>/delete/', views.NetosSoftwareEolDeleteView.as_view(), name='netossoftwareeol_delete'),

    path('software_eol/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='netossoftwareeol_changelog', kwargs={'model': models.NetosSoftwareEol}),
    path('software_eol/<int:pk>/journal/', ObjectJournalView.as_view(), name='netossoftwareeol_journal', kwargs={'model': models.NetosSoftwareEol}),

)