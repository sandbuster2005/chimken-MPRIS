from sdbus import (
    DbusInterfaceCommonAsync,
    dbus_method_async,
    dbus_property_async,
    DbusPropertyEmitsChangeFlag
)

class MediaPlayer2Player(DbusInterfaceCommonAsync, interface_name='org.mpris.MediaPlayer2.Player'):

    def __init__(self, action_queue):

        super().__init__()
        self.action_queue = action_queue



        self._playback_status = "Playing"
        self._loop_status = "Stopped"
        self._rate = 1.0
        self._shuffle = False
        self._metadata = {}
        self._volume = 1.0
        self._position = 0
        self._minimum_rate = 1.0
        self._maximum_rate = 1.0
        self._can_go_next = True
        self._can_go_previous = True
        self._can_play = True
        self._can_pause = True
        self._can_seek = True
        self._can_control = True

    @dbus_property_async('s', flags=DbusPropertyEmitsChangeFlag )
    def playback_status(self) -> str :
        # In a real app, query your state variables here
        return self._playback_status

    @playback_status.setter
    def playback_status_setter(self, new_status: str):
        self._playback_status = new_status



    @dbus_property_async('s', flags=DbusPropertyEmitsChangeFlag )
    def loop_status(self) -> str:
        return self._loop_status

    @loop_status.setter
    def loop_status_setter(self, new_status: str):
        self._loop_status = new_status



    @dbus_property_async('d', flags=DbusPropertyEmitsChangeFlag )
    def rate(self) -> float :
        return self._rate

    @rate.setter
    def rate_setter(self, new_status: float):
        self._rate = new_status



    @dbus_property_async('b', flags=DbusPropertyEmitsChangeFlag )
    def shuffle(self) -> bool:
        return self._shuffle

    @shuffle.setter
    def shuffle_setter(self , new_status: bool):
        self._shuffle = new_status



    @dbus_property_async('a{sv}', flags=DbusPropertyEmitsChangeFlag )
    def metadata(self) -> dict :
        return self._metadata

    @metadata.setter
    def metadata_setter(self , new_status: dict):
        self._metadata = new_status



    @dbus_property_async('d', flags=DbusPropertyEmitsChangeFlag )
    def volume(self) -> float:
        return self._volume

    @volume.setter
    def volume_setter(self , new_status: float):
        self._volume = new_status



    @dbus_property_async('x')
    def position(self) -> int :
        return self._position

    @position.setter
    def position_setter(self , new_status: int):
        self._position = new_status



    @dbus_property_async('d', flags=DbusPropertyEmitsChangeFlag)
    def minimum_rate(self) -> float :
        return self._minimum_rate

    @minimum_rate.setter
    def minimum_rate_setter(self , new_status: float):
        self._minimum_rate = new_status



    @dbus_property_async('d', flags=DbusPropertyEmitsChangeFlag)
    def maximum_rate(self) -> float:
        return self._maximum_rate

    @maximum_rate.setter
    def maximum_rate_setter(self , new_status: float):
        self._maximum_rate = new_status



    @dbus_property_async('b', flags=DbusPropertyEmitsChangeFlag)
    def can_go_next(self) -> bool:
        return self._can_go_next

    @can_go_next.setter
    def can_go_next_setter(self , new_status: bool):
        self._can_go_next = new_status



    @dbus_property_async('b', flags=DbusPropertyEmitsChangeFlag)
    def can_go_previous(self) -> bool:
        return self._can_go_previous

    @can_go_previous.setter
    def can_go_previous_setter(self , new_status: bool):
        self._can_go_previous = new_status



    @dbus_property_async('b', flags=DbusPropertyEmitsChangeFlag)
    def can_play(self) -> bool:
        return self._can_play

    @can_play.setter
    def can_play_setter(self , new_status: bool):
        self._can_play = new_status



    @dbus_property_async('b', flags=DbusPropertyEmitsChangeFlag)
    def can_pause(self) -> bool:
        return self._can_pause

    @can_pause.setter
    def can_pause_setter(self , new_status: bool):
        self._can_pause = new_status



    @dbus_property_async('b', flags=DbusPropertyEmitsChangeFlag)
    def can_seek(self) -> bool:
        return self._can_seek

    @can_seek.setter
    def can_seek_setter(self , new_status: bool):
        self._can_seek = new_status



    @dbus_property_async('b')
    def can_control(self) -> bool :
        return self._can_control

    @can_control.setter
    def can_control_setter(self , new_status: bool):
        self._can_control = new_status





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

    @dbus_method_async('x')
    async def seek(self,time_offset):
        self.action_queue.append(f"seek:{time_offset}")
