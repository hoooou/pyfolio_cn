import gettext
import locale


def auto_install():
    try:
        loc = locale.getlocale()
        if not loc[0] == "en_US":
            l10n = gettext.translation(loc[0], localedir='locale', languages=[loc[0]])
            l10n.install()
            return l10n.gettext
    except Exception as e:
        print(e, "\nUsing defalt language - English(en_US.UFT-8)")



def zh_install():
    lang_zh = gettext.translation('zh_CN', localedir='data/locale', languages=['zh_CN'])
    lang_zh.install()
    return lang_zh.gettext


def en_install():
    lang_zh = gettext.translation('en', localedir='locales', languages=['en'])
    lang_zh.install()
    return lang_zh.gettext
