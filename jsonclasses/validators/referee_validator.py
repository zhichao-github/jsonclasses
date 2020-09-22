"""module for referee validator."""
from ..fields import FieldDescription
from .validator import Validator
from ..contexts import ValidatingContext


class RefereeValidator(Validator):
    """Readwrite validator marks a reference field with a referee name."""

    def __init__(self, referee_key: str) -> None:
        self.referee_key = referee_key

    def define(self, field_description: FieldDescription) -> None:
        field_description.join_table_referee_key = self.referee_key

    def validate(self, context: ValidatingContext) -> None:
        pass
