from threading import Condition
from typing import BinaryIO, Collection, Optional
from uuid import uuid4

from ehforwarderbot import MsgType, Status, coordinator
from ehforwarderbot.channel import SlaveChannel
from ehforwarderbot.chat import Chat, PrivateChat
from ehforwarderbot.exceptions import EFBChannelNotFound, EFBOperationNotSupported
from ehforwarderbot.message import Message
from ehforwarderbot.types import MessageID, ModuleID, InstanceID, ChatID

from .__version__ import __version__


class CaiYunWeatherSlave(SlaveChannel):
    channel_name: str = 'Echo channel'
    channel_emoji: str = '🔁'
    channel_id: ModuleID = ModuleID('hawthorn.echo')
    __version__: str = __version__
    supported_message_types = {MsgType.Text}

    def __init__(self, instance_id: InstanceID = None):
        super().__init__(instance_id)
        # For test
        self.chat: PrivateChat = PrivateChat(channel=self, name='Echo Message', uid=ChatID('echo_chat'))
        self.condition: Optional[Condition] = None

    def send_message(self, msg: Message) -> Message:
        if msg.type == MsgType.Text:
            coordinator.send_message(Message(
                uid=MessageID(f'echo_{uuid4()}'),
                type=MsgType.Text,
                chat=self.chat,
                author=self.chat.other,
                deliver_to=coordinator.master,
                text=msg.text,
            ))
        return msg

    def send_status(self, status: Status):
        raise EFBOperationNotSupported()

    def get_chat(self, chat_uid: ChatID) -> Chat:
        if chat_uid == self.chat.uid:
            return self.chat
        raise EFBChannelNotFound()

    def get_chat_picture(self, chat: Chat) -> BinaryIO:
        raise EFBOperationNotSupported()

    def get_chats(self) -> Collection[Chat]:
        return [self.chat]

    def get_message_by_id(self, chat: Chat, msg_id: MessageID) -> Optional[Message]:
        return None

    def poll(self):
        pass

    def stop_polling(self):
        pass
