import asyncio


async def main():
    print("Hello")
    await asyncio.sleep(1)
    task1 = asyncio.create_task(calculate(1, 2))
    task2 = asyncio.create_task(calculate(3, 4))
    print("Tasks created")
    result1 = await task1
    result2 = await task2
    print(f"Result 1: {result1}")
    print(f"Result 2: {result2}")
    await asyncio.sleep(1)


async def calculate(a, b):
    print(f"Calculating {a} + {b}")
    return a + b


# asyncio.run(main())
if __name__ == "__main__":
    asyncio.run(main())
    print("ALL TASKS COMPLETED")
