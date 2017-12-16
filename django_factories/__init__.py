"""django-factories"""
from .admin_class_factories import *  # noqa pylint:disable=wildcard-import
from .model_class_factories import *  # noqa pylint:disable=wildcard-import
from .other_class_factories import *  # noqa pylint:disable=wildcard-import
from .tools import *  # noqa pylint:disable=wildcard-import
from .settings import *  # noqa pylint:disable=wildcard-import

__version__ = '0.1'


# def inline_product_options_admin_form_metaclass_factory(parent_klass, parent_klass_model):
#     return type(
#         # param: name
#         'Meta',
#         # param: bases
#         (
#             object,
#         ),
#         # param: dict
#         {
#             '__module__': '{}.{}'.format(parent_klass.__module__, parent_klass.__name__),
#
#             'model': parent_klass_model,
#             'exclude': [],
#             'widgets': {
#                 'option': autocomplete.ModelSelect2(),
#                 'values': autocomplete.ModelSelect2Multiple(
#                     url='admin:productoptionvalue-autocomplete',
#                     forward=['option'],
#                 ),
#             },
#         },
#     )


# def inline_product_options_admin_form_factory(model_klass, admin_klass):
#     intermediate_model_name = create_intermediate_model_name('ProductOptionsFor', model_klass)
#     inline_model_klass = getattr(
#         import_module(get_app_models_path(model_klass)),
#         intermediate_model_name
#     )
#
#     form_attrs = {
#         '__module__': admin_klass.__module__,
#     }
#     class_name = '{}AdminForm'.format(intermediate_model_name)
#
#     form_meta = type('Meta', (object, ), )
#
#     return type(class_name, (forms.ModelForm, ), form_attrs)
