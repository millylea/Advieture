
Feature: work with database
Background: connect to db
    * def dbHandler = Java.type('helpers.DatabaseHandler')
Scenario: Seed database with new data
    * eval dbHandler.addNewData("newname")

Scenario: Get data
    * def newdata = dbHandler.getdata("newname")
    And match newdata.email == "maimai"

