from netbox.views import generic

from . import filtersets, forms, models, tables
from django.db.models import F, Q, Case, When, FloatField
from django.db.models import ManyToManyField, Count

import datetime as dt

###
# NetosHardwareInventory
##


class NetosHardwareInventoryView(generic.ObjectView):
    template_name = 'netos/hardware_inventory/hardware_inventory.html'
    queryset = models.NetosHardwareInventory.objects.all()


class NetosHardwareInventoryListView(generic.ObjectListView):
    queryset = models.NetosHardwareInventory.objects.all()
    table = tables.NetosHardwareInventoryTable
    filterset = filtersets.NetosHardwareInventoryFilterSet
    filterset_form = forms.NetosHardwareInvenotryFilterForm


class NetosHardwareInventoryEditView(generic.ObjectEditView):
    queryset = models.NetosHardwareInventory.objects.all()
    form = forms.NetosHardwareInventoryForm


class NetosHardwareInventoryDeleteView(generic.ObjectDeleteView):
    queryset = models.NetosHardwareInventory.objects.all()


class NetosHardwareInventoryComponentsView(generic.ObjectChildrenView):
    queryset = models.NetosHardwareInventory.objects.all()

    def get_children(self, request, parent):
        return self.child_model.objects.restrict(request.user, 'view').filter(hardware_inventory=parent)

    def get_extra_context(self, request, instance):
        return {
            'active_tab': f"{self.child_model._meta.verbose_name.replace(' ', '-')}",
        }


class NetosHardwareEolComponentsView(NetosHardwareInventoryComponentsView):
    child_model = models.NetosHardwareEol
    template_name = 'netos/hardware_inventory/hardware_eol.html'
    filterset = filtersets.NetosHardwareEolFilterSet
    table = tables.NetosHardwareEolTable


class NetosExportComplianceComponentsView(NetosHardwareInventoryComponentsView):
    child_model = models.NetosExportCompliance
    template_name = 'netos/hardware_inventory/export_compliance.html'
    filterset = filtersets.NetosExportComplianceFilterSet
    table = tables.NetosExportComplianceTable

###
# NetosHardwareEol
###


class NetosHardwareEolView(generic.ObjectView):
    queryset = models.NetosHardwareEol.objects.all()


class NetosHardwareEolListView(generic.ObjectListView):
    queryset = models.NetosHardwareEol.objects.all()
    table = tables.NetosHardwareEolTable
    filterset = filtersets.NetosHardwareEolFilterSet
    filterset_form = forms.NetosHardwareEolFilterForm


class NetosHardwareEolEditView(generic.ObjectEditView):
    queryset = models.NetosHardwareEol.objects.all()
    form = forms.NetosHardwareEolForm


class NetosHardwareEolDeleteView(generic.ObjectDeleteView):
    queryset = models.NetosHardwareEol.objects.all()


###
# NetosSoftwareInventory
###


class NetosSoftwareInventoryView(generic.ObjectView):
    template_name = 'netos/software_inventory/software_inventory.html'
    queryset = models.NetosSoftwareInventory.objects.all()


class NetosSoftwareInventoryListView(generic.ObjectListView):
    queryset = models.NetosSoftwareInventory.objects.all()
    table = tables.NetosSoftwareInventoryTable
    filterset = filtersets.NetosSoftwareInventoryFilterSet
    filterset_form = forms.NetosSoftwareInventoryFilterForm


class NetosSoftwareInventoryEditView(generic.ObjectEditView):
    queryset = models.NetosSoftwareInventory.objects.all()
    form = forms.NetosSoftwareInventoryForm


class NetosSoftwareInventoryDeleteView(generic.ObjectDeleteView):
    queryset = models.NetosSoftwareInventory.objects.all()


class NetosSoftwareInventoryComponentsView(generic.ObjectChildrenView):
    queryset = models.NetosSoftwareInventory.objects.all()

    def get_children(self, request, parent):
        return self.child_model.objects.restrict(request.user, 'view').filter(software_inventories__in=(parent, ))

    def get_extra_context(self, request, instance):
        return {
            'active_tab': f"{self.child_model._meta.verbose_name.replace(' ', '-')}",
        }


class NetosSoftwareBugComponentsView(NetosSoftwareInventoryComponentsView):
    child_model = models.NetosSoftwareBug
    template_name = 'netos/software_inventory/software_bug.html'
    filterset = filtersets.NetosSoftwareBugFilterSet
    table = tables.NetosSoftwareBugTable


class NetosSoftwareCVEomponentsView(NetosSoftwareInventoryComponentsView):
    child_model = models.NetosSoftwareCVE
    template_name = 'netos/software_inventory/software_cve.html'
    filterset = filtersets.NetosSoftwareCVEFilterSet
    table = tables.NetosSoftwareCVETable

###
# NetosSoftwareEol
##
class NetosSoftwareEolView(generic.ObjectView):
    template_name = 'netos/netossoftwareeol.html'
    queryset = models.NetosSoftwareEol.objects.all()


class NetosSoftwareEolListView(generic.ObjectListView):
    queryset = models.NetosSoftwareEol.objects.all()
    table = tables.NetosSoftwareEolTable
    filterset = filtersets.NetosSoftwareEolFilterSet
    filterset_form = forms.NetosSoftwareEolFilterForm
    template_name = 'netos/netossoftwareeol_list.html'

    def get_extra_context(self, request):
        extra_content = super().get_extra_context(request)
        fields = [
            "vulnerability_date",
            "last_day_of_support_date",
            "maintenance_date",
            "last_sale_date",
        ]
            

        eol_stats = []
        curr_date = dt.datetime.now()

        for field in fields:
            eol_stats.append(Count(field,
                                   filter=Q(**{f"{field}__isnull": False}) & Q(**{f"{field}__lte": curr_date.strftime("%Y-%m-%d")})))

        query = (models.NetosSoftwareEol.objects.values("software_inventory__manufacturer__name","software_inventory__manufacturer").annotate(
            vulnerability_count=eol_stats[0],
            last_day_of_support_count=eol_stats[1],
            maintenance_count=eol_stats[2],
            last_sale_count=eol_stats[3],
        ))
    
        stats_by_vendor = {}
        for q in query:
            stats = [q["vulnerability_count"],
                 q["last_day_of_support_count"],
                 q["maintenance_count"],
                 q["last_sale_count"]]
            stats_by_vendor[q["software_inventory__manufacturer__name"]] = {k: v for k, v in zip(fields, stats)}
            # add id for click filter
            stats_by_vendor[q["software_inventory__manufacturer__name"]]["vendor_id"] = q["software_inventory__manufacturer"]
        extra_content["eol_count"] = stats_by_vendor

        return extra_content


class NetosSoftwareEolEditView(generic.ObjectEditView):
    queryset = models.NetosSoftwareEol.objects.all()
    form = forms.NetosSoftwareEolForm


class NetosSoftwareEolDeleteView(generic.ObjectDeleteView):
    queryset = models.NetosSoftwareEol.objects.all()


###
# NetosSoftwareCVE
###

class NetosSoftwareCVEView(generic.ObjectView):
    queryset = models.NetosSoftwareCVE.objects.all()


class NetosSoftwareCVEListView(generic.ObjectListView):
    queryset = models.NetosSoftwareCVE.objects.all()
    table = tables.NetosSoftwareCVETable
    filterset = filtersets.NetosSoftwareCVEFilterSet
    filterset_form = forms.NetosSoftwareCVEFilterForm


class NetosSoftwareCVEEditView(generic.ObjectEditView):
    queryset = models.NetosSoftwareCVE.objects.all()
    form = forms.NetosSoftwareCVEForm


class NetosSoftwareCVEDeleteView(generic.ObjectDeleteView):
    queryset = models.NetosSoftwareCVE.objects.all()

###
# NetosSoftwareBug
###


class NetosSoftwareBugView(generic.ObjectView):
    queryset = models.NetosSoftwareBug.objects.all()


class NetosSoftwareBugListView(generic.ObjectListView):
    queryset = models.NetosSoftwareBug.objects.all()
    table = tables.NetosSoftwareBugTable
    filterset = filtersets.NetosSoftwareBugFilterSet
    filterset_form = forms.NetosSoftwareBugFilterForm


class NetosSoftwareBugEditView(generic.ObjectEditView):
    queryset = models.NetosSoftwareBug.objects.all()
    form = forms.NetosSoftwareBugForm


class NetosSoftwareBugDeleteView(generic.ObjectDeleteView):
    queryset = models.NetosSoftwareBug.objects.all()

###
# NetosCVEChangeHistory
###


class NetosCVEChangeHistoryView(generic.ObjectView):
    queryset = models.NetosCVEChangeHistory.objects.all()


class NetosCVEChangeHistoryListView(generic.ObjectListView):
    queryset = models.NetosCVEChangeHistory.objects.all()
    table = tables.NetosCVEChangeHistoryTable
    filterset = filtersets.NetosCVEChangeHistoryFilterSet
    filterset_form = forms.NetosCVEChangeHistoryFilterForm


class NetosCVEChangeHistoryEditView(generic.ObjectEditView):
    queryset = models.NetosCVEChangeHistory.objects.all()
    form = forms.NetosCVEChangeHistoryForm


class NetosCVEChangeHistoryDeleteView(generic.ObjectDeleteView):
    queryset = models.NetosCVEChangeHistory.objects.all()

###
# NetosCompliance
###


class NetosComplianceView(generic.ObjectView):
    queryset = models.NetosExportCompliance.objects.all()


class NetosComplianceListView(generic.ObjectListView):
    queryset = models.NetosExportCompliance.objects.all()
    table = tables.NetosExportComplianceTable
    filterset = filtersets.NetosExportComplianceFilterSet
    filterset_form = forms.NetosComplianceFilterForm


class NetosComplianceEditView(generic.ObjectEditView):
    queryset = models.NetosExportCompliance.objects.all()
    form = forms.NetosComplianceForm


class NetosComplianceDeleteView(generic.ObjectDeleteView):
    queryset = models.NetosExportCompliance.objects.all()

###
# NetosHardwareCCC
###


class NetosHardwareCCCView(generic.ObjectView):
    queryset = models.NetosHardwareCCC.objects.all()


class NetosHardwareCCCListView(generic.ObjectListView):
    queryset = models.NetosHardwareCCC.objects.all()
    table = tables.NetosHardwareCCCTable
    filterset = filtersets.NetosHardwareCCCFilterSet
    filterset_form = forms.NetosHardwareCCCFilterForm


class NetosHardwareCCCEditView(generic.ObjectEditView):
    queryset = models.NetosHardwareCCC.objects.all()
    form = forms.NetosHardwareCCCForm


class NetosHardwareCCCDeleteView(generic.ObjectDeleteView):
    queryset = models.NetosHardwareCCC.objects.all()

###
# NetosReportHardware
###


class NetosReportHardwareView(generic.ObjectView):
    queryset = models.NetosReportHardware.objects.all()


class NetosReportHardwareListView(generic.ObjectListView):
    queryset = models.NetosReportHardware.objects.all()
    table = tables.NetosReportHardwareTable
    filterset = filtersets.NetosReportHardwareFilterSet
    filterset_form = forms.NetosReportHardwareFilterForm


class NetosReportHardwareEditView(generic.ObjectEditView):
    queryset = models.NetosReportHardware.objects.all()
    form = forms.NetosReportHardwareForm


class NetosReportHardwareDeleteView(generic.ObjectDeleteView):
    queryset = models.NetosReportHardware.objects.all()
