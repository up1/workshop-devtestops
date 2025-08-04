*** Settings ***
Library    SeleniumLibrary
Test Teardown    Close All Browsers

*** Variables ***
${URL}    http://www.google.com
${SELENIUM_URL}    http://selenium-hub:4444/wd/hub

*** Test Cases ***
Open Browser
    Open Browser    ${URL}    chrome   remote_url=${SELENIUM_URL}
    Maximize Browser Window