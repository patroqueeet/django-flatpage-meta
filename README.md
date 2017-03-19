This is a quick upgrade for any site using Django FlatPages.

Installation
============

Add flatpage_meta to your INSTALLED_APPS, run syncdb


Use:
===

Put this into your FlatPage template:

    {% load flatpage_meta_tags %}
    {% flatpage_meta_tags flatpage %}
    
and/or this into into your site's base template.

    {% load flatpage_meta_tags %}
    {% flatpage_meta_tags %}


Administration:
==============

Edit your meta data inline on your FlatPage and Site models.

Migrations & Initial Data
===============
```
./manage.py migrate flatpage_meta
./manage.py loaddata $(PATH_TO_LIB)/flatpage_meta/fixtures/initial_data.json
```

Add Admin
==========
```
from flatpage_meta.admin import ReplacementFlatPageAdmin

class FlatPageAdmin(ReplacementFlatPageAdmin):
	pass

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
```

