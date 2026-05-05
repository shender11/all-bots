import asyncio

from bots.breakfamily import start_bot as start_breakfamily
from bots.radisson import start_bot as start_radisson
from bots.sharkteambreaks import start_bot as start_sharkteambreaks
from bots.cometeambreaks import start_bot as start_cometeambreaks
from bots.lariusno import start_bot as start_lariusno
from bots.delta import start_bot as start_delta


async def main():
    await asyncio.gather(
        start_breakfamily(),
        start_radisson(),
        start_sharkteambreaks(),
        start_cometeambreaks(),
        start_lariusno(),
        start_delta(),
    )


if __name__ == "__main__":
    asyncio.run(main())
