import asyncio
from telethon import TelegramClient, events

async def main():
    event = asyncio.Event()
    bot_token = '5832858184:AAE-DaLW7nh9m1LYZJA0yOrlAXJXkX248fg'
    client = TelegramClient('ghhj'+bot_token, "17484848", "4d6acdeff347f8103a71c18b11e751bc")
    await client.start(bot_token=bot_token)
    bot_chat_id = 5832858184

    @client.on(events.NewMessage(chats=bot_chat_id))
    async def my_event_handler(event):
        print(event)
        if event.message.from_id.user_id == 5832858184:
               if '#AD' in event.message.message or '#PaidAD' in event.message.message or 'bots.business/ads' in event.message.message '#paidAD' in event.message.message or 'sponsored' in event.message.message:
                print(event)
                await client.delete_messages(event.message.peer_id.user_id, event.message.id)
                print('message deleted successfully')
               else:
                    print('failed')
                    pass
    client.add_event_handler(my_event_handler)
    while True:
        await event.wait()
        event.clear()

if __name__ == '__main__':
    asyncio.run(main())
