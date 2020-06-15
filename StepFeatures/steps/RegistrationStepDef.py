from behave import *
from selenium import webdriver


@given(u'User is on Registration Page')
def step_impl(context):
    # Write the below line first.
    # context.driver.find_element_by_id().send_keys()
    # context.driver.find_element_by_name().send_keys()
    context.driver.find_element_by_xpath('//input[@value="Sign up"]').click()


@when(u'User enters username')
def step_impl(context):
    context.driver.find_element_by_name("fld_username").send_keys("abcd")


@when(u'User enters email id')
def step_impl(context):
    context.driver.find_element_by_name("fld_email").send_keys("abcd@gmail.com")


@when(u'User enters password')
def step_impl(context):
    context.driver.find_element_by_name("fld_password").send_keys("password")


@when(u'User clicks on Sign Up Button')
def step_impl(context):
    context.driver.find_element_by_xpath('//input[@value="Sign up"]').click()


@then(u'User should be registered successfully')
def step_impl(context):
    print("Registered")


@when(u'User enters duplicate username')
def step_impl(context):
    print("Entered Duplicate Username")


@then(u'User should not be registered successfully.')
def step_impl(context):
    print("Not Registered")
