import gettext
import locale
from pkg_resources import resource_filename
import platform
import matplotlib.pyplot as plt


def auto_install():
    try:
        loc = locale.getlocale()
        if not loc[0] == "en_US":
            l10n = gettext.translation(loc[0], localedir=resource_filename(__name__, 'data/locale'), languages=[loc[0]])
            l10n.install()
            return l10n.gettext
    except Exception as e:
        print(e, "\nUsing defalt language - English(en_US.UFT-8)")


def zh_install():
    osName = platform.system()
    if osName == 'Windows':
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    elif osName == 'Darwin':
        plt.rcParams['font.sans-serif'] = ['Heiti TC']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    lang_zh = gettext.translation('zh_CN', localedir=resource_filename(__name__, 'data/locale'), languages=['zh_CN'])
    lang_zh.install()
    return lang_zh.gettext


def en_install():
    lang_zh = gettext.translation('en', localedir=resource_filename(__name__, 'data/locale'), languages=['en'])
    lang_zh.install()
    return lang_zh.gettext
