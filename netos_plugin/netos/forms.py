from django import forms
from dcim.models.devices import Manufacturer
from netbox.forms import NetBoxModelForm
from netbox.forms.base import NetBoxModelFilterSetForm
from utilities.forms.fields.dynamic import DynamicModelMultipleChoiceField
from utilities.forms.fields.fields import SlugField
from utilities.forms.widgets import DatePicker, DateTimePicker
from django.utils.translation import gettext as _

from . import models


class NetosHardwareInventoryForm(NetBoxModelForm):
    product_release_date = forms.DateField(required=True, widget=DatePicker())

    class Meta:
        model = models.NetosHardwareInventory
        fields = (
            'product_base_pid',
            'product_category',
            'product_data_sheet_url',
            'product_dimensions_format',
            'product_dimensions_value',
            'product_form_factor',
            'product_image_large',
            'product_image_small',
            'product_manufacturer',
            'product_name',
            'product_orderable_pid',
            'product_orderable_status',
            'product_related_software_versions',
            'product_release_date',
            'product_series',
            'product_subcategory',
            'product_support_page',
            'product_type',
            'product_visio_stencils',
            'product_weight',
            'device_type',
            'replacement_model',
            'product_raw_json',
        )


class NetosHardwareEolForm(NetBoxModelForm):
    end_of_routine_failure_analysis_date = forms.DateField(required=False, widget=DatePicker())
    end_of_service_contract_renewal_date = forms.DateField(required=False, widget=DatePicker())
    last_day_of_support_date = forms.DateField(required=False, widget=DatePicker())
    last_sale_date = forms.DateField(required=False, widget=DatePicker())
    maintenance_date = forms.DateField(required=False, widget=DatePicker())
    vulnerability_date = forms.DateField(required=False, widget=DatePicker())
    last_day_for_service_contract = forms.DateField(required=False, widget=DatePicker())
    record_update_timestamp = forms.DateTimeField(required=False, widget=DateTimePicker())

    class Meta:
        model = models.NetosHardwareEol

        fields = (
            'product_id',
            'product_id_description',
            'announcement',
            'hardware_inventory',
            'bulletin',
            'bulletin_url',
            'end_of_routine_failure_analysis_date',
            'end_of_service_contract_renewal_date',
            'last_day_for_service_contract',
            'last_day_of_support_date',
            'last_sale_date',
            'maintenance_date',
            'migration_info',
            'migration_option',
            'migration_product_id',
            'migration_product_name',
            'migration_product_url',
            'migration_strategy',
            'product_migration_status',
            'record_update_timestamp',
            'vulnerability_date',
        )

class NetosComplianceForm(NetBoxModelForm):
    ccats_review_date = forms.DateField(required=True, widget=DatePicker())
    hardware_inventory = forms.ModelChoiceField(required=True, queryset=models.NetosHardwareInventory.objects.all())

    class Meta:
        model = models.NetosExportCompliance
        fields = (
            'product_family',
            'hardware_inventory',
            'product_id',
            'encryption_status',
            'encryption_strength',
            'oam_field',
            'ccats',
            'ccats_review_date',
            'anssi_file_number',
            'hs_number',
            'hardware_inventory'
        )


class NetosSoftwareInventoryForm(NetBoxModelForm):
    release_date = forms.DateField(required=True, widget=DatePicker())

    class Meta:
        model = models.NetosSoftwareInventory
        fields = (
            'data_sheet_url',
            'manufacturer',
            'type',
            'release_date',
            'major_release_version',
            'release_train',
            'release_lifecycle',
            'release_version_display_name',
            'train_version_display_name',
            'image_name',
            'image_total_size',
            'image_feature_set',
            'image_description',
            'required_ram',
            'required_flash',
            'manufacturer',
            'device_type',
            'operating_system',
        )


class NetosSoftwareCVEForm(NetBoxModelForm):
    class Meta:
        model = models.NetosSoftwareCVE
        fields = (
            'cve_id',
            'data',
            'software_inventories',
        )


class NetosSoftwareBugForm(NetBoxModelForm):
    last_modified_date = forms.DateField(required=True, widget=DatePicker())

    class Meta:
        model = models.NetosSoftwareBug
        fields = (
            'bug_id',
            'base_product_id',
            'product',
            'headline',
            'description',
            'severity',
            'status',
            'behavior_changed',
            'last_modified_date',
            'duplicate_id',
            'known_affected_releases',
            'known_fixed_releases',
            'support_case_count',
            'software_inventories',
        )



class NetosCVEChangeHistoryForm(NetBoxModelForm):
    class Meta:
        model = models.NetosCVEChangeHistory
        fields = (
            'cve_id',
            'data',
        )


class NetosHardwareCCCForm(NetBoxModelForm):
    class Meta:
        model = models.NetosHardwareCCC
        fields = (
            'category',
            'name',
            'manufacturer',
            'scheme',
            'assurance_level',
            'protection_profile',
            'certification_date',
            'archived_date',
            'certification_report_url',
            'security_target_url',
            'maintenance_date',
            'maintenance_title',
            'maintenance_report',
            'maintenance_st',
        )


class NetosReportHardwareForm(NetBoxModelForm):
    class Meta:
        model = models.NetosReportHardware
        fields = (
            'announcement_days',
            'maintenance_days',
            'vulnerability_days',
            'support_days',
        )

class NetosSoftwareEolForm(NetBoxModelForm):
    end_of_routine_failure_analysis_date = forms.DateField(required=False, widget=DatePicker())
    end_of_service_contract_renewal_date = forms.DateField(required=False, widget=DatePicker())
    last_day_of_support_date = forms.DateField(required=False, widget=DatePicker())
    last_sale_date = forms.DateField(required=False, widget=DatePicker())
    maintenance_date = forms.DateField(required=False, widget=DatePicker())
    vulnerability_date = forms.DateField(required=False, widget=DatePicker())
    last_day_for_service_contract = forms.DateField(required=False, widget=DatePicker())
    record_update_timestamp = forms.DateTimeField(required=False, widget=DateTimePicker())
    software_inventory = forms.ModelChoiceField(
        queryset=models.NetosSoftwareInventory.objects.all(),
        required=False
    )

    class Meta:
        model = models.NetosSoftwareEol
        fields = (
            'product_id',
            'product_id_description',
            'announcement',
            'bulletin',
            'bulletin_url',
            'end_of_routine_failure_analysis_date',
            'end_of_service_contract_renewal_date',
            'last_day_for_service_contract',
            'last_day_of_support_date',
            'last_sale_date',
            'maintenance_date',
            'migration_info',
            'migration_option',
            'migration_product_id',
            'migration_product_name',
            'migration_product_url',
            'migration_strategy',
            'product_migration_status',
            'record_update_timestamp',
            'vulnerability_date',
            'software_inventory'
        )

###
# Filter
###
class NetosHardwareInvenotryFilterForm(NetBoxModelFilterSetForm):
    model = models.NetosHardwareInventory
    id = forms.IntegerField(required=False)

class NetosHardwareEolFilterForm(NetBoxModelFilterSetForm):
    model = models.NetosHardwareEol
    id = forms.IntegerField(required=False)

class NetosSoftwareInventoryFilterForm(NetBoxModelFilterSetForm):
    model = models.NetosSoftwareInventory
    id = forms.IntegerField(required=False)

class NetosSoftwareCVEFilterForm(NetBoxModelFilterSetForm):
    model = models.NetosSoftwareCVE
    id = forms.IntegerField(required=False)

class NetosSoftwareBugFilterForm(NetBoxModelFilterSetForm):
    model = models.NetosSoftwareBug
    id = forms.IntegerField(required=False)

class NetosCVEChangeHistoryFilterForm(NetBoxModelFilterSetForm):
    model = models.NetosCVEChangeHistory
    id = forms.IntegerField(required=False)

class NetosComplianceFilterForm(NetBoxModelFilterSetForm):
    model = models.NetosExportCompliance
    id = forms.IntegerField(required=False)

class NetosHardwareCCCFilterForm(NetBoxModelFilterSetForm):
    model = models.NetosHardwareCCC
    id = forms.IntegerField(required=False)

class NetosReportHardwareFilterForm(NetBoxModelFilterSetForm):
    model = models.NetosReportHardware
    id = forms.IntegerField(required=False)

class NetosSoftwareEolFilterForm(NetBoxModelFilterSetForm):
    manufacturer_id = DynamicModelMultipleChoiceField(
        queryset=Manufacturer.objects.all(),
        required=False,
        label=_('Manufacturer')
    )

    model = models.NetosSoftwareEol
    name = forms.CharField(required=False)
