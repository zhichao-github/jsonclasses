from __future__ import annotations
from jsonclasses import jsonclass, types


@jsonclass
class NumericAnalysis:
    product_name: str
    product_id: str = types.str.numeric.required

