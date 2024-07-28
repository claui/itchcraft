"""Custom error types."""

class CliError(Exception):
    """An user-facing error message."""

class BackendInitializationError(Exception):
    """An error that occurs during backend initialization."""

class EndpointNotFound(Exception):
    """An error that is raised if a hardware endpoint is not found."""
