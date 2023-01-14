from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

netoshardwareinventory_buttons = [
    PluginMenuButton(
        link='plugins:netos:netoshardwareinventory_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

netossoftwareinventory_buttons = [
    PluginMenuButton(
        link='plugins:netos:netossoftwareinventory_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN      
    )
]
netoshardwareeol_buttons = [
    PluginMenuButton(
        link='plugins:netos:netoshardwareeol_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]
netossoftwarecve_buttons = [
    PluginMenuButton(
        link='plugins:netos:netossoftwarecve_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]
netossoftwarebug_buttons = [
    PluginMenuButton(
        link='plugins:netos:netossoftwarebug_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]
netoscvechangehistory_buttons = [
    PluginMenuButton(
        link='plugins:netos:netoscvechangehistory_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]
netoscompliance_buttons = [
    PluginMenuButton(
        link='plugins:netos:netosexportcompliance_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]
netoshardwareccc_buttons = [
    PluginMenuButton(
        link='plugins:netos:netoshardwareccc_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

netossoftwareeol_buttons = [
    PluginMenuButton(
        link='plugins:netos:netossoftwareeol_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]


menu_items = (
    PluginMenuItem(
        link='plugins:netos:netoshardwareinventory_list',
        link_text='Hardware Inventory',
        buttons=netoshardwareinventory_buttons
    ),
    PluginMenuItem(
        link='plugins:netos:netoshardwareeol_list',
        link_text='Hardware EoL',
        buttons=netoshardwareeol_buttons
    ),
    PluginMenuItem(
        link='plugins:netos:netosexportcompliance_list',
        link_text='Export Compiliance',
        buttons=netoscompliance_buttons
    ),
    PluginMenuItem(
        link='plugins:netos:netossoftwareinventory_list',
        link_text='Software Inventory',
        buttons=netossoftwareinventory_buttons
    ),
    PluginMenuItem(
        link='plugins:netos:netossoftwareeol_list',
        link_text='Software EoL',
        buttons=netossoftwareeol_buttons
    ),
    PluginMenuItem(
        link='plugins:netos:netossoftwarecve_list',
        link_text='Software CVE',
        buttons=netossoftwarecve_buttons
    ),
    PluginMenuItem(
        link='plugins:netos:netossoftwarebug_list',
        link_text='Sofware Bug',
        buttons=netossoftwarebug_buttons
    ),
    PluginMenuItem(
        link='plugins:netos:netoscvechangehistory_list',
        link_text='CVE Change History',
        buttons=netoscvechangehistory_buttons
    ),
    PluginMenuItem(
        link='plugins:netos:netoshardwareccc_list',
        link_text='Hardware CCC',
        buttons=netoshardwareccc_buttons
    )
)
