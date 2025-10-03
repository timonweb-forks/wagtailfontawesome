from django.utils.html import format_html

try:
    from django.templatetags.static import static
except ImportError:  # fallback for Django <2.1
    from django.contrib.staticfiles.templatetags.staticfiles import static

try:
    from wagtail import __version__ as WAGTAIL_VERSION
    from wagtail import hooks
except ImportError:  # fallback for Wagtail <4.2
    from wagtail.core import hooks
    from wagtaill.core import __version__ as WAGTAIL_VERSION


def import_wagtailfontawesome_stylesheet():
    return format_html('<link rel="stylesheet" href="{}">',
                       static('wagtailfontawesome/css/wagtailfontawesome.css'))


# New Wagtail versions support importing CSS throughout the admin.
admin_stylesheet_hook = 'insert_global_admin_css'

hooks.register(admin_stylesheet_hook, import_wagtailfontawesome_stylesheet)
