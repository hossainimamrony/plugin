from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet

DEFAULT_MAX_LEN = 256


class OrderableStatusChoices(ChoiceSet):
    key = 'NetosHardwareInventory.product_orderable_status'

    CHOICES = [
        ('O', 'Orderable', 'green'),
        ('N', 'Non Orderable', 'gray'),
        ('EOX', 'End of Life', 'red'),
    ]


class SeverityChoices(ChoiceSet):
    key = 'NetosSoftwareBug.severity'

    CHOICES = [
        (1, 'Severity 1 (High)', 'red'),
        (2, 'Severity 2', 'red'),
        (3, 'Severity 3', 'red'),
        (4, 'Severity 4', 'red'),
        (5, 'Severity 5', 'red'),
        (6, 'Severity 6 (Low)', 'red'),
    ]


class StatusChoices(ChoiceSet):
    key = 'NetosSoftwareBug.status'
    CHOICES = [
        ('O', 'Open', 'red'),
        ('F', 'Fixed', 'green'),
        ('T', 'Terminated', 'blue'),
    ]


class OperatingSystemChoices(ChoiceSet):
    key = "NetosSoftwareInventory.operating_system"
    CHOICES = [
        ('Cisco IOS', 'Cisco IOS'),
        ('Cisco IOS-XE', 'Cisco IOS-XE'),
        ('Cisco IOS-XR', 'Cisco IOS-XR'),
        ('Cisco NXOS', 'Cisco NXOS'),
        ('Cisco CatOS', 'Cisco CatOS'),
        ('Juniper Junos', 'Juniper Junos'),
        ('Fortinet FortiOS', 'Fortinet FortiOS'),
        ('Aruba ArubaOS', 'Aruba ArubaOS'),
    ]


class NetosHardwareInventory(NetBoxModel):
    product_base_pid = models.CharField(max_length=40)
    product_category = models.CharField(max_length=100)
    product_data_sheet_url = models.CharField(max_length=100)
    product_dimensions_format = models.CharField(max_length=100)
    product_dimensions_value = models.CharField(max_length=100)
    product_form_factor = models.CharField(max_length=100)
    product_image_large = models.URLField(blank=True, null=True)
    product_image_small = models.URLField(blank=True, null=True)

    product_name = models.CharField(max_length=100)
    product_orderable_pid = models.CharField(max_length=40)
    product_orderable_status = models.CharField(
        max_length=3, choices=OrderableStatusChoices)
    product_related_software_versions = models.CharField(max_length=100)
    product_release_date = models.DateField(null=False)
    product_series = models.CharField(max_length=10)
    product_subcategory = models.CharField(max_length=100)
    product_support_page = models.URLField(blank=True, null=True)
    product_type = models.CharField(max_length=100)
    product_visio_stencils = models.URLField(blank=True, null=True)
    product_weight = models.CharField(max_length=20)
    product_raw_json = models.JSONField()

    product_manufacturer = models.ForeignKey(
        to='dcim.Manufacturer',
        on_delete=models.PROTECT,
        related_name='+',
        null=False
    )

    device_type = models.ForeignKey(
        to='dcim.DeviceType',
        on_delete=models.PROTECT,
        related_name='netos_hardware'
    )

    replacement_model = models.ForeignKey(
        to='NetosHardwareInventory',
        on_delete=models.PROTECT,
        related_name='+',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('product_name', )

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('plugins:netos:netoshardwareinventory', args=[self.pk, ])

    @property
    def hardware_eol_count(self):
        return self.hardware_eol.count()

    @property
    def export_compliance_count(self):
        return self.export_compliance.count()

    def __str__(self) -> str:
        return f"Hardware Inventory {self.pk}"


class NetosHardwareEol(NetBoxModel):
    announcement = models.CharField(max_length=100, null=True, blank=True)
    bulletin = models.CharField(max_length=24, null=True, blank=True)
    bulletin_url = models.URLField(blank=True, null=True)
    end_of_routine_failure_analysis_date = models.DateField(
        null=True, blank=True)
    end_of_service_contract_renewal_date = models.DateField(
        null=True, blank=True)
    last_day_for_service_contract = models.DateField(null=True, blank=True)
    last_day_of_support_date = models.DateField(null=True, blank=True)
    last_sale_date = models.DateField(null=True, blank=True)
    maintenance_date = models.DateField(null=True, blank=True)
    migration_info = models.CharField(max_length=500, null=True, blank=True)
    migration_option = models.CharField(max_length=24, null=True, blank=True)
    migration_product_id = models.CharField(
        max_length=48, null=True, blank=True)
    migration_product_name = models.CharField(
        max_length=200, null=True, blank=True)
    migration_product_url = models.URLField(blank=True, null=True)
    migration_strategy = models.CharField(
        max_length=1334, null=True, blank=True)
    product_id = models.CharField(max_length=48, null=False, blank=False)
    product_id_description = models.CharField(
        max_length=500, null=True, blank=True)
    product_migration_status = models.CharField(
        max_length=100, null=True, blank=True)
    record_update_timestamp = models.DateField(null=True, blank=True)
    vulnerability_date = models.DateField(null=True, blank=True)
    hardware_inventory = models.ForeignKey(
        to=NetosHardwareInventory, on_delete=models.CASCADE, related_name="hardware_eol", null=True, blank=True)

    def __str__(self):
        return f"Hardware EoL {self.product_id}"

    def get_absolute_url(self):
        return reverse('plugins:netos:netoshardwareeol', args=[self.pk, ])


class NetosExportCompliance(NetBoxModel):
    product_family = models.CharField(max_length=DEFAULT_MAX_LEN)
    product_id = models.CharField(max_length=DEFAULT_MAX_LEN)
    encryption_status = models.CharField(max_length=DEFAULT_MAX_LEN)
    encryption_strength = models.CharField(max_length=DEFAULT_MAX_LEN)
    oam_field = models.CharField(max_length=DEFAULT_MAX_LEN)
    ccats = models.CharField(max_length=DEFAULT_MAX_LEN)
    ccats_review_date = models.DateField()
    anssi_file_number = models.CharField(max_length=DEFAULT_MAX_LEN)
    hs_number = models.CharField(max_length=DEFAULT_MAX_LEN)
    hardware_inventory = models.ForeignKey(
        to=NetosHardwareInventory, on_delete=models.CASCADE, related_name="export_compliance")

    def get_absolute_url(self):
        return reverse('plugins:netos:netosexportcompliance', args=[self.pk, ])


class NetosSoftwareInventory(NetBoxModel):
    data_sheet_url = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    release_date = models.CharField(max_length=100)
    major_release_version = models.CharField(max_length=100)
    release_train = models.CharField(max_length=100)
    release_lifecycle = models.CharField(max_length=100)
    release_version_display_name = models.CharField(max_length=100)
    train_version_display_name = models.CharField(max_length=100)
    image_name = models.CharField(max_length=100)
    image_total_size = models.CharField(max_length=100)
    image_feature_set = models.CharField(max_length=100)
    image_description = models.CharField(max_length=100)
    required_ram = models.CharField(max_length=100)
    required_flash = models.CharField(max_length=100)

    operating_system = models.CharField(
        max_length=100, choices=OperatingSystemChoices)

    manufacturer = models.ForeignKey(
        to='dcim.Manufacturer',
        on_delete=models.PROTECT,
        related_name='+',
        null=False
    )

    device_type = models.ForeignKey(
        to='dcim.DeviceType',
        on_delete=models.PROTECT,
        related_name='netos_software'
    )

    def get_absolute_url(self):
        return reverse('plugins:netos:netossoftwareinventory', args=[self.pk, ])

    @property
    def software_cve_count(self):
        return self.cves.count()

    @property
    def software_bug_count(self):
        return self.bugs.count()

    def __str__(self) -> str:
        return f"Software Inventory {self.pk}"


class NetosSoftwareEol(NetBoxModel):
    announcement = models.CharField(max_length=100, null=True, blank=True)
    bulletin = models.CharField(max_length=24, null=True, blank=True)
    bulletin_url = models.URLField(blank=True, null=True)
    end_of_routine_failure_analysis_date = models.DateField(
        null=True, blank=True)
    end_of_service_contract_renewal_date = models.DateField(
        null=True, blank=True)
    last_day_for_service_contract = models.DateField(null=True, blank=True)
    last_day_of_support_date = models.DateField(null=True, blank=True)
    last_sale_date = models.DateField(null=True, blank=True)
    maintenance_date = models.DateField(null=True, blank=True)
    migration_info = models.CharField(max_length=500, null=True, blank=True)
    migration_option = models.CharField(max_length=24, null=True, blank=True)
    migration_product_id = models.CharField(
        max_length=48, null=True, blank=True)
    migration_product_name = models.CharField(
        max_length=200, null=True, blank=True)
    migration_product_url = models.URLField(blank=True, null=True)
    migration_strategy = models.CharField(
        max_length=1334, null=True, blank=True)
    product_id = models.CharField(max_length=48, null=False, blank=False)
    product_id_description = models.CharField(
        max_length=500, null=True, blank=True)
    product_migration_status = models.CharField(
        max_length=100, null=True, blank=True)
    record_update_timestamp = models.DateField(null=True, blank=True)
    vulnerability_date = models.DateField(null=True, blank=True)
    software_inventory = models.ForeignKey(
        to=NetosSoftwareInventory, on_delete=models.CASCADE,
        related_name="software_eol", null=True, blank=True)

    def __str__(self):
        return f"Software EoL {self.product_id}"

    def get_absolute_url(self):
        return reverse('plugins:netos:netossoftwareeol', args=[self.pk, ])


class NetosSoftwareCVE(NetBoxModel):
    """
    NVD Vulnerability Data API version 2.0
    https://csrc.nist.gov/schema/nvd/api/2.0/cve_api_json_2.0.schema
    """
    cve_id = models.CharField(max_length=36, unique=True, db_index=True)
    data = models.JSONField()
    software_inventories = models.ManyToManyField(
        NetosSoftwareInventory, related_name="cves")

    @property
    def vuln_status(self):
        if isinstance(self.data, dict):
            cve = self.data.get("cve")
            if cve and cve.get("vulnStatus"):
                return self.data["cve"]["vulnStatus"]
        else:
            return None

    def get_absolute_url(self):
        return reverse('plugins:netos:netossoftwarecve', args=[self.pk, ])


class NetosCVEChangeHistory(NetBoxModel):
    """
    NVD CVE History API version 2.0
    https://csrc.nist.gov/schema/nvd/api/2.0/history_api_json_2.0.schema
    """
    cve_id = models.ForeignKey(
        to=NetosSoftwareCVE, on_delete=models.CASCADE, related_name='change_history')
    data = models.JSONField()

    def get_absolute_url(self):
        return reverse('plugins:netos:netoscvechangehistory', args=[self.pk, ])


class NetosSoftwareBug(NetBoxModel):
    bug_id = models.CharField(max_length=10)
    base_product_id = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    headline = models.CharField(max_length=72)
    description = models.TextField()
    severity = models.IntegerField(choices=SeverityChoices)
    status = models.CharField(max_length=2, choices=StatusChoices)
    behavior_changed = models.CharField(max_length=2)
    last_modified_date = models.DateField()
    duplicate_id = models.CharField(max_length=20)
    known_affected_releases = models.CharField(max_length=1000)
    known_fixed_releases = models.CharField(max_length=1000)
    support_case_count = models.IntegerField()
    software_inventories = models.ManyToManyField(
        NetosSoftwareInventory, related_name="bugs")

    def get_absolute_url(self):
        return reverse('plugins:netos:netossoftwarebug', args=[self.pk, ])


class NetosHardwareCCC(NetBoxModel):
    category = models.CharField(max_length=DEFAULT_MAX_LEN)
    name = models.CharField(max_length=DEFAULT_MAX_LEN)
    manufacturer = models.CharField(max_length=DEFAULT_MAX_LEN)
    scheme = models.CharField(max_length=DEFAULT_MAX_LEN)
    assurance_level = models.CharField(max_length=DEFAULT_MAX_LEN)
    protection_profile = models.CharField(max_length=DEFAULT_MAX_LEN)
    certification_date = models.DateField()
    archived_date = models.DateField()
    certification_report_url = models.CharField(max_length=DEFAULT_MAX_LEN)
    security_target_url = models.CharField(max_length=DEFAULT_MAX_LEN)
    maintenance_date = models.CharField(max_length=DEFAULT_MAX_LEN)
    maintenance_title = models.CharField(max_length=DEFAULT_MAX_LEN)
    maintenance_report = models.CharField(max_length=DEFAULT_MAX_LEN)
    maintenance_st = models.CharField(max_length=DEFAULT_MAX_LEN)

    def get_absolute_url(self):
        return reverse('plugins:netos:netoshardwareccc', args=[self.pk, ])


class NetosReportHardware(NetBoxModel):
    announcement_days = models.IntegerField()
    maintenance_days = models.IntegerField()
    vulnerability_days = models.IntegerField()
    support_days = models.IntegerField()
