from django.contrib.admin.utils import flatten, flatten_fieldsets

__all__ = ['polymorphic_child_admin_class_factory']


def _get_fields(new_admin_fields):
    def get_fields(self, request, obj=None):
        fields = type(self).__bases__[0].get_fields(self=self, request=request, obj=obj)
        return fields + new_admin_fields

    return get_fields


def _get_fieldsets(new_admin_fieldsets):
    def get_fieldsets(self, request, obj=None):
        fieldsets = type(self).__bases__[0].get_fieldsets(self=self, request=request, obj=obj)
        return fieldsets + new_admin_fieldsets

    return get_fieldsets


def polymorphic_child_admin_class_factory(
        base_model, bases=None, admin_fields=None, admin_fieldsets=None):
    if not (isinstance(bases, tuple) or bases is None):
        raise TypeError('`bases` must be tuple.')

    if admin_fields and admin_fieldsets:
        raise ValueError('`admin_fields` and `admin_fieldsets` cannot be set at the same time.')

    admin_parent_class = bases[0]  # FIXME: May need refactoring in future!

    fields = {
        '__module__': base_model.__module__,
    }

    if admin_parent_class.fields:
        parent_admin_fields = flatten(admin_parent_class.fields)
    else:
        parent_admin_fields = flatten_fieldsets(admin_parent_class.fieldsets)

    parent_admin_fields += ['id', 'pk', 'order', 'ordering', ]

    inheritor_admin_fields = [item.name for item in base_model._meta.fields]
    new_admin_fields = set(filter(
        lambda item: not (item.endswith('_ptr') or item.endswith('_ctype')),
        set(inheritor_admin_fields) - set(parent_admin_fields)
    ))

    if admin_parent_class.fields:
        if admin_fieldsets:
            raise ValueError(
                '{} does not allow `admin_fieldsets`, please use `admin_fields`.'.format(bases[0].__name__)
            )

        if admin_fields:
            fields['get_fields'] = _get_fields(admin_fields)
        else:
            fields['get_fields'] = _get_fields(new_admin_fields)

    elif admin_parent_class.fieldsets:
        if admin_fields:
            raise ValueError(
                '{} does not allow `admin_fields`, please use `admin_fieldsets`.'.format(bases[0].__name__)
            )

        if not admin_fieldsets:
            admin_fieldsets = (
                (base_model.__name__, {
                    'fields': tuple(new_admin_fields),
                }),
            )

        fields['get_fieldsets'] = _get_fieldsets(admin_fieldsets)

    else:
        raise NotImplementedError

    class_name = '{}ChildAdmin'.format(base_model.__name__)

    return type(class_name, bases, fields)
