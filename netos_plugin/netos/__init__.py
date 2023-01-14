from extras.plugins import PluginConfig


class NetosConfig(PluginConfig):
    name = 'netos'
    verbose_name = 'Netos'
    description = 'Enrich netbox models'
    version = '0.1.4'
    base_url = 'netos'


config = NetosConfig
