
Feature: Booking
Background: precondition
    Given url apiURL
    * def dbHandler = Java.type('helpers.DatabaseHandler')

Scenario: get tour
    Given path "Danh-sach-tour/1"
    When method Get
    Then status 200
    And match response contains "Tour Miền Bắc"

    Given path "tour/11"
    When method Get
    Then status 200
    And match response contains "Vịnh Hạ Long"

    Given path "dat-tour/11"
    When method Get
    Then status 200
@debug
Scenario: book tours
    Given path "dat-tour/11"
    And header Content-Type = "application/x-www-form-urlencoded"
    And form field p_name = "ami" 
    And form field p_birthday = "2000"
    And form field p_phone = "12345"
    And form field p_address = "sg"
    And form field adult_quantity = 2
    And form field children_quantity = 1
    And form field discount = 0
    And form field btnCheckout = "Tiến Hành Đặt"
    When method Post
    Then status 200
    * def booking_id = dbHandler.getBookingID("ami", "12345").id

    Given path "tien-hanh-dat/", booking_id
    When method Get
    Then status 200
    And match response contains "Tổng Tiền"

    Given path "tien-hanh-dat/", booking_id
    And header Content-Type = "application/x-www-form-urlencoded"
    And form field btnPayment = "Thanh Toán"
    When method Post
    Then status 200


