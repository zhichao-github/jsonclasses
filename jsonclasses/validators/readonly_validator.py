"""module for readonly validator."""
from ..fields import FieldDescription, WriteRule
from .validator import Validator
from ..contexts import ValidatingContext


class ReadonlyValidator(Validator):
    """Readonly validator marks a field to be readonly."""

    def define(self, field_description: FieldDescription) -> None:
        field_description.write_rule = WriteRule.NO_WRITE

    def validate(self, context: ValidatingContext) -> None:
        pass
