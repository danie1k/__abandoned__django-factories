from django.contrib.admin.options import InlineModelAdmin

__all__ = ['inline_model_admin_class_factory']


def inline_model_admin_class_factory(inline_model, admin_class, **fields):
    """

    :param inline_model:
    :param admin_class:
    :param fields:
    :return:
    """
    if not issubclass(admin_class, InlineModelAdmin):
        raise ValueError('`admin_class` must subclass InlineModelAdmin.')

    if isinstance(inline_model, str):
        from django.apps import apps as django_apps
        inline_model = django_apps.get_model(inline_model)

    return type(
        '%sInlineAdmin' % inline_model.__name__,
        (admin_class, ),
        {
            '__module__': admin_class.__module__,
            'model': inline_model,
            **fields,
        },
    )
