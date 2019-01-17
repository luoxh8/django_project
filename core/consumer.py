from asgiref.sync import async_to_sync

from h_utils.websocket_extra import WebsocketConsumerExtra

'''
{"id":"28","route":"heartbeat","req_data":""}
'''


class IMConsumer(WebsocketConsumerExtra):
    room_name = 'im'

    def receive(self, text_data=None, bytes_data=None):
        data = self.parse_data(text_data)
        if data['route'] == 'heartbeat':
            async_to_sync(self.channel_layer.group_send)(self.room_name, {
                'type': data['route'],
                'message': text_data,
            })
        else:
            async_to_sync(self.channel_layer.group_send)(self.room_name, {
                'type': 'no_route',
            })
