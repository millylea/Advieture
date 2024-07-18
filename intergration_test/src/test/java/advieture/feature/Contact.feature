Feature: Tests for Contacting
Background: url
    Given url apiURL

Scenario: Contacting
    Given path "lien-he"
    And header Content-Type = 'application/x-www-form-urlencoded'
    And form field name = 'nerd'
    And form field phone = '123456'
    And form field email = '11@1231'
    And form field subject = '12312'
    And form field message = '14124'
    And form field btnGuiThongtin = 'Gửi'
    When method Post
    Then status 200