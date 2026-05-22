import asyncio

from bots.radisson import start_bot as start_radisson
from bots.sharkteambreaks import start_bot as start_sharkteambreaks
from bots.cometeambreaks import start_bot as start_cometeambreaks
from bots.lariusno import start_bot as start_lariusno
from bots.delta import start_bot as start_delta
from bots.Energy import start_bot as start_energy


async def delayed_start(delay, starter):
    await asyncio.sleep(delay)
    await starter()


async def main():
    await asyncio.gather(
        delayed_start(5, start_radisson),
        delayed_start(10, start_sharkteambreaks),
        delayed_start(15, start_cometeambreaks),
        delayed_start(20, start_lariusno),
        delayed_start(25, start_delta),
        delayed_start(30, start_energy),
    )


if __name__ == "__main__":
    asyncio.run(main())
