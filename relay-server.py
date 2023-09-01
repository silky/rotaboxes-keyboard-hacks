#!/usr/bin/env python

from pynput import keyboard
import asyncio
import hid
import string
import sys
import websockets

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Communicate-to-keyboard stuff
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def get_raw_hid_interface():
    # Trivia specific to the QMK setup and device.
    # See: <https://github.com/qmk/qmk_firmware/blob/master/docs/feature_rawhid.md>,
    # from which this code is taken directly.
    vendor_id     = 65261
    product_id    = 0
    usage_page    = 0xFF60
    usage         = 0x61

    device_interfaces = hid.enumerate(vendor_id, product_id)
    raw_hid_interfaces = [i for i in device_interfaces if i['usage_page'] == usage_page and i['usage'] == usage]

    if len(raw_hid_interfaces) == 0:
        return None

    interface = hid.Device(path=raw_hid_interfaces[0]['path'])
    return interface

def send_raw_report(data):
    report_length = 32
    interface = get_raw_hid_interface()

    if interface is None:
        print("No device found")
        sys.exit(1)

    request_data = [0x00] * (report_length + 1) # First byte is Report ID
    request_data[1:len(data) + 1] = data
    request_report = bytes(request_data)

    print(request_report)

    try:
        interface.write(request_report)
    finally:
        interface.close()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Read key event stuff
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def on_press(websocket, key):
    x = websocket.send(key)

def on_release(key):
    if key == keyboard.Key.esc:
        return False

def transmit_keys():
    queue = asyncio.Queue()
    loop  = asyncio.get_event_loop()
    def on_press(key):
        loop.call_soon_threadsafe(queue.put_nowait, key)
    keyboard.Listener(on_press=on_press).start()
    return queue


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Websocket-y stuff
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

keyToNumberMap = { k: n for (k,n) in zip(string.ascii_lowercase, range(25)) }


async def go(websocket):
    key_queue = transmit_keys()

    asyncio.create_task(receive_message(websocket))

    while True:
        try:
            key = await key_queue.get()
            n   = keyToNumberMap[key.char]
            await websocket.send(f"{n}")
        except:
            pass


async def receive_message(websocket):
    while True:
        response = await websocket.recv()
        (bit, n) = response.split(",")
        # 0x41 = 'A'; they key-code we sent from QMK.
        send_raw_report([int(bit), 0x41 + int(n)])



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Entrypoint
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

async def main():
    async with websockets.serve(go, "localhost", 8002):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
