from hello import create_app
import asyncio

app = create_app()

async def main():
    if __name__ == '__main__':
        app.run(debug=True)

asyncio.run(main())

