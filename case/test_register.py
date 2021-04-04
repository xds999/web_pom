from pages.register_page import RegisterPage


class TestRegister():

    def test_register_success(self, driver, base_url):
        '''测试注册成功案例 数据清理账号'''
        register = RegisterPage(driver, base_url)
        register.open("/users/register/")
        # 操作步骤
        register.input_email("65321@qq.com")
        register.input_password("123456")
        register.click_register_btn()
        # 实际结果
        actual_result = register.register_success_text()
        # 断言
        assert actual_result != "尊敬的用户，您好，账户已激活成功！"

    def test_register_email_existed(self, driver, base_url):
        '''测试注册成功案例'''
        register = RegisterPage(driver, base_url)
        register.open("/users/register/")
        # 操作步骤
        register.input_email("65321@qq.com")
        register.input_password("123456")
        register.click_register_btn()
        # 实际结果
        actual_result = register.register_success_text()
        # 断言
        assert actual_result != "尊敬的用户，您好，账户已激活成功！"

