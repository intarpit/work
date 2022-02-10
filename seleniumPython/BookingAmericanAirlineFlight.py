
#? Importing the required libraries.
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

#? Creating a funtional test case.
def bookflight():
    #? Starting the driver and opening the required webpage.
    path = "F:\\Scholad project\\chromedriver97.exe"
    driver = webdriver.Chrome(path)
    driver.get("https://www.aa.com/homePage.do")
    time.sleep(1)
    
    #? Capturing the first elements and sending the required data.
    flight_from = driver.find_element_by_id("reservationFlightSearchForm.originAirport")
    flight_from.click()
    flight_from.clear()
    flight_from.send_keys("EWR")

    #? Capturing the second elements and sending the required data.
    fligt_to = driver.find_element_by_id("reservationFlightSearchForm.destinationAirport")
    fligt_to.click()
    fligt_to.send_keys("SFO")

    #? Capturing the third elements and sending the required data.
    no_of_passangers = Select(driver.find_element_by_id("flightSearchForm.adultOrSeniorPassengerCount"))
    no_of_passangers.select_by_index('2')
    

    #? Capturing the fourth elements and sending the required data.
    depart_date = driver.find_element_by_id("aa-leavingOn")
    depart_date.click()
    depart_date.send_keys("02/03/2021")

    #? Capturing the fifth elements and sending the required data.
    return_date = driver.find_element_by_id("aa-returningFrom")
    return_date.click()
    return_date.send_keys("02/10/2021")

    #? Capturing the sixth elements and sending the required data.
    search_button = driver.find_element_by_id("flightSearchForm.button.reSubmit")
    search_button.click()
    
    #? Keeping the browser open for 10 seconds so some others things can be verified if needed.
    time.sleep(10)


#? Calling the function for booking flight test case.
bookflight()