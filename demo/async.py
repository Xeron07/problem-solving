import asyncio

async def callAfter(time):
    for i in range(0,time):
        await asyncio.sleep(0.5)
        print("called after:",i)

async def runLoop(t):
    while(t<=100):
        await asyncio.sleep(0.25)
        t += 1
        print(t)

async def main():
    asyncio.create_task(runLoop(0))
    await asyncio.create_task(callAfter(5))
    asyncio.create_task(callAfter(2))


asyncio.run(main())




