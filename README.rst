================
django-factories
================
Simple classes factories for Django Framework.

*******************
Available functions
*******************

Factories
---------
- ``class_in_class_factory`` (`usage example <#class_in_class_factory>`_)
- ``inline_model_admin_class_factory``
- ``intermediate_m2m_model_class_factory``
- ``model_admin_form_class_factory``
- ``polymorphic_child_admin_class_factory``

Tools & wrappers
----------------
- ``add_fields_to_model``
- ``register_model_in_app``
- ``set_class_in_class`` (`usage example <#set_class_in_class>`_)

**************
Usage examples
**************

``class_in_class_factory``
--------------------------
.. code-block:: python

    from django_factories import class_in_class_factory
    from myapp.admin import MyModelAdmin

    media_class_fields = {
        'js': ['path/to/javascript/file.js'],
    }

    # MyModelAdmin.Media will be overwritten if exists
    MyModelAdmin.Media = class_in_class_factory(MyModelAdmin, 'Media', **media_class_fields)

``set_class_in_class``
--------------------------
It's wrapper for ``class_in_class_factory``, which has implemented some logic for merging with already existing   classes:

.. code-block:: python

    from django_factories import set_class_in_class
    from myapp.admin import MyModelAdmin

    media_class_fields = {
        'js': ['path/to/javascript/file.js'],
    }
    # Existing MyModelAdmin.Media will merged with new Media class, so you won't loose any existing data
    set_class_in_class(MyModelAdmin, 'Media', media_class_fields)


More will come later...
