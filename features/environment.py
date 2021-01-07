from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from app.application import Application

def browser_init(context):
    """
    :param context: Behave context
    """
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')
    options.headless = False
    context.driver = webdriver.Chrome(options=options)

    # context.driver = webdriver.Chrome(desired_capabilities={"proxy": {"proxyType": "MANUAL", "httpProxy": "localhost:8888"}})
    # context.driver = webdriver.Chrome(desired_capabilities={"chromeOptions": {"args": ["--start-fullscreen"]}})
    # context.driver = webdriver.Chrome()
    # context.driver = webdriver.Firefox(executable_path = "C:\Webdrivers\geckodriver")
    # context.driver = webdriver.Edge(executable_path = "C:\Webdrivers\MicrosoftWebDriver")
    # context.browser = webdriver.Safari()

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 15)

    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name, '.')
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step, '.')


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step, '.')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
    print('\nTest done: ', feature, '!')