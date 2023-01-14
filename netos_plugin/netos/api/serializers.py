from dcim.api.nested_serializers import NestedDeviceTypeSerializer
from netbox.api.serializers import NetBoxModelSerializer

from .. import models


class NetosHardwareInventorySerializer(NetBoxModelSerializer):
    device_type = NestedDeviceTypeSerializer()

    class Meta:
        model = models.NetosHardwareInventory
        fields = (
            'pk',
            'product_base_pid',
            'product_category',
            'product_data_sheet_url',
            'product_dimensions_format',
            'product_dimensions_value',
            # 'product_export_compliance',
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
            'product_raw_json',
            'device_type',
            'replacement_model',
        )


class NetosHardwareEolSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.NetosHardwareEol

        fields = (
            'pk',
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
            'hardware_inventory',
        )


class NetosSoftwareInventorySerializer(NetBoxModelSerializer):
    class Meta:
        model = models.NetosSoftwareInventory
        fields = (
            'pk',
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
            'device_type',
        )


class NetosSoftwareCVESerializer(NetBoxModelSerializer):
    class Meta:
        model = models.NetosSoftwareCVE
        fields = (
            'pk',
            'cve_id',
            'data'
        )


class NetosCVEChangeHistorySerializer(NetBoxModelSerializer):
    class Meta:
        model = models.NetosCVEChangeHistory
        fields = (
            'pk',
            'cve_id',
            'data'
        )


class NetosSoftwareBugSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.NetosSoftwareBug
        fields = (
            'pk',
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


class NetosExportComplianceSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.NetosExportCompliance
        fields = (
            'pk',
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


class NetosHardwareCCCSerialzier(NetBoxModelSerializer):
    class Meta:
        model = models.NetosHardwareCCC
        fields = (
            'pk',
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


class NetosReportHardwareSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.NetosReportHardware
        fields = (
            'pk',
            'announcement_days',
            'maintenance_days',
            'vulnerability_days',
            'support_days',
        )

class NetosSoftwareEolSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.NetosSoftwareEol
        fields = (
            'pk',
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
            'software_inventory'
        )

