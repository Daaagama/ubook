class WebApplicationBaseException(Exception):
    ...


class ChannelNotFoundException(WebApplicationBaseException):
    ...


class VideoNotFoundException(WebApplicationBaseException):
    ...


class ManufacturerNotFoundException(WebApplicationBaseException):
    ...


class RadioPartNotFoundException(WebApplicationBaseException):
    ...
