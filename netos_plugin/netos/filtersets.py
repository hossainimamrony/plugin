from dcim.models.devices import Manufacturer
from netbox.filtersets import NetBoxModelFilterSet
import django_filters

from . import models


class NetosHardwareInventoryFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = models.NetosHardwareInventory
        fields = (
            'id',
            'product_base_pid',
            'product_category',
            'product_data_sheet_url',
            'product_dimensions_format',
            'product_dimensions_value',
            #'product_export_compliance',
            'product_form_factor',
            'product_image_large',
            'product_image_small',
            'product_manufacturer',
            'product_name',
            'product_orderable_pid',
            'product_orderable_status',
            'product_related_software_versions',
            'product_related_software_versions',
            'product_release_date',
            'product_series',
            'product_subcategory',
            'product_support_page',
            'product_type',
            'product_visio_stencils',
            'product_weight',
        )

    # def search(self, queryset, name, value):
    #     return queryset.filter(product_name__icontains=value)


class NetosHardwareEolFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = models.NetosHardwareEol
        fields = (
            'id',
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
            'product_id',
            'product_id_description',
            'product_migration_status',
            'record_update_timestamp',
            'vulnerability_date',
        )

class NetosSoftwareInventoryFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = models.NetosSoftwareInventory
        fields = (
            'id',
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
        )
      
class NetosSoftwareCVEFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = models.NetosSoftwareCVE
        fields = (
            'id',
            'cve_id',
            #'data'
        )


class NetosSoftwareBugFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = models.NetosSoftwareBug
        fields = (
            'id',
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


class NetosCVEChangeHistoryFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = models.NetosCVEChangeHistory
        fields = (
            'id',
            'cve_id',
            #'data'
        )


class NetosExportComplianceFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = models.NetosExportCompliance
        fields = (
            'id',
            'product_family',
            'product_id',
            'encryption_status',
            'encryption_strength',
            'oam_field',
            'ccats',
            'ccats_review_date',
            'anssi_file_number',
            'hs_number',
        )


class NetosHardwareCCCFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = models.NetosHardwareCCC
        fields = (
            'id',
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


class NetosReportHardwareFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = models.NetosReportHardware
        fields = (
            'id',
            'announcement_days',
            'maintenance_days',
            'vulnerability_days',
            'support_days',
        )

class NetosSoftwareEolFilterSet(NetBoxModelFilterSet):
    manufacturer_id = django_filters.ModelMultipleChoiceFilter(
        field_name='software_inventory__manufacturer',
        queryset=Manufacturer.objects.all(),
        label='Manufacturer (ID)',
    )

    class Meta:
        model = models.NetosSoftwareEol
        fields = (
            'id',
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
            'product_id',
            'product_id_description',
            'product_migration_status',
            'record_update_timestamp',
            'vulnerability_date',
        )
