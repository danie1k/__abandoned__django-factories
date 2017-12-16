from importlib import import_module

from .helpers import get_models_path_for_app, dict_merge
from .other_class_factories import class_in_class_factory

__all__ = ['add_fields_to_model', 'register_model_in_app', 'set_class_in_class']


def add_fields_to_model(destination_model, **fields):
    """

    :param destination_model:
    :param fields:
    :return:
    """
    for field_name, field_field in fields.items():
        field_field.contribute_to_class(destination_model, field_name)


def register_model_in_app(app, model_class):
    """

    :param app:
    :param model_class:
    :return:
    """
    return __register_class_in_app_module(app, 'models', model_class)


def set_class_in_class(destination_class, class_to_insert_name, class_to_insert_dict):
    """

    :param destination_class:
    :param class_to_insert_name:
    :param class_to_insert_dict:
    :return:
    """
    if hasattr(destination_class, class_to_insert_name):
        dict_merge(class_to_insert_dict, dict(destination_class.Media.__dict__))
        for key, value in class_to_insert_dict.items():
            if key.startswith('__') and key != '__module__':
                continue
            setattr(getattr(destination_class, class_to_insert_name), key, value)
    else:
        setattr(
            destination_class, class_to_insert_name,
            class_in_class_factory(
                destination_class, class_to_insert_name, **class_to_insert_dict,
            ),
        )


def __register_class_in_app_module(app, module_name, class_to_register):
    if module_name == 'models':
        path = get_models_path_for_app(app)
    # elif module_name == 'admin':
    #     path = get_admin_path_for_app(app)
    else:
        raise ValueError('`module_name` = "{}" is not allowed'.format(module_name))

    app_module = import_module(path)
    class_name = class_to_register.__name__
    setattr(app_module, class_name, class_to_register)
    return '{}.{}'.format(path, class_name)
