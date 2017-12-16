from django.db import models

from .helpers import get_models_path_for_app, intermediate_model_name
from .settings import GET_MODEL_LOCATION_FUNCTION

__all__ = ['intermediate_m2m_model_class_factory']


def intermediate_m2m_model_class_factory(name_prefix, parent_model, **fields):
    """

    :param name_prefix:
    :param parent_model:
    :param fields:
    :return:
    """
    # pylint:disable=protected-access
    def get_model_location(cls):
        return '{app_label}.{model_name}'.format(
            app_label=cls._meta.app_label,
            model_name=cls.__name__,
        )

    return type(
        intermediate_model_name(name_prefix, parent_model),
        (models.Model, ),
        {
            '__module__': get_models_path_for_app(parent_model),
            'parent': models.ForeignKey(parent_model),
            GET_MODEL_LOCATION_FUNCTION: classmethod(get_model_location),
            **fields,
        },
    )
