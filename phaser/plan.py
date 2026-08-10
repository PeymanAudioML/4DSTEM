import typing as t

from .types import Dataclass

class ReconsPlan(Dataclass, kw_only=True):

    name: str
    dtype: t.Literal['float32', 'float64'] = 'float32'
    wavelength: t.Optional[float] = None
#    raw_data: RawDataHook