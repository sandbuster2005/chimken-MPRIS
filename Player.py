from sdbus import (
    DbusInterfaceCommonAsync,
    dbus_method_async,
    dbus_property_async,
    DbusPropertyEmitsChangeFlag
)

class MediaPlayer2Player(DbusInterfaceCommonAsync, interface_name='org.mpris.MediaPlayer2.Player'):

    def __init__(self, action_queue):
        self._playback_status = "Playing"
        super().__init__()
        self.action_queue = action_queue

    @dbus_property_async('s', flags=DbusPropertyEmitsChangeFlag )
    def playback_status(self):
        # In a real app, query your state variables here
        return "Playing"

    @playback_status.setter
    def playback_status_setter(self, new_status: str):
        self._playback_status = new_status


    @dbus_method_async('')
    async def play(self):
        self.action_queue.append("PLAY")

    @dbus_method_async('')
    async def pause(self):
        self.action_queue.append("PAUSE")

    @dbus_method_async('')
    async def play_pause(self):
        self.action_queue.append("PLAY_PAUSE")

    @dbus_method_async('')
    async def next(self):
        self.action_queue.append("NEXT")

    @dbus_method_async('')
    async def previous(self):
        self.action_queue.append("PREVIOUS")
