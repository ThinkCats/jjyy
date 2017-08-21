webderiver = require 'selenium-webdriver'
chrome = require 'selenium-webdriver/chrome'
path = require('chromedriver').path

By = webderiver.By

main = ->

    service = new chrome.ServiceBuilder(path).build()
    chrome.setDefaultService(service)

    driver = new webderiver.Builder().withCapabilities(webderiver.Capabilities.chrome()).build()

    driver.get 'http://www.baidu.com'
    title = await driver.getTitle()
    console.log 'title:',title
    driver.quit()

main()

