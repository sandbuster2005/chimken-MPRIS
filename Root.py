from sdbus import (
    DbusInterfaceCommonAsync,
    dbus_method_async,
    dbus_property_async,
    DbusPropertyEmitsChangeFlag

)

class MediaPlayer2Root(DbusInterfaceCommonAsync, interface_name='org.mpris.MediaPlayer2'):

    def __init__(self, action_queue):
         super().__init__()
         self.action_queue = action_queue

    @dbus_property_async('b')
    def can_quit(self) -> bool:
        return True

    @dbus_property_async('b')
    def can_raise(self) -> bool:
        return False

    @dbus_property_async('s')
    def desktop_entry(self) -> str:
        return "my-custom-tui"

    @dbus_method_async('')
    async def quit(self) -> None:
        self.action_queue.append("QUIT")
