import asyncio
import threading
from sdbus import request_default_bus_name_async
from .Player import  MediaPlayer2Player
from .Root import MediaPlayer2Root

class MPRIS_server:


    def __init__(self):
        self.action_queue = []   # D-Bus -> TUI (e.g., media keys pressed)
        self.update_queue = []  # TUI -> D-Bus (e.g., user clicked pause inside TUI)

        self.root = MediaPlayer2Root( self.action_queue ) # interface
        self.player = MediaPlayer2Player( self.action_queue )# interface


        self._properties = {

            **{name : 'player' for name in
                [
                    "playback_status", "loop_status",
                    "rate", "shuffle",
                    "metadata", "volume",
                    "position", "minimum_rate",
                    "maximum_rate", "can_go_next",
                    "can_go_previous", "can_play",
                    "can_pause", "can_seek",
                    "can_control"
                ]
            },

            **{name : "root" for name in
                [
                    "can_quit", "fullscreen",
                    "can_set_fullscreen", "can_raise",
                    "has_track_list", "identity",
                    "desktop_entry", "supported_uri_schemes",
                    "supported_mime_types",
                ]
            }
        }



    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        async def main():
            # Register a well-known D-Bus name under the standard MPRIS convention
            # (e.g., org.mpris.MediaPlayer2.my_player)
            await request_default_bus_name_async("org.mpris.MediaPlayer2.ChimkenMuziks")

            # Export both interfaces to the standard MPRIS object path
            object_path = "/org/mpris/MediaPlayer2"

            self.root.export_to_dbus( object_path )
            self.player.export_to_dbus( object_path )

            async def sync_tui_states():
                while True:
                    if self.update_queue:
                        prop_name, new_value = self.update_queue.pop()

                        if prop_name in self._properties:
                             propertie = getattr(self.player, prop_name)
                             await propertie.set_async( new_value )

                    await asyncio.sleep(0.05)

            loop.create_task(sync_tui_states())


        loop.run_until_complete( main() )
        # This keeps the D-Bus listener running indefinitely in the background thread
        loop.run_forever()
