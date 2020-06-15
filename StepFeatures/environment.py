from selenium import webdriver


# Before All -- It will opens once and After All -- It will close Once
# def before_all(context):
#     context.driver = webdriver.Chrome()
#     context.driver.get("https://thetestingworld.com/testings/")
#
#
# def after_all(context):
#     context.driver.close()
#


# def before_feature(context, feature):
#     context.driver = webdriver.Chrome()
#     context.driver.get("https://thetestingworld.com/testings/")
#
#
# def after_feature(context, feature):
#     context.driver.close()

# def before_scenario(context, scenario):
#     context.driver = webdriver.Chrome()
#     context.driver.get("https://thetestingworld.com/testings/")
#
#
# def after_scenario(context, scenario):
#     context.driver.close()

# def before_tag(context, tag):
#     context.driver = webdriver.Chrome()
#     context.driver.get("https://thetestingworld.com/testings/")
#
#
# def after_tag(context, tag):
#     context.driver.close()

def before_step(context, step):
    context.driver = webdriver.Chrome()
    context.driver.get("https://thetestingworld.com/testings/")


def after_step(context, step):
    context.driver.close()
