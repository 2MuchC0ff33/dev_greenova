from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class ChatMessage(_message.Message):
    __slots__ = ["content", "timestamp", "type", "user_id"]
    class MessageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []

    CONTENT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPE_AUDIO: ChatMessage.MessageType
    MESSAGE_TYPE_IMAGE: ChatMessage.MessageType
    MESSAGE_TYPE_TEXT_UNSPECIFIED: ChatMessage.MessageType
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    content: str
    timestamp: int
    type: ChatMessage.MessageType
    user_id: str
    def __init__(
        self,
        user_id: str | None = ...,
        content: str | None = ...,
        timestamp: int | None = ...,
        type: ChatMessage.MessageType | str | None = ...,
    ) -> None: ...

class ChatResponse(_message.Message):
    __slots__ = ["content", "message_id", "timestamp"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    content: str
    message_id: str
    timestamp: int
    def __init__(
        self,
        message_id: str | None = ...,
        content: str | None = ...,
        timestamp: int | None = ...,
    ) -> None: ...
