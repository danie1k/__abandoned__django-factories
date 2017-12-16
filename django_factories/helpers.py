from collections import Mapping
from importlib import import_module

SEQ = (tuple, list)


def dict_merge(to_dict, from_dict):
    """

    :param to_dict:
    :param from_dict:
    :return:
    """
    for key, _unused in from_dict.items():
        if key not in to_dict:
            to_dict[key] = from_dict[key]
        elif isinstance(to_dict[key], dict) and isinstance(from_dict[key], Mapping):
            dict_merge(to_dict[key], from_dict[key])
        elif isinstance(to_dict[key], SEQ) and isinstance(from_dict[key], SEQ):
            to_dict[key] = type(to_dict[key])(list(to_dict[key]) + list(from_dict[key]))
        else:
            to_dict[key] = from_dict[key]


def get_admin_path_for_app(app_or_model_class):
    """

    :param app_or_model_class:
    :return:
    """
    return __get_app_package_path('admin', app_or_model_class)


def get_models_path_for_app(app_or_model_class):
    """

    :param app_or_model_class:
    :return:
    """
    return __get_app_package_path('models', app_or_model_class)


def import_module_obj(name):
    """

    :type name: str
    :return: obj
    """
    module_name = '.'.join(name.split('.')[:-1])
    class_name = name.split('.')[::-1][0]
    try:
        return getattr(import_module(module_name), class_name)
    except AttributeError as ex:
        raise ImportError from ex


def intermediate_model_name(name_prefix, parent_model):
    """

    :type name_prefix: str
    :type parent_model: object
    :rtype: str
    """
    # pylint:disable=protected-access
    return '{prefix}For{app_label}{class_name}'.format(
        prefix=name_prefix,
        app_label=parent_model._meta.app_label.capitalize(),
        class_name=parent_model._meta.object_name,
    )


def __get_app_package_path(package_type, app_or_model_class):
    """

    :param package_type:
    :return:
    """
    models_path = []
    found = False

    if isinstance(app_or_model_class, str):
        app_path_str = app_or_model_class
    elif hasattr(app_or_model_class, '__module__'):
        app_path_str = app_or_model_class.__module__
    else:
        raise RuntimeError('Unable to get module path.')

    for item in app_path_str.split('.'):
        if item in ['models', 'admin']:
            models_path.append(package_type)
            found = True
            break
        else:
            models_path.append(item)

    if not found:
        models_path.append(package_type)

    return '.'.join(models_path)
