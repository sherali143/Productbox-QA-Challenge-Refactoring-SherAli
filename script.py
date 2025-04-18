import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestSignUpForm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up the WebDriver
        cls.driver = webdriver.Chrome()
        cls.driver.get("file:///C:/Users/Sher%20Ali/Desktop/Productbox-QA-Challenge/Buggy%20Website.html")

    def check_for_alert(self):
        """Check if an alert is present and accept it."""
        try:
            WebDriverWait(self.driver, 1).until(EC.alert_is_present())
            alert_text = self.driver.switch_to.alert.text
            self.driver.switch_to.alert.accept()  # Close the alert
            return alert_text
        except:
            return None

    def test_valid_signup(self):
        """Test that valid input leads to the dashboard."""
        self.check_for_alert()  # Handle any unexpected alerts
        self.fill_form(first_name="Sher", last_name="Ali", father_name="Tauqeerabbas", 
                       email="sher.ali@example.com", phone="1234567890", 
                       dob="1990-01-01", country="USA", city="New York")
        self.driver.find_element(By.ID, "submit-btn").click()

        # Wait for redirection to dashboard
        time.sleep(5)
        self.assertIn("dashboard.html", self.driver.current_url)
        print("Test: Valid Signup - PASSED")

    def test_empty_fields(self):
        """Test that alerts are shown for empty required fields."""
        self.driver.find_element(By.ID, "submit-btn").click()
        alert_text = self.check_for_alert()
        self.assertIn("First name can't be empty", alert_text)
        print("Test: Empty Fields - PASSED")

    def test_invalid_email(self):
        """Test that alerts are shown for invalid email."""
        self.check_for_alert()  # Handle any unexpected alerts
        self.fill_form(first_name="John", last_name="Doe", father_name="Richard Doe", 
                       email="invalid-email", phone="1234567890", 
                       dob="1990-01-01", country="USA", city="New York")
        self.driver.find_element(By.ID, "submit-btn").click()
        
        alert_text = self.check_for_alert()
        self.assertIn("Please enter a valid email address", alert_text)
        print("Test: Invalid Email - PASSED")

    def test_invalid_phone(self):
        """Test that alerts are shown for invalid phone number."""
        self.check_for_alert()  # Handle any unexpected alerts
        self.fill_form(first_name="John", last_name="Doe", father_name="Richard Doe", 
                       email="john.doe@example.com", phone="1234", 
                       dob="1990-01-01", country="USA", city="New York")
        self.driver.find_element(By.ID, "submit-btn").click()

        alert_text = self.check_for_alert()
        self.assertIn("Please enter a valid phone number (10-15 digits)", alert_text)
        print("Test: Invalid Phone - PASSED")

    def test_space_in_first_name(self):
        """Test that alerts are shown for space in first name."""
        self.check_for_alert()  # Handle any unexpected alerts
        self.fill_form(first_name=" ", last_name="Doe", father_name="Richard Doe", 
                       email="john.doe@example.com", phone="1234567890", 
                       dob="1990-01-01", country="USA", city="New York")
        self.driver.find_element(By.ID, "submit-btn").click()

        alert_text = self.check_for_alert()
        self.assertIn("First name can't be empty", alert_text)
        print("Test: Space in First Name - PASSED")

    def fill_form(self, first_name, last_name, father_name, email, phone, dob, country, city):
        """Helper method to fill out the signup form."""
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "father-name").send_keys(father_name)
        self.driver.find_element(By.ID, "email").send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter Phone Number']").send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter Date of birth']").send_keys(dob)
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter Country']").send_keys(country)
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter City']").send_keys(city)

    @classmethod
    def tearDownClass(cls):
        """Close the browser after tests are done."""
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()