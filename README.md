# Taste of India
 
Welcome to Taste of India, the perfect destination for lovers of authentic Indian cuisine. Our website is designed to provide you with a seamless and immersive experience, where you can not only explore our menu but also make table reservations with ease. We understand the value of your time, so we've made it easy for you to secure a table at your preferred time and date. Additionally, we also have a meal blog page, where you can read about the various dishes we offer, see other user reviews and leave one of your own. We hope that our website will help you discover the taste of India and bring you closer to our culture and traditions.

![Taste of India](/static/assets/readme-media/home.png)

## Features 

### Existing Features

- __Navigation Bar__

  - Featured on all pages, the full responsive navigation bar includes links to the Logo/Name, Home, Menu, Bookings, Meals, About page, Sign Up / Register section. Identical in each page to allow for easy navigation.
  - The navigation bar is responsive and will collapse into a hamburger menu when used on medium and small screens.
  - This section will allow the user to easily navigate from page to page across all devices without having to revert back to the previous page via the ‘back’ button. 

![Nav Bar](/static/assets/readme-media/navbar.png)

- __The Landing Page Image__

  - The landing page has a photograph with text overlay informing the user what Taste of India offers.
  - This section is an informative section that tells the user what can be found on the website.
  - The user will be advised early as to what is available to them on Taste of India and can make an informed decision as to what page they'd like to visit.

![Landing Page](/static/assets/readme-media/landing.png)

- __About Us Section__

  - The about us section provides information on opening times, contact info and location of Taste of India. 
  - The details are made available to the user for any queries they may have or for planning their visit. 

![About Us](/static/assets/readme-media/about.png)

- __Sign Up Section__

  - This section will allow the user to register to Taste of India.
  - This enables the user to then make table reservations.

![Register / Login](/static/assets/readme-media/sign-up.png)

- __The Footer__ 

  - The footer section includes links to the relevant social media sites for Taste of India. The links will open to a new tab to allow easy navigation for the user.
  - The footer is valuable to the user as it encourages them to stay connected via social media

![Footer](/static/assets/readme-media/footer.png)

- __Menu__

  - The menu is stored on a PDF which can be accessed through the Navigation bar.
  - This opens a new browser tab with the menu displayed.

![Menu](/static/assets/readme-media/menu.png)

- __Bookings Page__

  - This page shows a list of the users bookings.
  - The page also includes an edit and delete option beside each booking.
  - The page is responsive to all screen sizes and will adjust the size of the table accordingly.
  - This will provide the user with all their booking information and the option to edit or cancel. 

![Bookings](/static/assets/readme-media/bookings.png)

- __Meals Page__

  - The Meals page contains blog like post for meals offered by Taste of India.
  - The meals link to a detail page where users can like and leave reviews.
  - This gives the user an insight into each dish and lets them have their say.

![Meals](/static/assets/readme-media/mealblog.png)

### Future Feature Ideas

- __Available Booking Slots__

  - Only show available time slots for selected date on the booking form.
  - This will eliminate the option a user has to try and book an unavailable time slot.

- __Filter Meals__

  - User can filter the Meal posts by the meals they have liked.
  - User can filter the Meal posts the meal type (Starter, Main, Side Dish, Dessert, Drink).

- __Take Bookings From Unregistered Users__

  - Give unregistered users the ability use the booking system

- __Booking Confirmations__

  - Send an email confirmation of booking details on submission of a successful booking.

## Design

A startbootstap theme was used as a template design which I could then build upon. This enabled a HTML foundation which could then be designed to suit the theme of the restaurant.

[Theme](https://startbootstrap.com/theme/business-casual)

## Testing 

The Taste of India site works as intended.
All sections were tested; Some of the main testing points included:

| Test       | Expected           | Passed  |
| :------------- |:-------------:| :-----:|
| User clicks all navigation links on home page     | Taken to corresponding page | ✅ |
| User clicks 'Menu(pdf)' button      | Opens new tab with a PDF of the Menu | ✅ |
| User logs in / registers | Nav links change and booking becomes available | ✅ |
| User clicks 'Make Reservation'| Directed to create booking page | ✅ |
| User completes booking form and submits (valid data) | Booking created and redirected to Bookings page with feedback message | ✅ |
| User completes booking form and submits (invalid data)| Error / Invalid messages | ✅ |
| User clicks update booking | Directed to update booking page with prepopulated form | ✅ |
| User updates booking (valid data) | Booking details updated successfully and redirected to Bookings page with feedback message | ✅ |
| User updates booking (invalid data) | Error / Invalid messages | ✅ |
| User clicks delete icon | Modal opens with corresponding booking information | ✅ |
| User clicks modal Delete button | Booking is deleted, feedback message and booking list updated | ✅ |
| User clicks modal No button | Modal closes | ✅ |
| User clicks outside modal area (while modal is open)| Modal closes | ✅ |
| User submits a review | An alert appears telling the user their review is waiting approval | ✅ |
| Admin adds a meal blog (draft) | new meal blog post created but not displayed on website | ✅ |
| Admin adds a meal blog (published) | new meal blog post created and displayed on website | ✅ |
| Admin approves user reviews | review is shown on the corresponding meal post and review count increased| ✅ |
| User clicks like button on a meal | Like is added to like count | ✅  |
| User clicks like button on a meal (already liked) | Like is removed from like count | ✅  |


The website was shared with family and friends to test the websites usage.

### Validator Testing 

- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2F8000-kizmistry-tasteofindia2-q9ygssujmqb.ws-eu93.gitpod.io%2Fbooking_list.html%2F)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](http://jigsaw.w3.org/css-validator/validator?lang=en&profile=css3svg&uri=https%3A%2F%2F8000-kizmistry-tasteofindia2-q9ygssujmqb.ws-eu93.gitpod.io%2F&usermedium=all&vextwarning=&warning=1)
- JS
  - No errors were found when passing script.js and map.js through JSHint

### Unfixed Bugs

- There is a minor bug with the delete icons on the bookings page: there is no response when clicking directly on the 'trash' icon.
- Amend url patterns



## Deployment

The process of deploying Taste of India to GitHub is detailed below: 

- Create a new app on Heroku and connect it to GitHub account
- Enable Automatic Deploys to automatically deploy code to Heroku whenever changes are pushed to the main branch of the GitHub repository
- Set up the required environment variables in the Heroku app settings (such as your database connection string or any API keys)
- Create a Procfile to specify the command that Heroku should use to start your app
- Make sure code is production-ready by running any necessary build or compilation steps, and ensuring that all dependencies are properly installed
- Push code to the main branch of the GitHub repository to trigger a deployment to Heroku
- Monitor the deployment logs in the Heroku dashboard to ensure that the app is starting up correctly and there are no errors. 

The live link can be found here - https://taste-of-india.herokuapp.com/


## Credits 

### Content 

- All icons used are from [Font Awesome](https://fontawesome.com/)

### Media

- All images used are from [Pexels](https://www.pexels.com)

