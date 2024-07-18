
Feature: Tests for homepage
    Background: url
        Given url apiURL
    Scenario: homepage
        When method Get
        Then status 200
        And match response == "#string"
        And match response contains "Trang Chủ"

    Scenario: Search keyword
        Given path "tim-kiem/"
        Given params {keyword: "ninh"}
        When method Get
        Then status 200
        And match response contains "Tìm thấy 7 tour"


    Scenario: Search tours
        Given path "tim-kiem/"
        Given params {departure_id: "2", category_id: "1", departure_date: "06-07-2024"}
        When method Get
        Then status 200
        And match response contains "Tìm thấy 2 tour"


