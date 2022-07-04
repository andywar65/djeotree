# django-geotree
Hierarchical geo tagging Django app
## Overview
Build a hierarchical Family tree, add some Tags, create geolocalized Elements as tree leaves, attach pictures and edit Tag values. Elements can be sorted by Family, Tags, Author and by date.
## Requirements
This app is tested on Django 4.0 and Python 10.0. It relies on [django-leaflet](https://django-leaflet.readthedocs.io/en/latest/index.html/) as map engine, [django-geojson](https://django-geojson.readthedocs.io/en/latest/) for storing geodata, [django-filebrowser](https://django-filebrowser.readthedocs.io/en/latest/) for managing pictures, [django-treebeard](https://django-treebeard.readthedocs.io/en/latest/) for materialized paths and [django-htmx](https://django-htmx.readthedocs.io/en/latest/) for interactions. I use [Bootstrap 5](https://getbootstrap.com/) for styling. I develop this app inside my personal [starter project](https://github.com/andywar65/project_repo/tree/architettura) that provides all the libraries you need, along with an authentication engine. If you want to embed `django-geotree` into your project you will need to make some tweaks.
## Installation
In your project root type `git clone https://github.com/andywar65/djeotree`, add `djeotree.apps.DjeotreeConfig` to `INSTALLED_APPS` and `path(_('geotree/'), include('djeotree.urls', namespace = 'geotree'))` to your project `urls.py`, migrate and collectstatic. You also need to add initial map defaults to `settings.py` (these are the settings for Rome, change them to your city of choice):
`LEAFLET_CONFIG = {
    "DEFAULT_CENTER": (41.8988, 12.5451),
    "DEFAULT_ZOOM": 10,
    "RESET_VIEW": False,
}`
If you want a satellite map layer you need a [Mapbox](https://www.mapbox.com/) token adding this to `settings.py` (I use `environs` for secrets):
`MAPBOX_TOKEN = env.str("MAPBOX_TOKEN")`
## Families and Tags
Families and Tags may be created and managed only in Django Admin, with a `GeoTree Manager` permission group. Remember: Families are hierarchical, Tags may span over multiple Families. In example you can have a `Buildings` root Family, with `Housing` and `Services` children. A `Height` Tag may relate to a `Building` but also to a `Mushroom`. You can attach Tags to Families for a start, this is useful when you create Elements.
## Elements
Every authenticated user may create Elements and edit/delete the Elements she/he created. To create an Element you have to choose a Family the Element belongs to, describe it and locate it on the map. Saving the Element will open a new window, where you can attach images, edit Tag values and attach/detach Tags. It's important to notice that the Element inherits all the Tags attached to the parent Family and all it's ancestors way up to the root. If Families and Tags are well sorted, you will have a complete data sheet of the Element.
When you create an Element a timestamp is created, so the Element is located in space and time. You can also add a long description, and mark the Element as `Private`, so you're the only one that can access it.
## Family Paths
When a Family is sorted on the map, you will notice lines of different colors that connect all Elements of the same Family, in timestamp order. This may be useful if you create Elements on a journey, in example taking pictures of Mushrooms while you walk in a forest. Notice that if you sort by a high rank Family, all the Elements belonging to children and descendant Families will be sorted too. Private Elements are not connected by Family paths.
