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

         self._can_quit = True
         self._can_raise = False
         self._can_set_fulscreen = False
         self._has_track_list = False
         self._identity = "ChimkenMuziks"
         self._desktop_entry = "ChimkenMuziks"
         self._supported_uri_schemes = ["file"]
         self._supported_mime_types = ["audio/mpeg"]

    @dbus_property_async('b',  flags=DbusPropertyEmitsChangeFlag)
    def can_quit(self) -> bool:
        return self._can_quit

    @can_quit.setter
    def can_quit_setter(self, new_status: bool):
        self._can_quit = new_status



    @dbus_property_async('b',  flags=DbusPropertyEmitsChangeFlag)
    def can_raise(self) -> bool:
        return self._can_raise

    @can_raise.setter
    def can_raise_setter(self, new_status: bool):
        self._can_raise = new_status



    @dbus_property_async('b',  flags=DbusPropertyEmitsChangeFlag)
    def can_set_fullscreen(self) -> bool:
        return self._can_set_fulscreen

    @can_set_fullscreen.setter
    def can_set_fullscreen_setter(self, new_status: bool):
        self._can_set_fulscreen = new_status



    @dbus_property_async('b',  flags=DbusPropertyEmitsChangeFlag)
    def has_track_list(self) -> bool :
        return self._has_track_list

    @has_track_list.setter
    def has_track_list_setter(self, new_status: bool):
         self._has_track_list = new_status



    @dbus_property_async('s',  flags=DbusPropertyEmitsChangeFlag)
    def identity(self) -> str:
        return self._identity

    @identity.setter
    def identity_setter(self, new_status: str):
        self._identity = new_status



    @dbus_property_async('s',  flags=DbusPropertyEmitsChangeFlag)
    def desktop_entry(self) -> str:
        return self._desktop_entry

    @desktop_entry.setter
    def desktop_entry_setter(self, new_status: str):
        self._desktop_entry = new_status



    @dbus_property_async('as',  flags=DbusPropertyEmitsChangeFlag)
    def supported_uri_schemes(self) -> list[str]:
        return self._supported_uri_schemes

    @supported_uri_schemes.setter
    def supported_uri_schemes_setter(self, new_status: list[str]):
        self._supported_uri_schemes = new_status



    @dbus_property_async('as',  flags=DbusPropertyEmitsChangeFlag)
    def supported_mime_types(self) -> list[str]:
        return self._supported_mime_types

    @supported_mime_types.setter
    def supported_mime_types_setter(self, new_status: list[str]):
         self._supported_mime_types = new_status



    @dbus_method_async('')
    async def quit(self) -> None:
        self.action_queue.append("QUIT")
