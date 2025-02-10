# PlanIt - Event Management Platform

## Live Website

[Deployed PlanIt Application](https://planitbyem-195a427d54d7.herokuapp.com/)

## Project Overview

PlanIt is an intuitive event management platform that allows users to create, manage, and book events effortlessly. Whether you're an event organizer or an attendee, PlanIt streamlines the process of event discovery, registration, and management.

## Objective

The purpose of this project is to demonstrate proficiency in Full-Stack web development using Django, HTML, CSS, JavaScript, and Python. The project follows best practices in software development, including Object-Oriented Programming, database management, testing, and deployment.

## Features

### **User Authentication**

- Users can register, log in, and log out securely.
- Username validation ensures that no two users share the same username.

### **Event Management**

- Create, update, and delete events.
- View event details including description, date, time, location, and category.

### **Search & Filtering**

- Users can search for events by name or category.
- Implemented real-time search filtering using JavaScript.

### **Booking System**

- Users can book events without logging in.
- Organizers can view the list of booked users.

### **Pagination & Navigation**

- Events are displayed with pagination for better user experience.
- Navigation bar ensures seamless access to different pages.

### **Responsive Design**

- Fully mobile-friendly and accessible across different devices.
- Enhanced UI/UX with Bootstrap styling.

### **Error Handling & Messages**

- Users receive confirmation messages for successful event creation, updates, and booking.
- Clear error messages guide users in case of invalid inputs.

## Technologies Used

### **Backend**

- Python & Django
- PostgreSQL (Database)

### **Frontend**

- HTML, CSS (Bootstrap for styling)
- JavaScript (Search filtering & username validation)

### **Hosting & Storage**

- Deployed on Heroku
- Cloudinary for media file storage

## Installation & Setup

### **Clone the Repository**

```sh
$ git clone https://github.com/EktaMehra/PlanIt.git
$ cd PlanIt
```

### **Create and Activate a Virtual Environment**

```sh
$ python -m venv venv
$ venv\Scripts\activate  # On Windows
```

### **Install Dependencies**

```sh
$ pip install -r requirements.txt
```

### **Set Up Environment Variables**

Create a `.env` file and add the following:

```sh
SECRET_KEY='your-secret-key'
DATABASE_URL='your-database-url'
CLOUDINARY_URL='your-cloudinary-url'
```

### **Apply Migrations & Run the Server**

```sh
$ python manage.py migrate
$ python manage.py runserver
```

## Deployment (Heroku)

1. Create a Heroku app:
   ```sh
   $ heroku create planitbyem
   ```
2. Add the Heroku remote repository:
   ```sh
   $ heroku git:remote -a planitbyem
   ```
3. Push the code to Heroku:
   ```sh
   $ git push heroku main
   ```
4. Run database migrations:
   ```sh
   $ heroku run python manage.py migrate
   ```
5. Set up environment variables in Heroku:
   ```sh
   $ heroku config:set SECRET_KEY='your-secret-key'
   $ heroku config:set DATABASE_URL='your-database-url'
   $ heroku config:set CLOUDINARY_URL='your-cloudinary-url'
   ```
6. Open the deployed application:
   ```sh
   $ heroku open
   ```

## Testing

### **Manual Testing**

- Verified all core functionalities like event creation, searching, and booking.
- Tested responsiveness on different devices.
- Ensured smooth navigation between pages.

### **Automated Testing**

- Django unit tests were implemented for event creation, user authentication, and booking system.
- Run tests with:
  ```sh
  $ python manage.py test
  ```

## Future Enhancements

- Implement user profiles for event organizers.
- Allow attendees to leave reviews and ratings for events.
- Add event reminders via email notifications.
- Improve search functionality with advanced filters.

## Credits & Acknowledgments

- **Code Institute** for guidance and learning resources.
- **Bootstrap & FontAwesome** for styling and icons.
- **Cloudinary** for media file management.
- **Django Documentation** for framework best practices.

---

This project was built as part of the Code Institute Full-Stack Development course.

