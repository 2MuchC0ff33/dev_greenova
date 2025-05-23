# Copyright 2025 Enveng Group.
# SPDX-License-Identifier: AGPL-3.0-or-later

"""
Protocol buffer utilities for the chatbot app.

This module provides serialization and deserialization functions for
converting between Django models and Protocol Buffer messages in the
chatbot application.
"""

import logging
import os
import time
from typing import Any

from django.contrib.auth import get_user_model
from django.utils import timezone

# Import datetime explicitly to fix the module attribute error

User = get_user_model()
logger = logging.getLogger(__name__)


# Create minimal stubs for the protocol buffer classes
class DummyMessage:
    """Stub class used when protocol buffers are not available."""

    def SerializeToString(self) -> bytes:
        return b""

    def ParseFromString(self, data: bytes) -> None:
        pass


# Import generated protobuf modules with improved error handling
try:
    # Use relative import to ensure consistent module path
    from .proto import chatbot_pb2

    logger.info("Successfully imported chatbot_pb2 from proto package")
except ImportError:
    logger.error("Failed to import chatbot_pb2. Protocol buffer definition missing.")

    # Check if the proto file exists
    current_dir = os.path.dirname(os.path.abspath(__file__))
    proto_file = os.path.join(current_dir, "proto", "chatbot.proto")

    if os.path.exists(proto_file):
        logger.info(
            "chatbot.proto exists but chatbot_pb2.py not found. "
            "Run 'python manage.py compile_protos --app=chatbot' to generate it."
        )
    else:
        logger.error("chatbot.proto file not found in the proto directory.")

    # Create a minimal stub for the module to allow Django to continue loading
    chatbot_pb2 = type("chatbot_pb2", (), {})

    # Define minimal classes needed for type hinting
    class ChatMessage(DummyMessage):
        class MessageType:
            MESSAGE_TYPE_TEXT_UNSPECIFIED = 0
            MESSAGE_TYPE_IMAGE = 1
            MESSAGE_TYPE_AUDIO = 2

        def __init__(self):
            self.user_id = ""
            self.content = ""
            self.timestamp = 0
            self.type = self.MessageType.MESSAGE_TYPE_TEXT_UNSPECIFIED

    class ChatResponse(DummyMessage):
        def __init__(self):
            self.message_id = ""
            self.content = ""
            self.timestamp = 0

    chatbot_pb2.ChatMessage = ChatMessage
    chatbot_pb2.ChatResponse = ChatResponse


def serialize_chat_message(chat_message) -> bytes | None:
    """
    Serialize a ChatMessage instance to a Protocol Buffer message.

    Args:
        chat_message: The ChatMessage instance to serialize

    Returns:
        Serialized protocol buffer data as bytes, or None if serialization failed
    """
    try:
        # Create a new ChatMessage message
        proto = chatbot_pb2.ChatMessage()

        # Set basic fields
        if hasattr(chat_message, "user") and chat_message.user:
            proto.user_id = str(chat_message.user.id)

        proto.content = chat_message.content
        proto.timestamp = int(chat_message.timestamp.timestamp())
        proto.type = chatbot_pb2.ChatMessage.MessageType.MESSAGE_TYPE_TEXT_UNSPECIFIED

        # Serialize to bytes
        return proto.SerializeToString()
    except (AttributeError, TypeError) as e:
        logger.error("Error during chat message serialization: %s", str(e))
        return None
    except ValueError as e:
        logger.error("Value error during chat message serialization: %s", str(e))
        return None


def build_chat_message_proto(
    user_id: str | None, content: str, timestamp: int | None, message_type: int
) -> "chatbot_pb2.ChatMessage":
    """
    Build a ChatMessage protobuf object with proper initialization.

    Args:
        user_id: User ID string or None
        content: Message content string
        timestamp: Message timestamp as Unix timestamp or None
        message_type: Message type enum value

    Returns:
        Initialized ChatMessage protobuf object
    """
    proto = chatbot_pb2.ChatMessage()

    if user_id is not None:
        proto.user_id = user_id

    proto.content = content

    if timestamp is not None:
        proto.timestamp = timestamp

    proto.type = message_type

    return proto


def deserialize_chat_message(data: bytes) -> dict[str, Any] | None:
    """
    Deserialize Protocol Buffer data to a dictionary that can be used to create
    a ChatMessage.

    Args:
        data: Serialized protocol buffer data

    Returns:
        A dictionary with ChatMessage fields, or None if deserialization failed
    """
    try:
        # Parse the binary data into a ChatMessage
        proto = chatbot_pb2.ChatMessage()
        proto.ParseFromString(data)

        # Convert to a dictionary
        message_dict = {
            "content": proto.content,
        }

        # Add user if present
        if proto.user_id:
            try:
                message_dict["user"] = User.objects.get(id=proto.user_id)
            except User.DoesNotExist:
                logger.warning("User with ID %s not found", proto.user_id)

        # Add timestamp if present
        if proto.timestamp:
            message_dict["timestamp"] = timezone.datetime.fromtimestamp(
                proto.timestamp, tz=timezone.get_current_timezone()
            )

        return message_dict
    except (AttributeError, TypeError) as e:
        logger.error("Error during message deserialization: %s", str(e))
        return None
    except ValueError as e:
        logger.error("Value error during message deserialization: %s", str(e))
        return None


def create_chat_response(message_id: str, content: str) -> bytes | None:
    """
    Create a serialized ChatResponse protocol buffer message.

    Args:
        message_id: The ID of the message being responded to
        content: The content of the response

    Returns:
        Serialized protocol buffer data as bytes, or None if creation failed
    """
    try:
        # Create a new ChatResponse message
        proto = chatbot_pb2.ChatResponse()

        # Set fields
        proto.message_id = str(message_id)
        proto.content = content

        # Set timestamp
        proto.timestamp = int(time.time())

        # Serialize to bytes
        return proto.SerializeToString()
    except (AttributeError, TypeError) as e:
        logger.error("Error during chat response creation: %s", str(e))
        return None
    except ValueError as e:
        logger.error("Value error during chat response creation: %s", str(e))
        return None


def parse_chat_response(data: bytes) -> dict[str, Any] | None:
    """
    Parse a serialized ChatResponse protocol buffer message.

    Args:
        data: Serialized protocol buffer data

    Returns:
        A dictionary with the response data, or None if parsing failed
    """
    try:
        # Parse the binary data into a ChatResponse
        proto = chatbot_pb2.ChatResponse()
        proto.ParseFromString(data)

        # Convert to a dictionary
        response_dict = {
            "message_id": proto.message_id,
            "content": proto.content,
        }

        # Add timestamp if present
        if proto.timestamp:
            response_dict["timestamp"] = timezone.datetime.fromtimestamp(
                proto.timestamp, tz=timezone.get_current_timezone()
            )

        return response_dict
    except (AttributeError, TypeError) as e:
        logger.error("Error during chat response parsing: %s", str(e))
        return None
    except ValueError as e:
        logger.error("Value error during chat response parsing: %s", str(e))
        return None
