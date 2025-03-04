*** Settings ***
Library    SeleniumLibrary
Library    totp_helper.py

*** Test Cases ***
Login with 2FA
    Open Browser    https://example.com    chrome
    Input Text    id=username    your_username
    Input Text    id=password    your_password
    ${totp_token}=    Get Totp Code
    Input Text    id=totp_field    ${totp_token}
    Click Button    id=login_button
    # Add assertions or further steps as needed
    [Teardown]    Close Browser
