"""module for checkpw modifier."""
from __future__ import annotations
from typing import Any, TYPE_CHECKING
from .modifier import Modifier
if TYPE_CHECKING:
    from ..ctx import Ctx
    from ..types import Types

class CheckpwModifier(Modifier):
    """Checkpw modifier checks string value with bcrypt's checkpw function."""

    def __init__(self, against: Types) -> None:
        try:
            from bcrypt import checkpw
        except ModuleNotFoundError as e:
            raise ModuleNotFoundError('please install bcrypt to use checkpw')
        self.against = against

    def validate(self, ctx: Ctx) -> None:
        from bcrypt import checkpw
        against_val = self.against.modifier.transform(ctx)
        if type(against_val) is not str:
            ctx.raise_vexc('value is incorrect')
        if type(ctx.val) is not str:
            ctx.raise_vexc('value is incorrect')
        if not checkpw(against_val.encode(), ctx.val.encode()):
            ctx.raise_vexc('value is incorrect')
