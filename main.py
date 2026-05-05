import asyncio

from bots.breakfamily import start_bot as start_breakfamily
from bots.radisson import start_bot as start_radisson
from bots.sharkteambreaks import start_bot as start_sharkteambreaks
from bots.cometeambreaks import start_bot as start_cometeambreaks
from bots.lariusno import start_bot as start_lariusno
from bots.delta import start_bot as start_delta


async def delayed_start(delay, starter):
    await asyncio.sleep(delay)
    await starter()


async def main():
    await asyncio.gather(
        delayed_start(0, start_breakfamily),
        delayed_start(5, start_radisson),
        delayed_start(10, start_sharkteambreaks),
        delayed_start(15, start_cometeambreaks),
        delayed_start(20, start_lariusno),
        delayed_start(25, start_delta),
    )


if __name__ == "__main__":
    asyncio.run(main())
