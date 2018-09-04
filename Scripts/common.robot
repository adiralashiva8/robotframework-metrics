*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Launch Chrome Browser
    [Documentation]    Launch chrome browser with google url as default
    Open Browser    https://www.google.com    chrome
    Wait Until Element Is Visible    name=q
    Location Should Be    https://www.google.com/

Go To Facebook Login
    Go To    https://www.facebook.com/login
    Wait Until Element Is Visible    name=login
    Location Should Be    https://www.facebook.com/login