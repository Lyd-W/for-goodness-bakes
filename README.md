# For Goodness Bakes

Deployed link: [For Goodness Bakes](https://for-goodness-bakes-app-93b97c50dd02.herokuapp.com/ "For Goodness Bakes | Heroku")

A full stack Django web application where users can browse recipes and, once logged in, create, edit, and delete comments on recipes. For Goodness Bakes is a relaxed and friendly community for bakers of all levels to come together for interaction and support from similar minded individuals. The platform focuses on clean UX, accessibility, secure authentication, and robust CRUD functionality.

![For Goodness Bakes](docs/homepage.png)

### [Contents](#contents)
* [Project Rationale](#project-rationale)
* [User Goals](#user-goals)
* [User Stories](#user-stories)
* [User Feedback](#user-feedback)
* [Website Goals](#website-goals)
* [Website Objectives](#website-objectives)
* [Target Audience](#target-audience) 
* [Wireframes](#wireframes)
* [Design Choices](#design-choices)
    + [Typography](#typography)
    + [Colour Scheme](#colour-scheme)
    + [Images](#images)
    + [Responsiveness](#responsiveness)
* [Security Measures and Protective Design](#security-measures-and-protective-design)
    + [User Authentication](#user-authentication)
    + [Password Management](#password-management)
    + [Form Validation](#form-validation)
    + [Database Security](#database-security)
* [Features](#features)
    * [Existing Features](#existing-features)
        + [Favicon](#favicon)
        + [Header](#header)
        + [Home Section](#home-section)
        + [Registration](#registration)
        + [Login Section](#login-section)
        + [About Section](#about-section)
        + [Recipe Detail Section](#recipe-detail-section)
        + [Comment Section](#comment-section)
        + [Success Page](#success-page)
        + [Error Pages](#error-page)
        + [Footer](#footer)
        + [Django Admin Panel](#django-admin-panel)
    * [Future Enhancements](#future-enhancements)
* [Technologies Used](#technologies-used)
    * [Languages](#languages)
    * [Libraries and Frameworks](#libraries-and-frameworks)
    * [Tools and Programmes](#tools-and-programmes)
* [Database Design and Data Modelling](#database-design-and-data-modelling)
    * [Date Model](#data-model)
    * [Entity Relationship](#entity-relationship)
    * [Entity Relationship Diagram](#entity-relationship-diagram)
* [Testing](#testing)
    * [Bugs](#bugs)
    * [Responsiveness Tests](#responsiveness-tests)
    * [Code Validation](#code-validation)
        + [HTML](#html)
        + [CSS](#css)
        + [JavaScript](#javascript)
    * [User Story Testing](#user-story-testing)
    * [Feature Testing](#feature-testing)
    * [Accessibility Testing](#accessibility-testing)
    * [Lighthouse Testing](#lighthouse-testing)
    * [Browser Testing](#browser-testing)
* [Deployment](#deployment)
* [Credits](#credits)

## Project Rationale

Many existing recipe websites prioritise monetisation through advertisements, pop-ups, autoplay media, and external links. While this approach may generate revenue, it often results in busy, distracting interfaces that interrupt the user’s focus and negatively impact the overall user experience. For users seeking a calm, supportive environment to explore recipes and share baking experiences, these platforms can feel overwhelming and impersonal.

Additionally, although many recipe platforms include social features such as likes or ratings, these mechanisms can discourage meaningful interaction. Users may become overly focused on numerical validation rather than genuine discussion, which can lead to comparison, reduced participation, or reluctance to engage. Comment sections, when thoughtfully designed, encourage richer interaction by allowing users to share advice, ask questions, and offer support in a more conversational and human way.

For Goodness Bakes was created to address these issues by providing a clean, distraction-free recipe platform centred around community interaction rather than popularity metrics. The application intentionally avoids advertisements and intrusive UI elements, allowing users to focus on content and engagement without interruption. Interaction is facilitated through moderated comment functionality rather than likes or ratings, promoting thoughtful discussion and reducing pressure associated with public metrics.

Moderation plays a key role in maintaining a positive and welcoming environment. By implementing an approval system for comments and restricting editing and deletion to the original author or administrators, the platform supports respectful interaction while protecting users from spam or inappropriate content. This approach reflects real-world community management practices and demonstrates the importance of backend logic in enforcing frontend behaviour and user permissions.

The project targets home bakers and food enthusiasts seeking a friendly, supportive space to share experiences and improve their skills. Django was selected as the framework for this application due to its robust authentication system, strong support for relational data modelling, and built-in security features. These capabilities allow for clear separation of concerns between models, views, and templates, ensuring maintainable code, secure data handling, and a seamless connection between backend logic and frontend presentation.

[Back to contents](#contents)

## User Goals

### Public Users:
* Display all recipes for public users, authenticated users and admin.
* Each recipe has an individual detail page for public users, authenticated users and admin to view.
* Public users can read comments on recipes.
* Public users can register for an account.

### Authenticated Users:
* Authenticated users can log in and out.
* Authenticated users can create comments on recipes with immediate UI feedback.
* Authenticated users can edit and delete their own comments with immediate UI feedback.

### Admin:
* Admin can create, edit and delete recipes.
* Admin can moderate comments.

[Back to contents](#contents)

## User Stories

### Public Users:
* As a public user, I want to browse a list of recipes and view individual recipe details so that I can find recipes to bake without needing to register.
* As a new user, I want to create an account and log in securely so that I can participate in commenting on recipes.

### Authenticated Users:
* As an authenticated user, I want to add comments to recipes so that I can share feedback, baking tips and interact with other users.
* As an authenticated user, I want to edit my own comment so that I can correct mistakes or update my advice.
* As an authenticated user, I want to delete my own comment so that I can remove content I no longer want displayed.

### Admin:
* As an admin, I want to create new recipes so that fresh content can be added to the site for users to explore.
* As an admin, I want to edit existing recipes so that I can correct errors or improve recipe content.
* As an admin, I want to delete recipes so that outdated or incorrect content can be removed.
* As an admin, I want to manage user comments so that inappropriate or spam content can be removed.

These user stories have been prioritised using the MoSCoW Prioritisation method. GitHub Project Board was then used to manage workflow and track progress towards completion of each story and ensuring all required elements of the user stories were met.

![GitHub Project Board](docs/github-project-board.png)

[Back to contents](#contents)

## User Feedback

Feedback was gathered informally through family and friends reviewing and testing during development. Users highlighted the clean and welcoming design, ease of navigation, and clarity of recipe information as key strengths.

Positive feedback included:
- The website is easy to navigate across devices.
- Recipe pages are clear and well structured.
- Commenting functionality is intuitive and responsive.
- The colour palette and typography create a calm, friendly atmosphere.

Suggested improvements included:
- Adding search or filtering options for recipes.
- Allowing users to save favourite recipes.
- Expanding UI beyond comments.

These suggestions have been considered and are documented within the Future Enhancements section.

[Back to contents](#contents)

## Website Goals

The key website goals are to provide users with a safe community to browse recipe ideas and, when authenticated, engage with the community through posting, editing and deleting their own comments. Administrators will provide this safe community through their ability to moderate user comments and add or amend recipe information. 

[Back to contents](#contents)

## Website Objectives

* To provide clearly structured and visually appealing recipe content for public users, authenticated users and admin, ensuring information is easy to find, read and navigate across different devices.
* To provide intuitive navigation onto individual recipe pages from the recipe listing page, keeping the layout consistent with clear information and easily accessible navigation controls.
* Enable secure registration for new users, with clear UI confirmation.
* Enable secure log in/out for existing users, with clear UI confirmation.
* Ability for only authenticated users to comment on recipes, including editing and deleting thier own comments successfully, with prior prompting before deletion and activity confirmation.
* All sensitive user and site data is suitably protected, following best practice for secure data handling.
* Allow users with administrative access to manage recipe content and moderate user comments to ensure accuracy, relevance and appropriate for the target audience.
* Ensure all data input is validated and users are clearly notified of errors in data input. 
* Inclusion of an error page to direct users back to the homepage if a broken link or error occurs.

[Back to contents](#contents)

## Target Audience

* Home bakers
* Food enthusiasts
* Users who want to discuss and improve recipes
* Beginner to intermediate bakers seeking advice
* Beginner to intermediate bakers wanting to share advice
* Users wanting to be part of a baking community
* Families

[Back to contents](#contents)


## Wireframes

Wireframes were created using [Draw.io](https://www.drawio.com/ "Draw.io Homepage"). A mobile first approach was taken throughout, the wireframes provided a visual respresentation of the expected layout and structure of the website. Within the wireframes, key element placement is visible for navigation, content and interactive areas.  

[Mobile Wireframes](docs/mobile-wireframes.png "Mobile Wireframes")

[Tablet Wireframes](docs/tablet-wireframes.png "Tablet Wireframes")

[Desktop Wireframes](docs/desktop-wireframes.png "Laptop Wireframes")

[Back to contents](#contents)

## Design Choices

### Typography

The primary font family that was chosen for For Goodness Bakes was [Playfair Display](https://fonts.google.com/specimen/Playfair+Display?query=playfair+display "Google Fonts | Playfair Display"), the soft curves of the serif style offers a warm and personal feeling to welcome users into the website. Playfair Display offers a familiar magazine feeling, helping users to feel comfortable and invited to interact with the recipes and other users. This font was used for recipe titles and headings.

The secondary font family that was chosen for For Goodness Bakes was [Lato](https://fonts.google.com/specimen/Lato "Google Fonts | Lato") due to its readability through its clean letter design and professional yet friendly appearance while remaining neutral enough to not compete with the headings. Lato offers legibility for longer bodies of text making it ideal for recipe descriptions, ingredient lists, instructions and comments.

Together, these font groups help to create visual balance, offering warmth and an easy reading experience. The use of a serif font for headings and a sans-serif font for body text also provides easy visual distinction for users.

### Colour Scheme

To visualise different colours together [Coolors Scheme](https://coolors.co/2b2b2b-faf7f2-e8b7c8-a8c3b1-c97a5d "Coolors Scheme | For Goodness Bakes") was used to create a fitting combination for the website. Graphite was chosen for the font colour for the feeling of professionalism and ease of legibility whilst being easier on the eyes which was ideal for body text, headings and icons. Parchment was used to create a calmer, welcoming approach. This creates the feeling of reading from paper, suggesting cookbook pages, giving a better UX, therefore this colour was ideal for the website background. Soft Blossom was used to bring in a comforting, feminine touch whilst not being too overpowering, and was used for buttons, links and navigation. To reinforce the calm atmosphere the website aimed for, Ash Grey was selected, this helped to bring a natural, healthier balance to the Soft Blossom because greens are often associated with food and wellness. The final colour used was Burnt Peach, being a similar colour to spices it felt a natural choice for a baking website, bringing a sharp enphasis among the other colours making it ideal for buttons such as submitting,  commenting or hovers and borders.

![Coolors Scheme](docs/coolors.png)

[Contrast Grid](https://contrast-grid.eightshapes.com/?version=1.1.0&background-colors=&foreground-colors=%23FAF7F2%0D%0A%23E8B7C8%0D%0A%23C97A5D%0D%0A%23A8C3B1%0D%0A%232B2B2B&es-color-form__tile-size=regular&es-color-form__show-contrast=aaa&es-color-form__show-contrast=aa&es-color-form__show-contrast=aa18&es-color-form__show-contrast=dnp "Contrast Grid") was used to determine the best colour combinations to ensure the website was visually appealing whilst remaining easy for the user to read the content.

![Contrast Grid](docs/contrast-grid.png)

|CSS Name               |HEX          |Use
|-----------------------|-------------|------------------------------------------------|
| --primary | #FAF7F2 | Website background colour |
| --secondary | #E8B7C8 | Log in status text  |
| --primary-highlight | #C97A5D | Button hover and borders |
| --secondary-highlight | #A8C3B1 | Current page indicator, success messages |
| --text | #2B2B2B | Primary text colour |
| --danger | #FF0000 | Danger buttons (delete, log out) |
| --success | #A8C3B1 | Success button (send, submit) |


### Images

High-quality food photography is used throughout the website to enhance visual appeal and encourage user engagement. Images were sourced from [Unsplash](https://unsplash.com/ "Unsplash | Homepage") and [Pexels](https://www.pexels.com/ "Pexels | Homepage"), ensuring consistency with the website’s warm and welcoming aesthetic.

All images are optimised for web performance to reduce load times while maintaining visual clarity. Placeholder images are used where necessary to maintain layout consistency and prevent broken image links.

Each recipe includes a featured image to help users quickly identify content and enhance the overall browsing experience.

### Responsiveness

A mobile-first approach was taken throughout the design and development process. [Bootstrap](https://getbootstrap.com/docs/5.3/layout/breakpoints/#available-breakpoints "Bootstrap Breakpoints")’s responsive grid system and utility classes were used to ensure the website adapts smoothly across all screen sizes.

The website has been tested on:
- Mobile devices
- Tablets (via [Dev Tools](https://developer.chrome.com/docs/devtools "Chrome | Dev Tools"))
- Desktop and laptop screens

Key responsive features include:
- Collapsible navigation for smaller screens
- Scalable images and typography
- Stacked layouts on mobile that expand into multi-column layouts on larger screens

This ensures a consistent and accessible user experience regardless of device.

![Breakpoints](docs/bootstrap-breakpoints.png "Bootstrap Breakpoints")

[Back to contents](#contents)

# Security Measures and Protective Design

### User Authentication

User authentication is handled using Django’s built-in authentication system. This ensures secure user registration, login, and logout functionality.

Access control is enforced so that:
- Only authenticated users can create, edit, or delete comments.
- Users can only modify or delete their own comments.
- Administrative features are restricted to superusers.

This protects user content and prevents unauthorised access or modification.

### Password Management

Passwords are securely managed using Django’s password hashing framework. Plain text passwords are never stored.

Additional measures include:
- Password confirmation during registration
- Secure password hashing algorithms
- Automatic protection against common authentication vulnerabilities

This ensures user credentials remain protected at all times.

### Form Validation

Both client-side and server-side form validation are implemented to ensure data integrity and improve user experience.

Validation includes:
- Required field enforcement
- Clear error messages displayed to users
- Prevention of invalid or empty submissions

Users receive immediate feedback if a form submission fails, helping them correct errors efficiently.

### Database Security

In order to protect sensitive configuration values, such as the Django `SECRET_KEY` and database credentials, environment variables are used. These values are stored securely using Heroku Config Vars and are never committed to the repository, with configuration files such as `env.py` excluded via `.gitignore`.

Additional security measures are implemented by ensuring `DEBUG` mode is disabled in production, restricting access using `ALLOWED_HOSTS`, and protecting against cross-site request forgery through trusted origins defined in `CSRF_TRUSTED_ORIGINS`.

The production database is not publicly accessible and can only be accessed through the Django application, ensuring users can only interact with data via the website’s features.

[Back to contents](#contents)
    
# Features

For Goodness Bakes focuses on simplicity, usability, and community interaction. Features are designed to support both casual visitors and registered users while maintaining secure content management.

## Existing Features

### Favicon

Due to the nature of For Goodness Bakes, a cupcake favicon was chosen from [Favicon](https://favicon.io/emoji-favicons/ "Favicon | Homepage") as it creates a quick visual indicator of what the website is about, whilst remaining fun and relaxed due to the cartoon style of the icon.

Key features include:
- Fun, cupcake favicon

![Favicon](docs/favicon.png "Favicon")

<br>

### Header

The header provides consistent navigation across the site and adapts responsively to different screen sizes.

Key features include:
- Website branding
- Website slogan 'Let's get baking'
- Navigation links with highlight to indicate current page in ash grey
- Authentication-aware options (login/register or logout)
- Log in status in soft blossom to highlight whether a user is logged in and the current user's username. When a user is not logged in, an encouraging message of 'Log in to get baking!' is displayed.
- Highlight hover effect in burnt peach
- Responsive across screen sizes

On smaller devices such as mobiles and tablets, the header collapses into a mobile-friendly menu then expands out for clarity on larger screens.

<br>

<b>Mobile header</b>

[Mobile header](docs/mobile-header.jpg "Mobile Header")

[Mobile header open](docs/mobile-header-open.jpg "Mobile Header Open")

<br>

<b>Tablet header</b>

[Tablet header](docs/tablet-header.png "Tablet Header")

[Tablet header open](docs/tablet-header-open.png "Tablet Header Open")

<br>

<b>Desktop header</b>

[Laptop header](docs/laptop-header.png "Laptop Header")

[Laptop header with hover effect](docs/laptop-header-hover.png "Laptop Header Hover Effect")

<br>

### Home Section

The home page displays a list of available recipes in a clean, visually appealing layout. 

Key features include:
- List of recipes displayed as cards
- Cards are resonsive when hovered over on larger screens
- Responsive on different screen sizes
- 'next' and 'prev' page buttons at the bottom of the page with hover effect in burnt peach

Each recipe card includes:
- A featured image
- Recipe title
- Short description

On larger screens, when the user hovers over a recipe, the recipe card moves slighlty to provide a better user experience. Users can click through to individual recipe pages for full details. 

<br>

[Desktop home view](docs/desktop-home-view.png "Desktop Home View")

[Desktop home view with hover effect](docs/desktop-home-view-hover.png "Desktop Home View With Hover Effect")

[Tablet home view](docs/tablet-home-view.png "Tablet Home View")

[Mobile home portrait view](docs/mobile-home-portrait-view.png "Mobile Home Portrait View")

[Mobile home landscape view](docs/mobile-home-landscape-view.png "Mobile Home Landscape View")

<br>

### Registration

New users can register for an account using a secure and intuitive form. There is a link to the log in page incase a user has incorrectly navigated to the registration page. The registration form gives validation feedback to users if they try to submit the form with an empty field that is required and offers password requirements. 

Upon successful registration, users receive clear feedback and are logged in immediately to access commenting features.

Key features include:
- User friendly form
- Link to log in page
- Form validation
- Password requirements
- Optional email address field
- Register button with hover effect in burnt peach

<br>

[Registration preview for desktop](docs/registration.png "Registration Preview | Desktop")

[Registration preview for tablet](docs/registration-tablet.png "Registration Preview | Tablet")

[Registration preview for mobile](docs/registration-mobile.png "Registration Preview | Mobile")

[Registration validation](docs/registration-validation.png "Registration Validation")

[Registration feedback](docs/registration-feedback.png "Registration Feedback")

<br>

### Login and Logout Sections

Registered users can log in securely using their credentials, there's the option to remember log in credentials for quicker access to For Goodness Bakes in the future, providing a better user experience. Incase a new user has incorrectly navigated to the log in page when they do not currently have an account, there is a link to the register page. Clear confirmation messages are displayed on successful login and logout with a prompt before logging out that includes a red hover over effect on the 'Log Out' button, improving user confidence and clarity.

Once a user has logged in, the header updates to welcome the user by username and adjusts to the navigation to the relevant options.

Key features include:
- Option to remember login credentials
- Link to registration page
- 'Log In' button with hover effect in burnt peach
- Friendly welcome message on log in page
- Adjusted navigation for logged in or logged out users
- Confirmation log out page
- 'Log Out' button with hover effect in danger

<br>

[Login preview for desktop](docs/login-desktop.png "Login | Desktop")

[Login preview for tablet](docs/login-tablet.png "Login | Tablet")

[Login preview for mobile](docs/login-mobile.png "Login | Mobile")

[Login credentials](docs/login-credentials.png "Login Credentials")

[Log out preview for desktop](docs/log-out-desktop.png "Log Out | Desktop")

[Log out preview for tablet](docs/log-out-tablet.png "Log Out | Tablet")

[Log out preview for mobile](docs/log-out-mobile.png "Log Out | Mobile")

[Log out button hover effect preview](docs/log-out-button.png "Log Out Button Hover Effect")

[Logged in user's header display preview](docs/logged-in-user-display.png "Logged In Header Display")

[Logged out user's header display preview](docs/logged-out-user-display.png "Logged Out Header Display")

<br>

### About Section

The About page introduces the purpose of For Goodness Bakes and reinforces the platform’s community-driven values. It provides users with context about the site and encourages engagement with a contact form. Keeping to the relaxed and friendly atmosphere, the contact form reads 
'Got a craving you wish to satisfy or a favourite recipe to share?
Contact us using the form below.'

Key features include:
- A featured image
- A description about For Goodness Bakes that can be modified by administrators
- Time and date stamp of when the description was last updated
- 'Get in touch' contact form
- Form 'Send' button has ash grey hover effect which is a green tone suggesting success
- Form validation
- Success message

<br>

![About](docs/about.png "About")

![About contact form](docs/about-contact-form.png "About Contact Form")

![About contact form validation](docs/about-contact-form-validation.png "About Contact Form Validation")

<br>

### Recipe Detail

Each recipe has its own dedicated detail page, providing comprehensive information for users:

- **Recipe Information:** Displays the title, featured image, ingredients, and step-by-step method.
- **Additional Details:** Includes preparation time, cooking time, servings and recipe difficulty.
- **Comment Integration:** Comments related to the recipe are displayed below the content, allowing users to interact directly.
- **Responsive Layout:** Content and images adapt seamlessly across mobile, tablet, and desktop devices.
- **Navigation:** Clear buttons and links allow users to return to the home page, browse other recipes, or perform authenticated actions (commenting, editing).
- **Accessibility:** Semantic HTML and proper contrast ensure readability for all users.

The recipe detail page combines visual appeal with clear structure to provide a smooth and engaging browsing experience.

<br>

![Recipe detail](docs/recipe-detail.png "Recipe Detail")

<br>

### Comment Section

Authenticated users can interact with recipes through a fully featured commenting system. Key functionalities include:

- **Create Comments:** Users can add new comments to any recipe, sharing feedback, baking tips, or personal experiences.
- **Edit Comments:** Users can edit their own comments to correct errors or provide updates. Edited comments update immediately in the UI.
- **Delete Comments:** Users can delete their own comments. A confirmation prompt ensures accidental deletions are avoided.
- **Real-Time Feedback:** Actions such as adding, editing, or deleting comments provide immediate visual confirmation with a success message, improving user experience.
- **Access Control:** Only authenticated users can create, edit, or delete comments. Users cannot modify comments posted by others.
- **Moderation:** Admin users have the option to authorise comments and can decline and delete inappropriate or irrelevant comments to maintain a positive community environment.

This system encourages UI while maintaining content integrity and community standards.

<br>

![Comment section | logged in](docs/comment-section.png "Comment Section | Logged In")

<br>

![Comment section | logged out](docs/comment-section-logged-out.png "Comment Section | Logged Out")

<br>

![Comment awaiting approval](docs/comment-awaiting-approval.png "Comment Awaiting Approval")

<br>

![Update comment success](docs/update-comment-success.png "Update Comment Success")

<br>

![Delete comment confirmation](docs/delete-comment-confirmation.png "Delete Comment Confirmation")

<br>

![Delete comment success](docs/delete-comment-success.png "Delete Comment Success")

<br>

### Success Page

Success messages are displayed following key user actions such as registration, login, or comment submission. These provide immediate visual confirmation that actions have been completed successfully.

<br>

![Login feedback](docs/login-feedback.png "Login Feedback")

<br>

![Logout feedback](docs/logout-feedback.png "Logout Feedback")

<br>

![Comment success](docs/comment-success.png "Comment Success")

<br>

### Error Pages

Custom 400, 403, 404 and 500 error pages are included to handle broken or invalid URLs. The error page clearly informs users that the requested content cannot be found and provides a link back to the homepage.

<br>

![400](docs/400.png "400")

<br>

![403](docs/403.png "403")

<br>

![404](docs/404.png "404")

<br>

![500](docs/500.png "500")

<br>

### Footer

The footer contains:
- Copyright information
- Social media links
- Consistent branding

It remains accessible across all pages and screen sizes.

<br>

![Footer](docs/footer.png "Footer")

<br>

### Django Admin Panel

Administrators have access to a secure, feature-rich admin panel to manage the website and community content:

- **Recipe Management:** Admins can create, edit, and delete recipes, ensuring content remains accurate and up-to-date.
- **Summernote Editing:** Summernote is integrated into the admin panel to allow text editing for recipe instructions and descriptions. Admins can:
  - Format text (bold, italics, headings)
  - Add lists, links, and images
  - Easily structure content for better readability
  This ensures recipes are visually appealing and easy to follow for all users.
- **Comment Moderation:** Admins can view, edit, and delete user comments, accepting, declining and removing inappropriate or spam content.
- **User Management:** Admins can manage user accounts, including editing user details and assigning admin privileges.
- **Secure Access:** Admin access is restricted to superusers with Django’s authentication system, preventing unauthorized access.
- **UI Feedback:** Admin actions provide immediate confirmation messages to ensure administrators are aware of successful updates or deletions.
- **Database Control:** All changes made in the admin panel directly update the database while maintaining data integrity and security.

This panel ensures that the platform remains safe, well-maintained, and engaging for all users.

<br>

## Future Enhancements

Potential future features include:
- Recipe search and filtering functionality
- User profiles
- Ability to save favourite recipes
- Expanded community interaction features
- Rating system for recipes

These enhancements would further improve user engagement and scalability.

<br>

[Back to contents](#contents)

# Technologies Used

## Languages

- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS "CSS")
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML "HTML")
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript "JavaScript")
- [Markdown](https://en.wikipedia.org/wiki/Markdown "Markdown")
- [Python](https://www.python.org/ "Python")

## Libraries and Frameworks

- [Bootstrap v5.3](https://getbootstrap.com/ "Bootstrap v5.3 Homepage")
- [Django](https://www.djangoproject.com/ "Django Homepage")
- [Favicon](https://favicon.io/ "Favicon Homepage")
- [Font Awesome](https://fontawesome.com/search?q=menu&o=r&ic=free "Font Awesome Homepage")
- [Google Fonts](https://fonts.google.com/ "Google Fonts Homepage")

## Tools and Programmes

- [Contrast Grid](https://contrast-grid.eightshapes.com/?version=1.1.0&background-colors=&foreground-colors=%23FAF7F2%0D%0A%23E8B7C8%0D%0A%23C97A5D%0D%0A%23A8C3B1%0D%0A%232B2B2B&es-color-form__tile-size=regular&es-color-form__show-contrast=aaa&es-color-form__show-contrast=aa&es-color-form__show-contrast=aa18&es-color-form__show-contrast=dnp "Contrast Grid")
- [Coolors](http://https://coolors.co/ "Coolors")
- [Draw.io](https://www.drawio.com/ "Draw.io Homepage")
- [GitHub](https://github.com "GitHub Homepage")
- [Heroku](https://www.heroku.com/ "Heroku")
- [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode "Prettier - Code Formatter")
- [VS Code](https://code.visualstudio.com/ "VS Code Homepage")
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input "W3C CSS Validation Service Homepage")
- [W3C HTML Validation Service](https://validator.w3.org/#validate_by_uri "W3C HTML Validation Service Homepage")

[Back to contents](#contents)

# Database Design and Data Modelling

The database for For Goodness Bakes has been designed to support a secure, responsive, and interactive recipe community. A relational database model was chosen to ensure data consistency, enforce relationships, and support CRUD operations efficiently.

## Data Model 

The application contains the following primary entities:
- User – Stores registered user accounts, including authentication credentials, roles (regular user or admin), and profile-related information.
- Recipe – Represents each recipe, including title, description, ingredients, method, preparation and cooking times, servings, difficulty level, and featured image.
- Comment – Represents user comments on recipes. Each comment is linked to both a recipe and a user. Comments include content, timestamps, and status (approved, pending moderation).

## Entity Relationship

The data model follows a relational structure, ensuring clear and enforceable relationships:

- A User can create multiple Comments (1-to-many).
- A Recipe can have multiple Comments (1-to-many).
- Each Comment is associated with exactly one User and one Recipe (1-to-1).
- Admin users have elevated permissions, but no separate table is required as roles are stored in the User entity.

These relationships maintain data integrity, prevent orphaned records, and allow efficient retrieval of information such as “all comments for a recipe” or “all recipes commented on by a user.”

## Entity Relationship Diagram

The Entity Relationship Diagram (ERD) shows how the main pieces of the app fit together and how they relate to each other.

Some key things to notice:
- Each entity has a primary key (User.id, Recipe.id, Comment.id) to keep everything unique.
- Foreign keys make sure the relationships are correct, for example, every comment points to a specific user and a specific recipe (Comment.user_id → User.id, Comment.recipe_id → Recipe.id).
- Data types and constraints are set up to make sure all the information is stored properly and stays consistent.

The ERD gives a clear overview of how users, recipes, and comments all connect in the database.

[ERD](docs/erd.pdf "ERD")

[Back to contents](#contents)

# Testing

## Bugs

|   Bug Description                         | Resolved |    Resolution Description                               |
|-------------------------------------------|----------|---------------------------------------------------------|

## Responsiveness Tests

## Responsiveness Tests

Manual testing was conducted across multiple devices and screen sizes both on actual devices and through [Dev Tools](https://developer.chrome.com/docs/devtools "Chrome | Dev Tools") to ensure layout consistency and usability. No significant layout issues were identified.

## Code Validation

### HTML

HTML information to be added here.

### CSS

CSS information to be added here.

### JavaScript

JavaScript information to be added here.

### Python

Python code was tested through manual testing, Django error reporting and by running the python code through [Code Institute's](https://pep8ci.herokuapp.com/ "Code Institute | CI Python Linter") Python Linter. The application runs without errors in production, and all core functionality behaves as expected.

## User Story Testing

|User Story                               | Result                                      |Pass| Evidence             |
|-----------------------------------------|---------------------------------------------|----|----------------------|
| As a public user, I want to browse a list of recipes and view individual recipe details so that I can find recipes to bake without needing to register. | Result | Pass | Evidence |
| As a new user, I want to create an account and log in securely so that I can participate in commenting on recipes. | Result | Pass | Evidence |
| As an authenticated user, I want to add comments to recipes so that I can share feedback, baking tips and interact with other users. | Result | Pass | Evidence |
| As an authenticated user, I want to edit my own comment so that I can correct mistakes or update my advice. | Result | Pass | Evidence |
| As an authenticated user, I want to delete my own comment so that I can remove content I no longer want displayed. | Result | Pass | Evidence | 
| As an admin, I want to create new recipes so that fresh content can be added to the site for users to explore. | Result | Pass | Evidence |
| As an admin, I want to edit existing recipes so that I can correct errors or improve recipe content. | Result | Pass | Evidence |
| As an admin, I want to delete recipes so that outdated or incorrect content can be removed. | Result | Pass | Evidence |
| As an admin, I want to manage user comments so that inappropriate or spam content can be removed. | Result | Pass | Evidence |

[Back to contents](#contents)

## Feature Testing

All features were tested to ensure they function correctly for their intended purpose. Authentication, comment CRUD operations, and admin controls were verified.

## Accessibility Testing

Accessibility best practices were followed, including:
- Sufficient colour contrast
- Semantic HTML
- Clear navigation structure

Contrast Grid and Lighthouse tools were used to support accessibility testing.

## Lighthouse Testing

For Goodness Bakes has been tested in [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/inspect-mode "Google Chrome Dev Tools") using the Lighthouse Testing tool to check:

* Performance - this measures the efficiency of the page loading and running.
* Accessibility - this assesses the usability of the page for all people, especially those with accessibility issues.
* Best Practices - this checks how the page compares to a set of established web development practices.
* SEO - this checks for relevance to search engines.

The site majoritively achieved strong scores across all categories with the most scores being 90+. However, the Best Practices category consistently scored 78–79 on the following pages, across desktop and mobile:

- Home page
- About page
- Recipe detail pages

The Best Practices score is reduced due to third-party cookies set by Cloudinary’s CDN. These cookies are required for secure and efficient image delivery and cannot be disabled without removing Cloudinary entirely. The application itself follows recommended security and development practices, and no insecure behaviour is introduced by the project code.

[Lighthouse - desktop](docs/lighthouse-desktop.pdf "Lighthouse | Desktop")

[Lighthouse - about desktop](docs/lighthouse-about-desktop.pdf "Lighthouse | About Desktop")

[Lighthouse - recipe detail desktop](docs/lighthouse-recipe-detail-desktop.pdf "Lighthouse | Recipe Detail Desktop")

[Lighthouse - register desktop](docs/lighthouse-register-desktop.pdf "Lighthouse | Register Desktop")

[Lighthouse - login desktop](docs/lighthouse-login-desktop.pdf "Lighthouse | Login Desktop")

[Lighthouse - log out desktop](docs/lighthouse-log-out-desktop.pdf "Lighthouse | Log Out Desktop")

[Lighthouse - mobile](docs/lighthouse-mobile.pdf "Lighthouse | Mobile")

[Lighthouse - about mobile](docs/lighthouse-about-mobile.pdf "Lighthouse | About Mobile")

[Lighthouse - recipe detail mobile](docs/lighthouse-recipe-detail-mobile.pdf "Lighthouse | Recipe Detail Mobile")

[Lighthouse - register mobile](docs/lighthouse-register-mobile.pdf "Lighthouse | Register Mobile")

[Lighthouse - login mobile](docs/lighthouse-login-mobile.pdf "Lighthouse | Login Mobile")

[Lighthouse - log out mobile](docs/lighthouse-log-out-mobile.pdf "Lighthouse | Log Out Mobile")

## Browser Testing

The website was tested on:
- Google Chrome
- Mozilla Firefox
- Microsoft Edge

No browser-specific issues were identified.

[Back to contents](#contents)

# Deployment

The project was deployed to Heroku from VS Code early on, this allowed for more opportunity to notice errors, as well as to view and test the website at regular intervals. The steps used for deployment were as follows:

## Step One - Create a New Heroku App
- Log into Heroku and access your dashboard.
- Click **"New"** from the top right corner of your dashboard and select **'Create new app'**.
- Enter a unique name for your app and choose your closest region (EU or USA), click **'Create app'** to create your app.
## Step Two - Configure Environment Variables
- Go to the **'Settings'** tab of your new app, in the **'Config Vars'** section, click **'Reveal Config Vars'**.
- Add the following keys and values:

| KEY | VALUE |
|-----|-------|
| DATABASE_URL | Insert your own PostgreSQL database URL here. |
| DISABLE_COLLECTSTATIC | Set the value to **'1'** temporarily and remove it before the final deployment. |
| SECRET_KEY | Enter a random secret key, this can be randomly generated using a website such as [Djecrety](https://djecrety.ir/ "Djecrety").

## Step Three - Prepare the Project for Deployment in the IDE
- Create a **'requirements.txt'** file to list all of the dependancies required by your project. This can be done by running **'pip3 install -r requirements.txt'** in the terminal, it can then be updated to include any other packages installed by running **'pip3 freeze --local > requirements.txt'** in the terminal.
- Install **'gunicorn'** using the command **'pip3 install gunicorn~=20.1'** in the terminal and update **'requirements.txt'**.
- Create a **'Procfile'** in the root directory of the project, add the following line of code to the Procfile **'web: gunicorn project_name.wsgi'**. Ensure project_name matches the project's name.
- Update the **'ALLOWED_HOSTS'** list in **'settings.py'** to include **'.herokuapp.com',**. 
## Step Four - Connect Your GitHub Respository to Heroku
- On the Heroku dashboard, click on the **'Deploy'** tab, in the **'Deployment method'** section, click **'GitHub Connect to GitHub'** where you will be prompted to authenticate with GitHub.
- Type your project repo name into the search box and click **'Search'**, select the correct repo name.
- Scroll down to the **'Manual Deploy'** section, ensure the **'Choose a branch to deploy'** is set to **'main'**, then click on the **'Deploy Branch'** button.
- Once the **'Your app was successfully deployed.'** message is displayed, click the **'View'** button to open your deployed project in a new tab.

[Back to contents](#contents)

# Credits

#### Feedback, advice and support

- 

#### Learning Resources and Guidance

- [Code Institute](https://codeinstitute.net/ "Code Institute")
- [MDN](https://developer.mozilla.org/en-US/ "MDN | Homepage")
- [Slack](https://slack.com/intl/en-gb/ "Slack")
- [Stack Overflow](https://stackoverflow.com/ "Stack Overflow")
- [W3 Schools](https://www.w3schools.com/ "W3 Schools")

#### Images:

All images were sourced from [Unsplash](https://unsplash.com/ "Unsplash | Homepage") and [Pexels](https://www.pexels.com/ "Pexels | Homepage") and are used in accordance with their respective free-use licences. Attribution is provided where recommended. [Squoosh](https://squoosh.app/ "Squoosh | Homepage") was used to resize the images and change file formats to webp and images were stored with [Cloudinary](https://cloudinary.com/ "Cloudinary | Homepage").

- Almond Biscotti [Cook Eat](https://www.pexels.com/photo/sliced-bread-on-green-surface-776859/ "Pexels | Cook Eat")
- [Favicon.io](https://favicon.io "Favicon.io")
- Baked Vanilla Cheesecake [A Studios](https://unsplash.com/photos/a-piece-of-cheesecake-on-a-plate-next-to-a-cup-of-tea-rWAwhghF4ag "Unsplash | A Studios")
- Banana Bread [Jeff Siepman](https://unsplash.com/photos/sliced-cakes-MssPSnkV1yM "Unsplash | Jeff Siepman")
- Blueberry Muffins [Joshua Flores](https://unsplash.com/photos/brown-cupcakes-on-white-ceramic-plate-5RQffqRkmWQ "Unsplash | Joshua Flores")
- Chocolate Cake [Polina Tankilevitch](https://www.pexels.com/photo/person-eating-chocolate-cake-4187672/ "Pexels | Polina Tankilevitch")
- Chocolate Cheesecake [American Heritage Chocolate](https://unsplash.com/photos/a-slice-of-chocolate-cheesecake-with-a-strawberry-on-top-DOWsiEekKIA "Unsplash | American Heritage Chocolate")
- Chocolate Chip Banana Bread [Dasha Klimova](https://www.pexels.com/photo/photograph-of-brown-cake-9928323/ "Pexels | Dasha Klimova")
- Chocolate Chip Cookies [Brigitte Tohm](https://www.pexels.com/photo/brown-cookies-189536/ "Pexels | Brigitte Tohm")
- Chocolate Fudge Cake [Richard Bell](https://unsplash.com/photos/a-piece-of-chocolate-cake-on-a-plate-Oul4t1hvQZQ "Unsplash | Richard Bell")
- Chocolate Mousse [American Heritage Chocolate](https://unsplash.com/photos/two-bowls-of-chocolate-pudding-with-raspberries-on-the-side-YxjIO0LmDO0 "Unsplash | American Heritage Chocolate")
- Crème Brûlée [Max Griss](https://unsplash.com/photos/white-ceramic-bowl-with-brown-soup-Wp7ZsJYWP0M "Unsplash | Max Griss")
- Double Chocolate Cookies [Karolina Bobek](https://unsplash.com/photos/cookies-on-white-and-blue-ceramic-plate-hgzPdjwSHEI "Unsplash | Karolina Bobek")
- Fudgy Chocolate Brownie [Saveurs Secretes](https://www.pexels.com/photo/slices-of-chocolate-brownies-5410404/ "Pexels | Saveurs Secretes")
- Jamie and Oliver [Julien Lenoir](https://unsplash.com/photos/a-couple-of-men-standing-next-to-each-other-in-a-kitchen-9WalxeSSSak "Unsplash | Julien Lenoir") - Image edited using [ChatGPT](https://chatgpt.com/ "ChatGPT | Homepage") to remove visible logos.
- Lemon Shortbread Cookies [Kader D. Kahraman](https://www.pexels.com/photo/heap-of-cookies-15776576/ "Pexels | Kader D. Kahraman")
- Placeholder for about - Created by [ChatGPT](https://chatgpt.com/ "ChatGPT | Homepage").
- Placeholder for recipe images [Calum Lewis](https://unsplash.com/photos/wooden-ladle-and-spatula-on-top-of-table-rkT_TG5NKF8 "Unsplash | Calum Lewis")
- Shortbread Biscuits [Shay Wood](https://www.pexels.com/photo/white-and-blue-ceramic-saucer-574125/ "Pexels | Shay Wood")
- Strawberry Victoria Sponge [Becky Fantham](https://unsplash.com/photos/fruit-cake-on-blue-cake-holder-DIUJSBiJNoc "Unsplash | Becky Fantham")
- Vanilla Blondie [Liana S](https://unsplash.com/photos/a-person-holding-a-piece-of-cake-on-a-wooden-plate-1vsupadWQDI "Unsplash | Liana S")
- Victoria Sponge [Nick Fewings](https://unsplash.com/photos/brown-bread-on-stainless-steel-plate-9t_v5yHAW-o "Unsplash | Nick Fewings")

<br>

- [Cloudinary](https://cloudinary.com/ "Cloudinary | Homepage")
- [Squoosh](https://squoosh.app/ "Squoosh | Homepage")
- [Pexels](https://www.pexels.com/ "Pexels | Homepage")
- [Unsplash](https://unsplash.com/ "Unsplash | Homepage")

#### Content:

- [ChatGPT](https://chatgpt.com/ "ChatGPT | Homepage") was used to create recipes and the information about For Goodness Bakes.

#### Visual Content:

- [Contrast Grid](https://contrast-grid.eightshapes.com/?version=1.1.0&background-colors=&foreground-colors=%23FAF7F2%0D%0A%23E8B7C8%0D%0A%23C97A5D%0D%0A%23A8C3B1%0D%0A%232B2B2B&es-color-form__tile-size=regular&es-color-form__show-contrast=aaa&es-color-form__show-contrast=aa&es-color-form__show-contrast=aa18&es-color-form__show-contrast=dnp "Contrast Grid")
- [Coolors Scheme](https://coolors.co/ "Coolors Scheme Homepage")
- [Favicon](https://favicon.io/emoji-favicons/ "Favicon | Homepage")

[Back to contents](#contents)