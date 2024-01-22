from typing import Union, Optional, Dict, Any
from streamsync.core import Readable, FileWrapper, BytesWrapper, Config, Component
from streamsync.core import initial_state, component_manager, session_manager, session_verifier

VERSION = "0.2.8"

component_manager
session_manager
Config
session_verifier

def pack_file(file: Union[Readable, str], mime_type: Optional[str] = None):
    """
    Returns a FileWrapper for the file provided, which is automatically
    serialised to a data URL.
    """

    return FileWrapper(file, mime_type)


def pack_bytes(raw_data, mime_type: Optional[str] = None):
    """
    Returns a BytesWrapper for the bytes raw data provided, which is automatically
    serialised to a data URL.
    """

    return BytesWrapper(raw_data, mime_type)


def init_state(state_dict: Dict[str, Any]):
    """
    Sets the initial state, which will be used as the starting point for
    every session.
    """

    initial_state.user_state.state = {}
    initial_state.user_state.ingest(state_dict)
    return initial_state

def attach(parent_id: str, child: Component):
    parent = component_manager.components.get(parent_id)
    if not parent:
        raise ValueError(f'Could not find component with id "{parent_id}"')
    parent.attach(child)


class Section(Component):

    def __init__(self, content={}):
        super().__init__(None, "section", content)


class Page(Component):

    def __init__(self, content={}):
        super().__init__(None, "page", content)


class Heading(Component):

    def __init__(self, content={}):
        super().__init__(None, "heading", content)
