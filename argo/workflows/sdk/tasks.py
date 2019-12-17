from functools import partial
from functools import wraps

from typing import Any
from typing import Dict
from typing import Callable
from typing import List
from typing import Optional
from typing import Tuple
from typing import Type
from typing import Union

from argo.workflows.client.models import (
    V1alpha1Arguments,
    V1alpha1Artifact,
    V1alpha1ContinueOn,
    V1alpha1DAGTask,
    V1alpha1Parameter,
    V1alpha1Sequence,
    V1alpha1Template,
    V1alpha1TemplateRef,
)

from ._base import Prop
from ._base import Spec
from ._arguments import artifact, parameter


__all__ = [
    # decorators
    "artifact",
    "continue_on",
    "dependencies",
    "parameter",
    "task",
    "when",
    "with_items",
    "with_param",
    "with_sequence",
    # models
    "V1alpha1Template",
    "V1alpha1TemplateRef",
]

# return type
T = Union[V1alpha1Template, V1alpha1TemplateRef]


class task(Spec):

    __model__ = V1alpha1DAGTask

    def __new__(cls, f: Callable[..., T]):
        """Workflow spec for V1alpha1Template."""
        self = super().__new__(cls, f)
        self.name = f.__code__.co_name

        return self

    def __compilehook__(self, spec: T, *args, **kwargs):
        if isinstance(spec, V1alpha1Template):
            self.template: str = spec.name
        elif isinstance(spec, V1alpha1TemplateRef):
            self.template_ref: V1alpha1TemplateRef = spec
        else:
            raise TypeError(f"Expected {T}, got: {type(spec)}")


class dependencies(Prop):

    __model__ = List[str]


class continue_on(Prop):

    __model__ = V1alpha1ContinueOn


class when(Prop):

    __model__ = str


class with_items(Prop):

    __model__ = List[str]


class with_param(Prop):

    __model__ = str


class with_sequence(Prop):

    __model__ = V1alpha1Sequence