# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from pynput import mouse
import time
import octoprint.plugin

class FilamentJamMonitorPlugin(octoprint.plugin.StartupPlugin,
                      octoprint.plugin.TemplatePlugin,
                      octoprint.plugin.SettingsPlugin,
                      octoprint.plugin.AssetPlugin,
                      octoprint.plugin.ProgressPlugin):

    def get_settings_defaults(self):
        return({
            'enabled': True,
            'monitor_method': 'mouse',  #alt: gpio
            'mouse_leftclick': '',      #could probably do something here
            'mouse_rightclick': '',     #do something when clicked?
            'monitor_pin': '',          #not used if monitor_method is mouse
            'poll_style': 'percent',    #alt: timer
            'poll_interval': 2,         #every 2%
            'poll_timer': 10,           #how long to monitor, in seconds
            'movement_counter': 0,      #DO NOT MODIFY
            'movement_threshold': 100,  #How much movement should we detect before it's "ok"
            'movement_fail_count': 3,   #how many times should the check fail before abort?
            'stop_print': True,         #should we stop the print?
            'stop_type': 'stop',        #stop or pause
            'notify': False,            #should we notify? (not implemented)
            'notify_who': ''            #who should we notify?
            'usage_enabled': False,     #how much filament was used
            'usage_rate': '',           #the amount of filament per scroll? ADVANCED!!
            'usage_log_location': ''    #where to log filament usage.
        })

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

    def filament_moved(x,y):
        global self.movement_counter, self.movement_threshold
        self.movement_counter += 1
    
    def monitor_button(x,y,button,pressed):
        self._logger.info('Button '+button+' pressed')
    def monitor_scroll(x,y,dx,dy):
        self._logger.info('Scroll '.format(
            'down' if dy <0 else 'up', (x,y)
        ))

    #https://github.com/jneilliii/OctoPrint-Tasmota/blob/7b8fb53a62d73bad4d7e73012e2db7c738748685/octoprint_tasmota/__init__.py#L257-L261
    def on_print_progress(storage,path,progress):
        read_movement

    def read_movement():
        global self.movement_fail_count, 
            self.movement_counter,
            self.movement_threshold

        listener = mouse.Listener(
            on_move=filament_moved,
            on_click=monitor_button,
            on_scroll=monitor_scroll)
        
        try:
            listener.start()
            time.sleep(self.poll_timer)
            listener.stop
        except Exception as e:
            self._logger.error(e)

        movement = str.format(
            self.movement_counter'/'self.movement_threshold
        )

        if self.movement_threshold != 0:
            if self.movement_counter > self.movement_threshold:
                self._logger.info("Reached movement threshold "+movement)
            else:
                self.movement_fail_count -= 1
                if self.movement_fail_count > 0:
                    self._logger.warn("FAILURE #" +self.movement_fail_count+" TO DETECT SUFFICIENT FILAMENT MOVEMENT "+movement)
                else:
                    raise RuntimeError("Did not reach movement threshold "+movement)
                    if self.stop_print:
                        self._logger.error("HOW DO I STOP THIS THING")                
                    else:
                        self._logger.warn("Not stopping")
                        self.movement_threshold = 0 # we get it, shut up
        elif self.movement_threshold == 0:
            ignoreThis = "This is a placeholder that does nothing and isn't referenced anywhere"
        else:
            raise ValueError("This shouldn't happen. "+str(self.movement_threshold))

__plugin_name__ = "Filament Jam Monitor"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = FilamentJamMonitorPlugin()
