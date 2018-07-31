***Settings***
Library    SeleniumLibrary
Resource    ${EXECDIR}/common.robot

***Test Cases ***
TC-001
    [Documentation]    Login To Facebook With Valid Credentials
    Launch Chrome Browser
    Go To Facebook Login
    Enter Email Or Phone    XXXXXXXXXX    5s
    Enter Password    XXXXXXXXXX
    
TC-002
    [Documentation]    Login To Facebook With INVALID Credentials
    Launch Chrome Browser
    Go To Facebook Login
    Enter Email Or Phone    XXXXXXXXXX    10s
    Enter Password    XXXXXXXXXX
    
TC-003
    [Documentation]    Login To Facebook With special characters in Credentials
    Launch Chrome Browser
    Go To Facebook Login
    Enter Email Or Phone    ~!@#$%^&*    20s
    Enter Password    ~!@#$%^&*
    
***Keywords***
Enter Email Or Phone
    [Arguments]    ${value}    ${time}=2s
    Wait Until Element Is Visible    id=email
    Sleep    ${time}
    Input Text    id=email    ${value}

Enter Password
    [Arguments]    ${value}
    Wait Until Element Is Visible    id=pass
    Input Text    id=pass    ${value}
