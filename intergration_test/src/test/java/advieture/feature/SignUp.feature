

Feature: Sign up new user
    Background: Preconditions
        * def dataGenerator = Java.type('helpers.DataGenerator')
        * def randomEmail = dataGenerator.getRandomEmail()
        * def randomUsername = dataGenerator.getRandomUsername()
        Given url apiURL

    Scenario: Create new user and log in
        Given path "tao-tai-khoan"
        And header Content-Type = "application/x-www-form-urlencoded"
        And form field last_name = "Test"
        And form field first_name = "Testing"
        And form field username = randomUsername
        And form field phone = "1234509876"
        And form field email = randomEmail
        And form field password = "1"
        And form field confirm_password = "1"
        And form field btnRegister = "Đăng Ký"
        When method Post
        Then status 200
        * print randomUsername
      
        Given path "dang-nhap"
        And header Content-Type = "application/x-www-form-urlencoded"
        And form field username = randomUsername
        And form field email = randomEmail
        When method Post
        Then status 200
    
     Scenario Outline:  Validate sign up error
        Given path "tao-tai-khoan"
        And header Content-Type = "application/x-www-form-urlencoded"
        And form field last_name = "<last_name>"
        And form field first_name = "<first_name>"
        And form field username = "<username>"
        And form field phone = "<phone>"
        And form field email = "<email>"
        And form field password = "<password>"
        And form field confirm_password = "<confirm_password>"
        And form field btnRegister = "Đăng Ký"
        When method Post
        Then status 400
        And match response contains <errorResponse>

        Examples:
            | last_name |   first_name|username      | phone |email            |  password | confirm_password        | errorResponse                                      |
            | abc       |   def       |aaa           | 123456|randomEmail      |  12345    |     12345               | "Tên dăng nhập đã tồn tại"                |
            | abc       |   def       |randomUsername| 123456|aaa@gmail.com    |  12345    |     12345               |  "Email đã tồn tại"                        |


