import gettext
import locale


def auto_install():
    try:
        loc = locale.getlocale()
        if not loc[0] == "en_US":
            l10n = gettext.translation(loc[0], localedir='locales', languages=[loc[0]])
            l10n.install()
    except Exception as e:
        print(e, "\nUsing defalt language - English(en_US.UFT-8)")
    return gettext.gettext


def zh_install():
    lang_zh = gettext.translation('zh', localedir='locales', languages=['zh'])
    lang_zh.install()
    return gettext.gettext


def en_install():
    lang_zh = gettext.translation('en', localedir='locales', languages=['en'])
    lang_zh.install()
    return gettext.gettext
