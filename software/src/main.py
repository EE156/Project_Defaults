# example async function
import board
from rainbowio import colorwheel
import neopixel
import asyncio

neopixel = neopixel.NeoPixel(board.A1, 1, brightness=0.3, auto_write=False)

async def rainbow_cycle(neopixel, wait):
    for i in range(255):
        neopixel[0] = colorwheel(i)
        neopixel.show()
        await asyncio.sleep(wait)

async def coroutine():
    while True:
        await rainbow_cycle(neopixel)

# Your coroutine will run "at the same time" as coroutines performing other
# tasks for the Uber Radio.
asyncio.run(coroutine)