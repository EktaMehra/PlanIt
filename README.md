# PlanIt - Event Management Platform

## Live Website

[Deployed PlanIt Application](https://planitbyem-195a427d54d7.herokuapp.com/)

## Project Overview
!Mockup (responsive page screenshot)
PlanIt is an intuitive event management platform that allows users to create, manage, and book events effortlessly. Whether you're an event organizer or an attendee, PlanIt streamlines the process of event discovery, registration, and management.

# Objective

The purpose of this project is to demonstrate my proficiency in Full-Stack web development using Django, HTML, CSS, JavaScript, and Python. The project follows best practices in software development, including Object-Oriented Programming, database management, testing, and deployment.

# Features

## Navbar
![Nav bar](assets/features/nav-box.jpg)
A responsive navigation bar that allows users to easily navigate between different sections of the site, including Home, Login, and Register.
## Page Description
![Page description](assets/features/description.jpg)
 

## Search Section
![Search section](assets/features/search-bar.jpg)
A search functionality that enables users to filter events by name or category in real-time, providing a seamless browsing experience.

## Event List
![Event list](assets/features/events-list.jpg)
A paginated list displaying available events with essential details like name, description, date, and category, making it easy for users to find and explore events.

## Event Detail
![Event details]
A dedicated page for each event, providing in-depth details, including event description, location, date, and time, along with a booking option.

## Create Event Page
![Create event](assets/features/create_event_page.jpg)
Allows registered users to create new events by filling out a form with event details.
![CRUD function](assets/features/CRUD-function.jpg)
Update Event: Any changes made to an event are updated in real-time:
- Edit Event: Users who have created the event can modify that event details after creation.
- Delete Event: Users who have created the event can remove their events if necessary.

## Register Page
![Register](assets/features/registeration-page.jpg)
- New users can create an account to create and manage their events on the page.
- The registration page link is in the navigation bar and at the bottom of the login page.
- To become a member, the user has to enter a username and password.
- If the provided username and password are valid, the user is automatically taken to the login page where they can then enter their credentials to create events.
### Validation
![Username validation](assets/features/)
- If the entered username is already taken, the form shows an error message and asks the user to use a different username. 
- After fixing the username and reentering the same password twice, the user can submit the form successfully.

## Login Page
![Login](assets/features/login-page.jpg)
- Registered users can log in to create, edit, and manage their events.
- If an unregistered user wants to create events, they have to log in.
- The user can reach the login page by the link in the navigation bar or through links available throughout the website.
- To log in, the user needs to have their username and password registered on the register page.
- If the username and/or password are incorrect, the page indicates an error.

## Book Event
![Book event](assets/features/book-event.jpg)
Users can book available events by providing their name and email, ensuring a simple and streamlined booking process.

## Messaging
![Alert Messages](assets/features/messaging.jpg)
Upon 

## Footer
![Footer](assets/)
A simple footer providing copyright information.

## Additional Features for Future Enhancements

- **Categories Section:** A separate section where users can directly browse events by category.
- **Social Sharing:** Users will have the ability to share events via social media platforms.
- **Payment Integration:** Option to include payment processing for paid events.
- **Email Notification:** Send an notification to users on their email id upon booking an event.

## Testing

### Manual Testing

- Ensuring core features function as expected by manually testing event creation, searching, and booking.
- I shared the website with multiple users to confirm its functionality and to get feedback on their experience.

### Automated Testing

- Unit tests will be implemented for critical functionalities such as user authentication, event creation, and booking processes.

### Validation

- **Python:** 

Code validated using PEP8 to maintain coding standards.

- **HTML:** 

Checked using the W3C HTML validator.

- **CSS:** 

Verified for errors using the W3C CSS validator.

- **JavaScript:** 

Console logs and debugging tools were used to ensure smooth execution.

- **Bugs:**
There are no known unfixed bugs. Identified and fixed any issues encountered during testing.


- **Lighthouse Report:**

![Lighthouse Report](assets/)  
The website was tested with Google Lighthouse.

## Development Process

### Development Preparation

- Initial project setup, including database configuration, static file management, and necessary dependencies.

### Agile Development

- Following an iterative approach to implement features step by step while continuously testing and improving the platform.

- **Git**

- I started the program and repository by using the gitpod python template provided by the Code Insitute.
- Then I regularly staged my changes using the command git add . and then committed the staged changes to my local repository using git commit -m 'short descriptive message here'.
- Finally, I would push the commits from my local repository up to the GitHub repository using the command git push.
- With every push, Heroku automatically deploys my latest commit from the 'main' branch to the Heroku app.

### Deployment

**Deployment Prepration**
Before the deployment, the following steps were taken to prepare the application for the deployment on Heroku:
- The setting DEBUG in the settings.py was set to FALSE.
- All the dependencies were stored in the requirements.txt file with the command `pip3 freeze --local > requirements.txt`.
- The start command for the application `web: gunicorn event_manage.wsgi` was stored in a Procfile.

**Setup**
The steps to deploy an app to Heroku are as follows:
- Create a new App from the Heroku dashboard.
- Enter a name for the app and select a region, then click on "Create App".
- On the page of the app that opens, go to the "Settings" tab.
- In Settings add the necessary config vars, for this project I added my cloudinary URL, database URL, and django secret key
- Next, add the buildpack "Heroku/Python".
- Afterwards, go to the "Deploy" tab on the app page.
- In the "Deployment method" section, select "GitHub" and follow the steps to connect Heroku with GitHub.
- Then, in the "Connect to GitHub" section, search for the repository that is supposed to be deployed and click on "Connect".
- The last step is to deploy a branch manually by selecting the branch and clicking the button "Deploy Branch" in the "Manual deploys" section.

## Content and Media
- All the articles were either copied from [Eventbrite](https://www.eventbrite.co.uk/) or are made up.
- All the images were downloaded from [Pexels](https://www.pexels.com/).
- All the icons on the website are from [FontAwesome](https://fontawesome.com/).

## Credits & Acknowledgments

- **Code Institute** for guidance and learning resources.
- **Bootstrap & FontAwesome** for styling and icons.
- **Cloudinary** for media file management.
- **Django Documentation** for framework best practices.

---

This project was built as part of the Code Institute Full-Stack Development course.