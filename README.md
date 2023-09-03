# Exclusive Restaurant

Exclusive Restaurant is a web application that allows users to make restaurant bookings. It is built using various technologies and frameworks and deployed using Heroku, Cloudinary and ElephantSQL, a description of all these is provided below. Here is a link to the deployed website. \
**Note:** This booking system would not be a whole restaurants website but only the booking system feature for one. This app has full functionality for authentication and creating bookings but is only a basic app and should be included in and styled to suit a full restaurant website. The current version has very little CSS and is mainly styled with Bootstrap classes to allow custom classes to be added to elements when integrating into a larger project.

## Technologies and Frameworks Used

- **Django**: A high-level Python web framework.
- **HTML/CSS**: For building the website's front-end.
- **JavaScript**: For adding interactivity to the front-end.
- **Bootstrap**: A front-end framework for responsive web design.
- **Python**: The primary programming language used in the back-end.
- **PostgreSQL**: A powerful, open-source relational database.
- **Heroku**: A cloud platform for deploying web applications.
- **ElephantSQL**: A PostgreSQL database hosting service.
- **Cloudinary**: A cloud-based image and video management service.
- **Allauth**: A Django package for user authentication and registration.

## Features

- **Main Homepage**: The main landing page provides an introduction to the restaurant and its booking service.\
<img src="images/homepage.png" alt="Homepage screenshot">

- **User Authentication**: Users can create accounts and log in using the Allauth package.
<img src="images/login.png" alt="Login page screenshot">

- **Booking Page**: Users can select dates and times to make restaurant bookings.
- **Messages Section**: Below the header there is a messages section where users are informed of actions they take. Login, logout successful bookings and cancelations are shown here.
- **Bookings List**: Above the booking form a list of any bookings a user has made is shown here with the option to cancel the booking.
<img src="images/booking.png" alt="Booking page screenshot">

- **Admin Panel**: Admins can access an admin panel to create and cancel bookings for users.
<img src="images/admin.png" alt="Login page screenshot">

