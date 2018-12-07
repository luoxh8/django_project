import json
from json import JSONDecodeError

from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer

from h_utils.scheduler_extra import scheduler


class WebsocketConsumerExtra(WebsocketConsumer):
    room_name = 'hall'
    text_data_json = {}
    bytes_data_json = {}
    heartbeat_time_out = 10

    def connect(self):
        scheduler.add_job(self.close, self.heartbeat_time_out, self.channel_name)
        async_to_sync(self.channel_layer.group_add)(
            self.room_name,
            self.channel_name
        )
        self.accept()

    def no_route(self, event):
        self.send(text_data='找不到该路由')
        self.close()

    def heartbeat(self, event):
        message = event['message']
        scheduler.re_add_job(self.close, self.heartbeat_time_out, self.channel_name)
        self.send(text_data=message)

    def parse_data(self, data):
        try:
            self.text_data_json = dict(json.loads(data))
        except JSONDecodeError:
            return {'route': 'no_route'}
        except ValueError:
            return {'route': 'no_route'}
        return self.text_data_json

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_name,
            self.channel_name
        )
        scheduler.remove_job(self.channel_name)


class AsyncWebsocketConsumerExtra(AsyncWebsocketConsumer):
    room_name = 'hall'
    text_data_json = {}
    bytes_data_json = {}

    async def connect(self):
        scheduler.add_job(self.close, 5, self.channel_name)
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )
        await self.accept()

    async def no_route(self, event):
        await self.send(text_data='找不到该路由')
        await self.close()

    async def heartbeat(self, event):
        message = event['message']
        scheduler.re_add_job(self.close, 5, self.channel_name)
        await self.send(text_data=message)

    def parse_data(self, data):
        try:
            self.text_data_json = dict(json.loads(data))
        except JSONDecodeError:
            return {'route': 'no_route'}
        return self.text_data_json

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )
        scheduler.remove_job(self.channel_name)
