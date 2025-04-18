# Test Script Overview

## Purpose
The test script is designed to validate a signup form on a web application. It performs several tests to ensure that:
- Valid input leads to a successful redirect to the dashboard.
- Invalid input triggers appropriate alerts.

## Tests Implemented

1. **Test for Valid Signup**
   - **Description**: Fills out the form with valid data and submits it.
   - **Expected Outcome**: The user should be redirected to the dashboard.
   
2. **Test for Empty Fields**
   - **Description**: Submits the form without filling in required fields.
   - **Expected Outcome**: An alert should indicate that the first name is required.

3. **Test for Invalid Email**
   - **Description**: Submits the form with an invalid email format.
   - **Expected Outcome**: An alert should indicate that a valid email is required.

4. **Test for Invalid Phone Number**
   - **Description**: Submits the form with a phone number that does not meet the length requirement.
   - **Expected Outcome**: An alert should indicate that a valid phone number is required.

5. **Test for Space in First Name**
   - **Description**: Submits the form with a space as the first name.
   - **Expected Outcome**: An alert should indicate that the first name cannot be empty.

## Test Output Summary

### Results

### Explanation of Results

1. **Test: Empty Fields - PASSED**
   - This test successfully triggered the alert for missing required fields.

2. **Test: Invalid Email - PASSED**
   - This test successfully triggered the alert for an invalid email format.

3. **Test: Valid Signup - ERROR**
   - **Issue**: An unexpected alert ("Please enter a valid email address") appeared when attempting to check the current URL after form submission.
   - **Impact**: This error prevented the test from verifying if the user was redirected to the dashboard.

4. **Test: Invalid Phone - FAILED**
   - **Issue**: The expected alert ("Please enter a valid phone number (10-15 digits)") did not appear. Instead, the alert "Please select a gender" was shown.
   - **Impact**: This discrepancy caused the test to fail, indicating that the validation logic may not be working as intended.

5. **Test: Space in First Name - FAILED**
   - **Issue**: The expected alert ("First name can't be empty") was not displayed. Instead, the alert "Please enter a valid email address" appeared.
   - **Impact**: This mismatch indicates potential issues in the form validation logic.

## Conclusion
The test script effectively checks for valid and invalid inputs on the signup form. However, the presence of unexpected alerts during valid submissions and mismatched alert messages for invalid inputs highlights issues with the form's validation logic. Further debugging of the form's JavaScript validation may be necessary to align the expected alerts with actual behavior.

### Next Steps
- Review and correct the JavaScript validation logic in the signup form.
- Ensure that alerts are handled appropriately to prevent interference with test flow.
- Re-run the tests after making necessary adjustments to validate the changes.