from collections.abc import Sequence

class Message:
    content: str
    is_bot: bool
    timestamp: str

    def __init__(
        self, *, content: str = ..., is_bot: bool = ..., timestamp: str = ...
    ) -> None: ...
    def CopyFrom(self, other_msg: Message) -> None: ...

class Conversation:
    title: str
    user_id: str
    created_at: str
    updated_at: str
    messages: list[Message]

    def __init__(
        self,
        *,
        title: str = ...,
        user_id: str = ...,
        created_at: str = ...,
        updated_at: str = ...,
        messages: Sequence[Message] | None = ...,
    ) -> None: ...
    def CopyFrom(self, other_msg: Conversation) -> None: ...
    def add_messages(self) -> Message: ...

class ConversationCollection:
    conversations: list[Conversation]

    def __init__(
        self, *, conversations: Sequence[Conversation] | None = ...
    ) -> None: ...
    def CopyFrom(self, other_msg: ConversationCollection) -> None: ...
    def add_conversations(self) -> Conversation: ...
