# coding=utf-8
from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver import Firefox, FirefoxOptions


def firefox_browser():
    """print('生成Firefox浏览器driver')"""
    opt = webdriver.FirefoxOptions()
    # options.add_argument('--headless')
    # opt.add_argument('--disable-gpu')
    opt.set_preference('permissions.default.image', 2)

    # # 禁用浏览器缓存
    # opt.set_preference("network.http.use-cache", False)
    # opt.set_preference("browser.cache.memory.enable", False)
    # opt.set_preference("browser.cache.disk.enable", False)
    # opt.set_preference("browser.sessionhistory.max_total_viewers", 3)
    # opt.set_preference("network.dns.disableIPv6", True)
    # opt.set_preference("Content.notify.interval", 750000)
    # opt.set_preference("content.notify.backoffcount", 3)
    #
    # # 有的网站支持   有的不支持
    # opt.set_preference("network.http.pipelining", True)
    # opt.set_preference("network.http.proxy.pipelining", True)
    # opt.set_preference("network.http.pipelining.maxrequests", 32)
    # opt.add_argument('--start-maximized')

    # selenium firefox设置代理(默认是0，就是直接连接；1就是手工配置代理)
    opt.set_preference('network.proxy.type', 0)
    # 指定下载路径
    # opt.set_preference('browser.download.dir', self.excel_file_dir)
    # 设置成 2 表示使用自定义下载路径；设置成 0 表示下载到桌面；设置成 1 表示下载到默认路径
    opt.set_preference('browser.download.folderList', 2)
    # 在开始下载时是否显示下载管理器
    opt.set_preference('browser.download.manager.showWhenStarting', False)
    # 设置正确的文件的Content_Type
    opt.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/octet-stream')
    # 设置浏览器语言
    opt.set_preference("intl.accept_languages", "zh-CN")

    driver = webdriver.Firefox(options=opt)
    return driver


def firefox_browser_no_display():
    """print('生成无界面Firefox浏览器driver')"""
    opt = FirefoxOptions()  # 创建Firefox 参数对象
    opt.add_argument('-headless')  # 把Firefox 设置成无界面模式，windows/Linux 皆可
    driver = Firefox(options=opt)  # 创建无界面对象
    return driver


def chrome_browser():
    """print('生成Chrome浏览器driver')"""
    prefs = {"": ""}
    prefs["credentials_enable_service"] = False
    prefs["profile.password_manager_enabled"] = False
    opt = webdriver.ChromeOptions()
    # opt.add_argument('headless')
    opt.add_argument('--start-maximized')  # 最大化运行（全屏窗口）,不设置，取元素会报错
    opt.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    opt.add_experimental_option("prefs", prefs)  # 屏蔽'保存密码'提示框
    opt.add_argument("--disable-blink-features")
    opt.add_argument("--disable-blink-features=AutomationControlled")
    opt.add_experimental_option("excludeSwitches", ["enable-logging"])
    opt.add_experimental_option('excludeSwitches', ['enable-automation'])  # 以开发者模式启动调试chrome，可以去掉提示受到自动软件控制
    driver = Chrome(options=opt)
    return driver


def chrome_browser_no_display():
    """print('生成无界面Chrome浏览器driver')"""
    prefs = {}
    prefs["credentials_enable_service"] = False
    prefs["profile.password_manager_enabled"] = False
    opt = ChromeOptions()  # 创建 Chrome 参数对象
    opt.add_argument('--start-maximized')  # 最大化运行（全屏窗口）,不设置，取元素会报错
    opt.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    opt.add_experimental_option("prefs", prefs)  # 屏蔽'保存密码'提示框
    opt.add_argument('-headless')  # 把Chrome设置成无界面模式，windows/Linux 皆可
    # opt.headless = True  # 把Chrome 设置成无界面模式，windows/Linux 皆可
    driver = Chrome(options=opt)  # 创建无界面对象
    # driver = Chrome()
    return driver


def phantomjs_browser():
    # print('生成PhantomJS浏览器driver')
    driver = webdriver.PhantomJS()
    return driver
