# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import octoprint.plugin

class FilamentJamMonitorPlugin(octoprint.plugin.StartupPlugin,
                      octoprint.plugin.TemplatePlugin,
                      octoprint.plugin.SettingsPlugin,
                      octoprint.plugin.AssetPlugin,
                      octoprint.plugin.ProgressPlugin):

    def get_settings_defaults(self):
        return dict(url="https://en.wikipedia.org/wiki/Hello_world")

    def get_template_configs(self):
        return [dict(type="settings", custom_bindings=False)]

    def get_assets(self):
        return dict(
            js=["js/filamentjammonitor.js"],
            css=["css/filamentjammonitor.css"],
            less=["less/filamentjammonitor.less"]
        )

    def on_after_startup(self):
        self._logger.info("Filament Jam Monitor! (more: %s)" % self._settings.get(["url"]))

    #https://github.com/jneilliii/OctoPrint-Tasmota/blob/7b8fb53a62d73bad4d7e73012e2db7c738748685/octoprint_tasmota/__init__.py#L257-L261
    def on_print_progress(storage,path,progress):
        readMouse

__plugin_name__ = "Filament Jam Monitor"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = FilamentJamMonitorPlugin()