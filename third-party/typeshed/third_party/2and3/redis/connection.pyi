from typing import Any, Text, Optional

ssl_available: Any
hiredis_version: Any
HIREDIS_SUPPORTS_CALLABLE_ERRORS: Any
HIREDIS_SUPPORTS_BYTE_BUFFER: Any
msg: Any
HIREDIS_USE_BYTE_BUFFER: Any
SYM_STAR: Any
SYM_DOLLAR: Any
SYM_CRLF: Any
SYM_EMPTY: Any
SERVER_CLOSED_CONNECTION_ERROR: Any

class Token:
    value: Any
    def __init__(self, value) -> None: ...

class BaseParser:
    EXCEPTION_CLASSES: Any
    def parse_error(self, response): ...

class SocketBuffer:
    socket_read_size: Any
    bytes_written: Any
    bytes_read: Any
    def __init__(self, socket, socket_read_size) -> None: ...
    @property
    def length(self): ...
    def read(self, length): ...
    def readline(self): ...
    def purge(self): ...
    def close(self): ...

class PythonParser(BaseParser):
    encoding: Any
    socket_read_size: Any
    def __init__(self, socket_read_size) -> None: ...
    def __del__(self): ...
    def on_connect(self, connection): ...
    def on_disconnect(self): ...
    def can_read(self): ...
    def read_response(self): ...

class HiredisParser(BaseParser):
    socket_read_size: Any
    def __init__(self, socket_read_size) -> None: ...
    def __del__(self): ...
    def on_connect(self, connection): ...
    def on_disconnect(self): ...
    def can_read(self): ...
    def read_response(self): ...

DefaultParser: Any

class Connection:
    description_format: Any
    pid: Any
    host: Any
    port: Any
    db: Any
    password: Any
    socket_timeout: Any
    socket_connect_timeout: Any
    socket_keepalive: Any
    socket_keepalive_options: Any
    retry_on_timeout: Any
    encoding: Any
    encoding_errors: Any
    decode_responses: Any
    def __init__(
        self,
        host=...,
        port=...,
        db=...,
        password=...,
        socket_timeout=...,
        socket_connect_timeout=...,
        socket_keepalive=...,
        socket_keepalive_options=...,
        retry_on_timeout=...,
        encoding=...,
        encoding_errors=...,
        decode_responses=...,
        parser_class=...,
        socket_read_size=...,
    ) -> None: ...
    def __del__(self): ...
    def register_connect_callback(self, callback): ...
    def clear_connect_callbacks(self): ...
    def connect(self): ...
    def on_connect(self): ...
    def disconnect(self): ...
    def send_packed_command(self, command): ...
    def send_command(self, *args): ...
    def can_read(self): ...
    def read_response(self): ...
    def encode(self, value): ...
    def pack_command(self, *args): ...
    def pack_commands(self, commands): ...

class SSLConnection(Connection):
    description_format: Any
    keyfile: Any
    certfile: Any
    cert_reqs: Any
    ca_certs: Any
    def __init__(
        self,
        ssl_keyfile=...,
        ssl_certfile=...,
        ssl_cert_reqs=...,
        ssl_ca_certs=...,
        **kwargs,
    ) -> None: ...

class UnixDomainSocketConnection(Connection):
    description_format: Any
    pid: Any
    path: Any
    db: Any
    password: Any
    socket_timeout: Any
    retry_on_timeout: Any
    encoding: Any
    encoding_errors: Any
    decode_responses: Any
    def __init__(
        self,
        path=...,
        db=...,
        password=...,
        socket_timeout=...,
        encoding=...,
        encoding_errors=...,
        decode_responses=...,
        retry_on_timeout=...,
        parser_class=...,
        socket_read_size=...,
    ) -> None: ...

class ConnectionPool:
    @classmethod
    def from_url(
        cls, url: Text, db: Optional[int] = ..., **kwargs
    ) -> ConnectionPool: ...
    connection_class: Any
    connection_kwargs: Any
    max_connections: Any
    def __init__(
        self, connection_class=..., max_connections=..., **connection_kwargs
    ) -> None: ...
    pid: Any
    def reset(self): ...
    def get_connection(self, command_name, *keys, **options): ...
    def make_connection(self): ...
    def release(self, connection): ...
    def disconnect(self): ...

class BlockingConnectionPool(ConnectionPool):
    queue_class: Any
    timeout: Any
    def __init__(
        self,
        max_connections=...,
        timeout=...,
        connection_class=...,
        queue_class=...,
        **connection_kwargs,
    ) -> None: ...
    pid: Any
    pool: Any
    def reset(self): ...
    def make_connection(self): ...
    def get_connection(self, command_name, *keys, **options): ...
    def release(self, connection): ...
    def disconnect(self): ...