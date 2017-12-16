__all__ = ['class_in_class_factory']


def class_in_class_factory(parent_class, name, bases=None, **fields):
    if not (isinstance(bases, tuple) or bases is None):
        raise TypeError('`bases` must be tuple.')

    fields['__module__'] = '{parent_class_module_name}.{parent_class_name}'.format(
        parent_class_module_name=parent_class.__module__,
        parent_class_name=parent_class.__name__,
    )

    return type(name, bases or (object, ), fields)
