"""module for linkto validator."""
from ..fields import FieldDescription, FieldStorage
from .validator import Validator
from ..contexts import ValidatingContext


class LinkToValidator(Validator):
    """Link to validator marks a field which is a local key."""

    def define(self, field_description: FieldDescription) -> None:
        field_description.field_storage = FieldStorage.LOCAL_KEY

    def validate(self, context: ValidatingContext) -> None:
        pass
