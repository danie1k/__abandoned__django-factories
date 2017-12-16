from django import forms

from .helpers import get_admin_path_for_app

__all__ = ['model_admin_form_class_factory']


def model_admin_form_class_factory(model_class, media_fields=None, meta_fields=None, **fields):
    if not(isinstance(media_fields, dict) or media_fields is None):
        raise AttributeError('`media_fields` must be dict or None.')
    if not(isinstance(meta_fields, dict) or meta_fields is None):
        raise AttributeError('`media_fields` must be dict or None.')

    fields['__module__'] = '{app_admin_path}.{admin_class_name}'.format(
        app_admin_path=get_admin_path_for_app(model_class),
        admin_class_name=model_class.__name__,
    )

    form_class = type(
        '{}AdminForm'.format(model_class.__name__),
        (forms.ModelForm, ),
        fields,
    )

    if media_fields or meta_fields:
        from .tools import set_class_in_class

        if media_fields:
            set_class_in_class(form_class, 'Media', media_fields)
        if meta_fields:
            set_class_in_class(form_class, 'Meta', meta_fields)

    return form_class
