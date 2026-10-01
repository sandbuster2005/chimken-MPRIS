import asyncio
import threading
from sdbus import request_default_bus_name_async
from Player import  MediaPlayer2Player
from Root import MediaPlayer2Root



class MPRIS_server:

    def __init__(self):
        self.action_queue = []   # D-Bus -> TUI (e.g., media keys pressed)
        self.update_queue = []  # TUI -> D-Bus (e.g., user clicked pause inside TUI)

        self.root_interface = MediaPlayer2Root( self.action_queue )
        self.player_interface = MediaPlayer2Player( self.action_queue )

    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        async def main():
            # Register a well-known D-Bus name under the standard MPRIS convention
            # (e.g., org.mpris.MediaPlayer2.my_player)
            await request_default_bus_name_async("org.mpris.MediaPlayer2.ChimkenMuziks")

            # Export both interfaces to the standard MPRIS object path
            object_path = "/org/mpris/MediaPlayer2"

            self.root_interface.export_to_dbus( object_path )
            self.player_interface.export_to_dbus( object_path )

        loop.run_until_complete( main() )
        # This keeps the D-Bus listener running indefinitely in the background thread
        loop.run_forever()

MPRIS = MPRIS_server()
dbus_thread = threading.Thread(target=MPRIS.run, daemon=True).start()
#
while 1:
    if MPRIS.action_queue:
        print(f"Received action from MPRIS: {MPRIS.action_queue}")
