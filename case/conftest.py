import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import platform
from pages.register_page import RegisterPage
from common.connect_msysql import DbConnect, dbinfo
from pages.users_login_page import UsersLoginPage
from pages.users_feedbackiframe_page import UsersFeedbackiframePage
from pages.users_userinfo_page import UsersUserInfoPage

def pytest_addoption(parser):
    '''添加命令行参数'''
    parser.addoption(
        "--headless",action="store",
        default='no',help='set chrome headless option yes or no'
    )

@pytest.fixture(scope="session", name="driver")
def browser():
    '''定义全局driver'''
    # windows系统
    if platform.system() == 'Windows':
        # driver = webdriver.Chrome()
        # driver.maximize_window()
        chrome_optins = Options()
        chrome_optins.add_argument('--Windows-size =1920,1080')
        chrome_optins.add_argument('--headless')
        driver = webdriver.Chrome(chrome_options=chrome_optins)
        yield driver
        # quit是退出浏览器
        driver.quit()
    else:
        chrome_optins = Options()
        chrome_optins.add_argument('--Windows-size =1920,1080')
        chrome_optins.add_argument('--no-sandbox')
        chrome_optins.add_argument('--disable-dev-shm-usage')
        chrome_optins.add_argument('--disable-gpu')
        chrome_optins.add_argument('--headless')


@pytest.fixture(scope="session")
def base_url():
    url = "http://49.235.92.12:8200"
    return url

@pytest.fixture(scope="session")
def db():
    _db = DbConnect(dbinfo, "online")
    yield _db
    _db.close()


@pytest.fixture(scope="session")
def registerPage(driver, base_url):
    register = RegisterPage(driver, base_url)
    return register

@pytest.fixture(scope="session")
def usersLoginPage(driver, base_url):
    usersLogin = UsersLoginPage(driver, base_url)
    return usersLogin


@pytest.fixture(scope="session")
def usersFeedbackPage(driver, base_url):
    feedback = UsersFeedbackiframePage(driver, base_url)
    return feedback

@pytest.fixture(scope="session")
def login_driver(driver, usersLoginPage:UsersLoginPage):
    '''用户先登陆，返回driver'''
    usersLoginPage.open("/users/login/")
    usersLoginPage.input_login_username("1234@qq.com")
    usersLoginPage.input_login_password("123456")
    usersLoginPage.click_login_btn()
    return driver


@pytest.fixture(scope="session")
def userInfoPage(login_driver, base_url):
    '''需先登陆, 返回已登陆的页面对象'''
    userInfo = UsersUserInfoPage(login_driver, base_url)
    return userInfo