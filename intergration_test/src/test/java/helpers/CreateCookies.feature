Feature: Create Cookie
Scenario: Create Cookie
        Given url apiURL 
        Given path "dang-nhap"
        And header Content-Type = "application/x-www-form-urlencoded"
        And form field username = 'aaa'
        And form field password = '1'
        And form field btnDangnhap =  "Đăng Nhập"
        When method Post
        Then status 200
        * def authsession = responseCookies.sessionid.value
        * print authsession