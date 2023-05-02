import datetime


class AppInfo:
    APP_NAME = "WinChatGPTAPI"

    APP_AUTHOR = "Sunny8747"

    APP_AUTHOR_WEBSITE = "https://github.com/Sunny8747/WinChatGPTAPI"

    APP_VERSION = "0.0.0"

    # todo: change this
    APP_FIRST_VERSION_RELEASED = datetime.datetime(2023, 10, 1)

    APP_LICENSE = "GPLv3"

    @classmethod
    def getCopyright(cls):
        return f"{cls.APP_AUTHOR} " \
               f"© {cls.APP_FIRST_VERSION_RELEASED.year}-{datetime.datetime.now().year}"

    @classmethod
    def getProjectInfo(cls):
        return f"{cls.APP_NAME} v{cls.APP_VERSION} " \
               f"by {cls.APP_AUTHOR} " \
               f"({cls.APP_LICENSE})"
