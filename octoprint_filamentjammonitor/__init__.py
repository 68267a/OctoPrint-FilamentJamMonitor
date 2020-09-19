# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import octoprint.plugin

class FilamentJamMonitorPlugin(octoprint.plugin.StartupPlugin,
                      octoprint.plugin.TemplatePlugin,
                      octoprint.plugin.SettingsPlugin,
                      octoprint.plugin.AssetPlugin):

    def on_after_startup(self):
        self._logger.info("Filament Jam Monitor! (more: %s)" % self._settings.get(["url"]))

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

__plugin_name__ = "Filament Jam Monitor"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = FilamentJamMonitorPlugin()