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
        + [Success Messages](#success-messages)
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
    * [Error Page Testing](#error-page-testing)
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
* Ability for only authenticated users to comment on recipes, including editing and deleting their own comments successfully, with prior prompting before deletion and activity confirmation.
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

[Desktop header](docs/laptop-header.png "Desktop Header")

[Desktop header with hover effect](docs/laptop-header-hover.png "Desktop Header Hover Effect")

[Tablet header](docs/tablet-header.png "Tablet Header")

[Tablet header open](docs/tablet-header-open.png "Tablet Header Open")

[Mobile header](docs/mobile-header.jpg "Mobile Header")

[Mobile header open](docs/mobile-header-open.jpg "Mobile Header Open")

<br>

### Home Section

The home page displays a list of available recipes in a clean, visually appealing layout. 

Key features include:
- List of recipes displayed as cards
- Cards are responsive when hovered over on larger screens
- Responsive on different screen sizes
- 'next' and 'prev' page buttons at the bottom of the page with hover effect in burnt peach

Each recipe card includes:
- A featured image
- Recipe title
- Short description

On larger screens, when the user hovers over a recipe, the recipe card moves slightly to provide a better user experience. Users can click through to individual recipe pages for full details. 

<br>

[Desktop home view preview](docs/desktop-home-view.png "Desktop Home View Preview")

[Desktop home view with hover effect](docs/desktop-home-view-hover.png "Desktop Home View With Hover Effect")

[Tablet home view preview](docs/tablet-home-view.png "Tablet Home View Preview")

[Mobile home portrait view preview](docs/mobile-home-portrait-view.png "Mobile Home Portrait View Preview")

[Mobile home landscape view preview](docs/mobile-home-landscape-view.png "Mobile Home Landscape View Preview")

<br>

### Registration

New users can register for an account using a secure and intuitive form. There is a link to the log in page in case a user has incorrectly navigated to the registration page. The registration form gives validation feedback to users if they try to submit the form with an empty field that is required and offers password requirements. 

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

Registered users can log in securely using their credentials, there's the option to remember log in credentials for quicker access to For Goodness Bakes in the future, providing a better user experience. In case a new user has incorrectly navigated to the log in page when they do not currently have an account, there is a link to the register page. Clear confirmation messages are displayed on successful login and logout with a prompt before logging out that includes a red hover over effect on the 'Log Out' button, improving user confidence and clarity.

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
- A description about For Goodness Bakes that can be modified by administrators through Django Administration.
- Administrators can carry out CRUD functions through Django Administration.
- Time and date stamp of when the description was last updated.
- 'Get in touch' contact form
- Form 'Send' button has ash grey hover effect which is a green tone suggesting success.
- Form validation
- Success message

<br>

[About preview for desktop](docs/about-desktop.png "About | Desktop")

[About preview for tablet](docs/about-tablet.png "About | Tablet")

[About preview for mobile](docs/about-mobile.png "About | Mobile")

[About contact form](docs/about-contact-form.png "About | Contact Form")

[About contact form button hover effect](docs/about-contact-form-hover.png "About | Contact Form Button Hover Effect")

[About contact form validation](docs/about-contact-form-validation.png "About | Contact Form Validation")

[About - Django administration preview for desktop](docs/about-django-administration-desktop.png "About - Django Administration | Desktop")

<br>

### Recipe Detail

Each recipe has its own dedicated detail page, providing comprehensive information for users whilst maintaining the same relaxed theme the rest of the website carries. 

Key features include:
- Recipe Information: displays the title, a brief description, recipe author, date of publish, featured image, ingredients and  step-by-step method with key information such as oven temperature and cooking time in bold to help the user find it.
- Additional Details: Includes preparation time, cooking time, servings and recipe difficulty.
- Comment Integration: Comments related to the recipe are displayed below the content with a comment count, allowing users to interact directly.
- Comment buttons for logged in users are highlighted accordingly, 'Submit' with a success colour, 'Delete' with a danger colour and 'Edit' with the websites standard highlight colour of burnt peach. 
- A prompt to 'Log in to leave a comment' is visible for guest users who are not logged in.
- Responsive Layout: Content and images adapt seamlessly across mobile, tablet, and desktop devices.
- Navigation: Clear buttons and links allow users to return to the home page, about page, register/log in/out page or perform authenticated actions (commenting, editing).
- Accessibility: Semantic HTML and proper contrast ensure readability for all users.
- Administrators can carry out CRUD functions through Django Administration.

The recipe detail page combines visual appeal with clear structure to provide a smooth and engaging browsing experience.

<br>

[Recipe detail preview for desktop](docs/recipe-detail-desktop.png "Recipe Detail | Desktop")

[Recipe detail preview for tablet](docs/recipe-detail-tablet.png "Recipe Detail | Tablet")

[Recipe detail preview for mobile](docs/recipe-detail-mobile.png "Recipe Detail | Mobile")

[Recipe detail preview for mobile ](docs/recipe-detail-ingredients-and-method-mobile.png "Recipe Detail | Mobile Continued")

[Recipe detail form validation for desktop](docs/form-validation-desktop.png "Recipe Detail Form Validation | Desktop")

[Recipe detail comments section preview for desktop](docs/recipe-detail-comments-desktop.png "Recipe Detail Comments Section| Desktop")

[Recipe detail comments section preview for tablet](docs/recipe-detail-comments-tablet.png "Recipe Detail Comments Section| Tablet")

[Recipe detail comments section preview for mobile](docs/recipe-detail-comments-mobile.png "Recipe Detail Comments Section| Mobile")

[Recipe detail - Django administration preview for desktop](docs/recipe-django-administration-desktop.png "Recipe Detail - Django Administration | Desktop")

<br>

### Comment Section

Authenticated users can interact with recipes through a fully featured commenting system. 

Key features include:
- Create Comments: Users can add new comments to any recipe, sharing feedback, baking tips, or personal experiences.
- Edit Comments: Users can edit their own comments to correct errors or provide updates. Edited comments update immediately in the UI with an awaiting approval message.
- Delete Comments: Users can delete their own comments. A confirmation prompt ensures accidental deletions are avoided.
- Real-Time Feedback: Actions such as adding, editing, or deleting comments provide immediate visual confirmation with a success message, improving user experience.
- Access Control: Only authenticated users can create, edit, or delete comments. Users cannot modify comments posted by others.
- Moderation: Admin users have the option to authorise comments and can decline and delete inappropriate or irrelevant comments to maintain a positive community environment.
- When a user selects a message to edit, the message autofills the comment box to improve UX.

This system improves UX while maintaining content integrity and community standards.

[Recipe detail comments section submit button hover effect](docs/recipe-detail-comments-submit-hover-desktop.png "Recipe Detail Comments Section Submit Button Hover Effect | Desktop")

[Recipe detail comments section delete button hover effect](docs/recipe-detail-comments-delete-hover-desktop.png "Recipe Detail Comments Section Delete Button Hover Effect | Desktop")

[Recipe detail comments section edit autofill](docs/recipe-detail-comments-edit-autofill-desktop.png "Recipe Detail Comments Section Autofill | Desktop")

[Recipe detail comments section edit button hover effect](docs/recipe-detail-comments-edit-hover-desktop.png "Recipe Detail Comments Section Edit Button Hover Effect | Desktop")

[Recipe detail comments section logged in](docs/comment-section.png "Comment Section | Logged In")

[Recipe detail comments section logged out](docs/comment-section-logged-out.png "Comment Section | Logged Out")

[Recipe detail comments section awaiting approval](docs/comment-awaiting-approval.png "Comment Awaiting Approval")

[Recipe detail comments section update comment success](docs/update-comment-success.png "Update Comment Success")

[Recipe detail comments section delete comment confirmation](docs/delete-comment-confirmation.png "Delete Comment Confirmation")

[Recipe detail comments section delete comment success](docs/delete-comment-success.png "Delete Comment Success")

<br>

### Success Messages

Success messages are displayed following key user actions such as registration, login, or comment submission. These provide immediate visual confirmation that actions have been completed successfully.

[Login feedback message preview for desktop](docs/login-feedback.png "Login Feedback Message | Desktop")

[Login feedback message preview for tablet](docs/login-feedback-tablet.png "Login Feedback Message | Tablet")

[Login feedback message preview for mobile](docs/login-feedback-mobile.png "Login Feedback Message | Mobile")

[Logout feedback message preview](docs/logout-feedback.png "Logout Feedback Message")

[Comment success feedback message preview](docs/comment-success.png "Comment Success Message")

[Update comment success feedback message preview](docs/update-comment-success.png "Update comment Success Message")

[Delete comment success feedback message preview](docs/delete-comment-success.png "Delete comment Success Message")

<br>

### Error Pages

Custom 400, 403, 404 and 500 error pages are included to handle broken or invalid URLs which improves UX. The error page clearly informs users that the requested content cannot be found and provides a link back to the homepage. These were manually tested during development.

[400 error page preview](docs/400.png "400 Error Page")

[403 error page preview](docs/403.png "403 Error Page")

[404 error page preview](docs/404.png "404 Error Page")

[500 error page preview](docs/500.png "500 Error Page")

<br>

### Footer

The footer contains:
- Copyright information
- Social media links that open in a new tab
- Consistent branding

It offers a clear and simple display making it easy to read without drawing attention away from the main website and remains accessible across all pages and screen sizes.

[Footer preview for desktop](docs/footer-desktop.png "Footer | Desktop")

[Footer preview for tablet](docs/footer-tablet.png "Footer | Tablet")

[Footer preview for mobile](docs/footer-mobile.png "Footer | Mobile")

<br>

### Django Admin Panel

Administrators have access to a secure, feature-rich admin panel to manage the website and community content:

- Recipe Management: Admins can create, edit, and delete recipes, ensuring content remains accurate and up-to-date.
- Summernote Editing: Summernote is integrated into the admin panel to allow rich text editing for recipe instructions and descriptions. Admins can:
  - Format text (bold, italics, headings)
  - Add lists, links, and images
  - Easily structure content for better readability
  This ensures recipes are visually appealing and easy to follow for all users.
- Comment Moderation: Admins can view, edit, and delete user comments, accepting, declining and removing inappropriate or spam content.
- User Management: Admins can manage user accounts, including editing user details and assigning admin privileges.
- Secure Access: Admin access is restricted to superusers with Django’s authentication system, preventing unauthorized access.
- UI Feedback: Admin actions provide immediate confirmation messages to ensure administrators are aware of successful updates or deletions.
- Database Control: All changes made in the admin panel directly update the database while maintaining data integrity and security.
- User passwords are always stored securely using a hashing algorithm to offer high levels of protection.

This panel ensures that the platform remains safe, well-maintained, and engaging for all users.

[Django administration login preview](docs/django-administration-login.png "Django Administration | Login")

[Django administration site administration preview](docs/django-administration-site-administration.png "Django Administration | Site Administration")

[Django administration abouts preview](docs/django-administration-abouts.png "Django Administration | Abouts")

[Django administration change abouts preview](docs/django-administration-change-abouts.png "Django Administration | Change Abouts")

[Django administration recipe preview](docs/django-administration-recipe.png "Django Administration | Recipe")

[Django administration change recipe 1/3 preview](docs/django-administration-change-recipe-one.png "Django Administration | Change Recipe 1/3")

[Django administration change recipe 2/3 preview](docs/django-administration-change-recipe-two.png "Django Administration | Change Recipe 2/3")

[Django administration change recipe 3/3 preview](docs/django-administration-change-recipe-three.png "Django Administration | Change Recipe 3/3")

[Django administration users preview](docs/django-administration-users.png "Django Administration | Users")

[Django administration password preview](docs/django-administration-password.png "Django Administration | Passwords")

[Django administration comments preview](docs/django-administration-comments.png "Django Administration | Comments")

[Django administration change comments preview](docs/django-administration-change-comment.png "Django Administration | Change Comments")

[Django administration add user success message preview](docs/django-administration-add-user-success.png "Django Administration | Add User Success Message")

<br>

## Future Enhancements

Potential future features include:
- Recipe search and filtering functionality
- User profiles
- Ability to save favourite recipes
- Expanded community interaction features
- Rating system for recipes
- Dark mode
- Character limit for comments
- Update language to ensure consistency 

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

- [Bootstrap v5.3.8](https://getbootstrap.com/ "Bootstrap v5.3 Homepage")
- [Django](https://www.djangoproject.com/ "Django Homepage")
- [Favicon](https://favicon.io/ "Favicon Homepage")
- [Font Awesome](https://fontawesome.com/search?q=menu&o=r&ic=free "Font Awesome Homepage")
- [Google Fonts](https://fonts.google.com/ "Google Fonts Homepage")

## Tools and Programmes

- [Black](https://pypi.org/project/black/ "Black | Code Formatter")
- [Contrast Grid](https://contrast-grid.eightshapes.com/?version=1.1.0&background-colors=&foreground-colors=%23FAF7F2%0D%0A%23E8B7C8%0D%0A%23C97A5D%0D%0A%23A8C3B1%0D%0A%232B2B2B&es-color-form__tile-size=regular&es-color-form__show-contrast=aaa&es-color-form__show-contrast=aa&es-color-form__show-contrast=aa18&es-color-form__show-contrast=dnp "Contrast Grid")
- [Coolors](http://https://coolors.co/ "Coolors")
- [Digital Colour Meter](https://support.apple.com/en-gb/guide/digital-color-meter/welcome/mac "Apple | Digital Colour Meter")
- [Draw.io](https://www.drawio.com/ "Draw.io Homepage")
- [GitHub](https://github.com "GitHub Homepage")
- [Heroku](https://www.heroku.com/ "Heroku")
- [HTML Color Codes](https://htmlcolorcodes.com/ "HTML Color Codes | Homepage")
- [JSHint](https://jshint.com/ "JSHint | Homepage")
- [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode "Prettier | Code Formatter")
- [VS Code](https://code.visualstudio.com/ "VS Code Homepage")
- [WAVE](https://wave.webaim.org/report#/https://for-goodness-bakes-app-93b97c50dd02.herokuapp.com/ "WAVE | Homepage")
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/ "W3C CSS Validation Service Homepage")
- [W3C HTML Validation Service](https://validator.w3.org/ "W3C HTML Validation Service Homepage")

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
|Server Error occurring only on Heroku deployment.|Yes|Add Cloudinary_URL to config vars on Heroku.|
|Comment form not submitting on button click|Yes|Amend typo from comment-on to comment_on|
|Logged in users unable to see comments awaiting moderation.|Yes|Amend comment filtering from approved=true to all.|
|Blue outline around social links|Yes|Update CSS to remove text decoration.|
|When a comment is edited, the original unedited comment remains and a new edited version is posted.|Yes|Update Javascript in comments.js to check for hidden input of comment_id of post being edited and set value to the comment's id from the database. This prevents duplicate comments being made when edits are completed.|
|Error page button styling not taking effect.|Yes|Set Debug to True to view styling. Once completed, update static files and reset Debug to False.|

## Responsiveness Tests

Manual testing was conducted across multiple devices and screen sizes both on actual devices and through [Dev Tools](https://developer.chrome.com/docs/devtools "Chrome | Dev Tools") to ensure layout consistency and usability. No significant layout issues were identified.

## Code Validation

### HTML

[W3C HTML Validator](https://validator.w3.org/ "W3C HTML Validator | Home") was used to check all of the HTML on the For Goodness Bakes website with no errors or warnings found.

[W3C HTML Validator - home page results](docs/html-checker-home.png "W3C HTML Validator | Home Page Results")

[W3C HTML Validator - recipe detail page results](docs/html-checker-recipe-detail.png "W3C HTML Validator | Recipe Detail Page Results")

[W3C HTML Validator - about page results](docs/html-checker-home.png "W3C HTML Validator | About Page Results")

[W3C HTML Validator - register page results](docs/html-checker-signup.png "W3C HTML Validator | Register Page Results")

[W3C HTML Validator - login page results](docs/html-checker-login.png "W3C HTML Validator | Login Page Results")

[W3C HTML Validator - logout page results](docs/html-checker-logout.png "W3C HTML Validator | Logout Page Results")

### CSS

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/ "W3C CSS Validator | Home") was used to validate the CSS on the For Goodness Bakes website with no errors found.

[W3C CSS Validator results](docs/css-validator.png "W3C CSS Validator")

### JavaScript

[JSHint](https://jshint.com/ "JSHint | Homepage") was used to analyse the JavaScript used in the For Goodness Bakes website, no errors were found.

[JSHint Analyse results](docs/jshint-analyse.png "JSHint Analyse Results")

### Python

Python code was tested through manual testing, Django error reporting and by running the python code through [Code Institute's](https://pep8ci.herokuapp.com/ "Code Institute | CI Python Linter") Python Linter. The application runs without errors in production, and all core functionality behaves as expected. CI's Python Linter returned no errors on all python code, the key tests can be found below:

[CI Python Linter test for recipe.views.py](docs/python-testing-recipes-views-py.png "CI Python Linter | recipe.views.py")

[CI Python Linter test for about.views.py](docs/python-testing-about-views-py.png "CI Python Linter | about.views.py")

[CI Python Linter test for for_goodness_bakes-settings.py](docs/python-testing-for-goodness-bakes-settings-py.png "CI Python Linter | or_goodness_bakes-settings.py")

[CI Python Linter test for recipe.admin.py](docs/python-testing-recipes-admin-py.png "CI Python Linter | recipe.admin.py")

[CI Python Linter test for recipe.forms.py](docs/python-testing-recipes-forms-py.png "CI Python Linter | recipe.forms.py")

[CI Python Linter test for recipe.models.py](docs/python-testing-recipes-models-py.png "CI Python Linter | recipe.models.py")

[CI Python Linter test for about.forms.py](docs/python-testing-about-forms-py.png "CI Python Linter | about.forms.py")

[CI Python Linter test for about.models.py](docs/python-testing-about-models-py.png "CI Python Linter | about.models.py")

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

## Error Page Testing

The error pages can be viewed by:
- **400**: In recipes.views.py import 'BadRequest' from Django.core.exceptions then define the function for testing 400.
```
def test_400(request): 
    raise BadRequest
```
In recipes.urls.py add a new path at the top of urlpatterns to connect to the new view.
```
urlpatterns = [
    path("tests-400/", views.test_400),
]
```
Run the local server and then navigate to the [local deployment](http://127.0.0.1:8000)/test-400/ to view the error page. Once viewing of the error page is complete, remove all code edits to prevent users accessing the 400 error page mistakenly.
<br>
- **403**:  In recipes.views.py import 'PermissionsDenied' from Django.core.exceptions then define the function for testing 403.
```
def test_403(request):
    raise PermissionDenied
```
In recipes.urls.py add a new path at the top of urlpatterns to connect to the new view.
```
urlpatterns = [
    path("tests-403/", views.test_403),
  ]
```
In settings.py, set
<br>
`DEBUG = False`
<br>
Run the local server and then navigate to the [local deployment](http://127.0.0.1:8000/)/test-403 to view the error page. Once viewing of the error page is complete, remove all code edits to prevent users accessing the 403 error page mistakenly.
<br>
- **404**: - Visit the website at: 
<br>
https://for-goodness-bakes-app-93b97c50dd02.herokuapp.com/incorrectlink 
<br>
The path does not need to be 'incorreclink', it needs to be something other than a valid path. Once done, the error page should be displayed.
<br>
- **500**: - In recipes.index.html, prevent the block content code from running correctly, for example
<br>
`{% block content}`
<br>
Run the local server and the error page should be displayed.

[400 and 403 error page test code - views.py](docs/recipes-views-code.png "400 and 403 Error Page Test Code | views.py")

[400 and 403 error page test code - urls.py](docs/recipes-urls-code.png "400 and 403 Error Page Test Code | urls.py")

[404 error page - incorrect link](docs/incorrect-link.png "404 Error Page Test Code | Incorrect link")

[500 error page test code - index.html](docs/recipes-index-code.png "500 Error Page Test Code | index.html")

## Accessibility Testing

Accessibility best practices were followed, including:
- Sufficient colour contrast
- Semantic HTML
- Clear navigation structure

Contrast Grid and Lighthouse tools were used to support accessibility testing.

[WAVE](https://wave.webaim.org/report#/https://for-goodness-bakes-app-93b97c50dd02.herokuapp.com/ "WAVE | Homepage") was used to evaluate the accessibility of the website, no errors were found across the site. Some contrast errors were found on the Register and Log In pages due to the links between each other, the standard blue hyperlinks were used to make it clear to users that the link were active. 

[WAVE accessibility evaluation for the home page](docs/wave-home.png "WAVE | Home Page")

[WAVE accessibility evaluation for the recipe detail page](docs/wave-recipe-detail.png "WAVE | Recipe Detail Page")

[WAVE accessibility evaluation for the about page](docs/wave-about.png "WAVE | About Page")

[WAVE accessibility evaluation for the register page](docs/wave-register.png "WAVE | Register Page")

[WAVE accessibility evaluation for the log in page](docs/wave-log-in.png "WAVE | Log In Page")

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
- Create a **'requirements.txt'** file to list all of the dependencies required by your project. This can be done by running **'pip3 install -r requirements.txt'** in the terminal, it can then be updated to include any other packages installed by running **'pip3 freeze --local > requirements.txt'** in the terminal.
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
- [Django Projects | Django Exceptions](https://docs.djangoproject.com/en/6.0/ref/exceptions/ "Django Projects | Django Exceptions")
- [Django Projects | Request and Response Objects](https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.HttpResponseBadRequesthttps://docs.djangoproject.com/en/dev/ref/request-response/#django.http.HttpResponseBadRequest "Django Projects | Request and Response Objects")
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