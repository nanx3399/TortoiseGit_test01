"""
===============
Author:Nan Xi
Time:  
Email:nanxi0309@gmail.com
===============
"""
from appium import webdriver


# # 准备启动参数
capability = {
    # 设备操作系统
    "platformName": "Android",
    # 系统版本
    "platformVersion": "7.1.2",
    # 设备名称（随意填写），不能为空
    "deviceName": "OppoReno",
    # 应用程序的包名
    "appPackage": "com.ziroom.ziroomcustomer",
    # 应用程序的启动页面
    "appActivity": "com.ziroom.ziroomcustomer.WelcomeActivity"

}
#
# 创建一个driver对象
driver = webdriver.Remote(command_executor = 'http://127.0.0.1:4723/wd/hub',
                 desired_capabilities= capability)

# 设置隐式等待
driver.implicitly_wait(10)

# 我要出租
# 1.点击业主委托页
driver.find_element_by_xpath("//*[@text='业主委托']").click()
# 2.点击允许获取位置信息
# YunXu = 'new UiSelector().text("允许")'
# driver.find_element_by_android_uiautomator(YunXu)
driver.find_element_by_xpath("//*[@text='允许']").click()
# 3.点击关闭弹窗X
driver.find_element_by_id("com.ziroom.ziroomcustomer:id/tv_ok").click()
# 4.点击我的
driver.find_element_by_id("com.ziroom.ziroomcustomer:id/rl_tab_my").click()
# 5.点击登录/注册
driver.find_element_by_id("com.ziroom.ziroomcustomer:id/tv_user_name").click()
# 6.输入用户名/手机号
driver.find_element_by_xpath("//*[@text='请输入用户名/手机号/邮箱']").send_keys("16621253279")
# 7.输入密码
driver.find_element_by_xpath("//*[@text='请输入密码']").send_keys("qwerty")
# 8.点击登录
driver.find_element_by_id("com.ziroom.ziroomcustomer:id/btn_login").click()

