# Test Cases for PlanIt Project

| **Testcase**                          | **Expected Result**                                                       | **Test Result** |
|---------------------------------------|---------------------------------------------------------------------------|-----------------|
| **Homepage**                          |                                                                           |                 |
| Open the Homepage                     | Homepage loads with the correct template and data                         | ✅ PASS          |
| Search for an event                   | Events matching the search query are displayed                            | ✅ PASS          |
| Pagination on Homepage                | Clicking pagination links loads the correct events                        | ✅ PASS          |
| **User Registration and Login**       |                                                                           |                 |
| Register a user with valid data       | Request is successful, user is registered and logged in                   | ✅ PASS          |
| Register a user with invalid data     | Request fails, form loads again with data and errors                      | ✅ PASS          |
| Login a user with valid data          | Request is successful, user is logged in                                  | ✅ PASS          |
| Login a user with invalid data        | Request fails, form loads again with data and errors                      | ✅ PASS          |
| Logout a user                         | User is successfully logged out                                           | ✅ PASS          |
| **Event Management**                  |                                                                           |                 |
| Open the "My Events" page             | Page loads with events created by the logged-in user                      | ✅ PASS          |
| Create an event with valid data       | Event is successfully created and added to the list of events             | ✅ PASS          |
| Create an event with invalid data     | Request fails, form loads again with data and errors                      | ✅ PASS          |
| Edit an event                         | Event data is successfully updated, success message is shown              | ✅ PASS          |
| Delete an event                       | Event is successfully deleted, success message is shown                   | ✅ PASS          |
| **Event Details and Booking**         |                                                                           |                 |
| Open an event detail page             | Event Detail page loads with the correct template and data                | ✅ PASS          |
| Open an event detail page with invalid URL | 404 Error page is shown                                                 | ✅ PASS          |
| Book an event with valid data         | Booking is successful, success message is shown                           | ✅ PASS          |
| Book an event with invalid data       | Request fails, form reloads with data and errors                          | ✅ PASS          |
| **Unauthorised Requests**             |                                                                           |                 |
| Access "My Events" page without login | Request fails, redirect to login page                                     | ✅ PASS          |
| Create an event without login         | Request fails, redirect to login page                                     | ✅ PASS          |
| Edit an event without login           | Request fails, redirect to login page                                     | ✅ PASS          |
| Delete an event without login         | Request fails, redirect to login page                                     | ✅ PASS          |
| Book an event without login           | Booking form is displayed (public booking allowed without login)          | ✅ PASS          |
