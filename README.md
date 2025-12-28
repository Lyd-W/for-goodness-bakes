# For Goodness Bakes

[For Goodness Bakes]( "For Goodness Bakes | Heroku")

A full stack Django web application where users can browse recipes and, once logged in, create, edit, and delete comments on recipes. For Goodness Bakes is a relaxed and friendly community for bakers of all levels to come together for interaction and support from similar minded individuals. The platform focuses on clean UX, accessibility, secure authentication, and robust CRUD functionality.

![For Goodness Bakes](docs/homepage.png)

### [Contents](#contents)
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
* [Features](#features)
    * [Existing Features](#existing-features)
        + [Header](#header)
        + [Home Section](#home-section)
        + [Registration](#registration)
        + [Login Section](#login-section)
        + [About Section](#about-section)
        + [Success Page](#success-page)
        + [404 Error Page](#404-error-page)
        + [Footer](#footer)
    * [Future Enhancements](#future-enhancements)
* [Technologies Used](#technologies-used)
    * [Languages](#languages)
    * [Libraries and Frameworks](#libraries-and-frameworks)
    * [Tools and Programmes](#tools-and-programmes)
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

These user stories have been prioritied using the MoSCoW Prioritisation method. GitHub Project Board was then used to manage workflow and track progress towards completion of each story and ensuring all required elements of the user stories were met.

![GitHub Project Board](docs/github-project-board.png)

[Back to contents](#contents)

## User Feedback

User feedback will go here.

[Back to contents](#contents)

## Website Goals

The key website goals are to provide users with a safe community to browse recipe ideas and, when authenticated, engage with the community through posting, editing and deleting their own comments. Administrators will provide this safe community through their abilitiy to moderate user comments and add or amend recipe information. 

[Back to contents](#contents)

## Website Objectives

* To provide clearly structured and visually appealing recipe content for public users, authenticated users and admin, ensuring information is easy to find, read and navigate across different devices.
* To provide intuitive navigation onto individual recipe pages from the recipe listing page, keeping the layout consistent with clear information and easily accessible navigation controls.
* Enable secure registration for new users, with clear UI confirmation.
* Enable secure log in/out for existing users, with clear UI confirmation.
* Ability for only authenticated users to comment on recipes, including editing and deleting thier own comments successfully, with prior prompting before deletion and activity confirmation.
* All sensitive user and site data is suitably protected, following best practiuce for secure data handling.
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

The wireframes were designed using templates from [Balsamiq](https://balsamiq.com/ "Balsamiq Homepage"). A mobile first approach was taken throughout.

[Mobile Wireframes](docs/mobile-wireframes.pdf "Mobile Wireframes")

[Tablet Wireframes](docs/tablet-wireframes.pdf "Tablet Wireframes")

[Desktop Wireframes](docs/desktop-wireframes.pdf "Laptop Wireframes")

[Back to contents](#contents)

## Design Choices

### Typography

The primary font family that was chosen for For Goodness Bakes was [Playfair Display](https://fonts.google.com/specimen/Playfair+Display?query=playfair+display "Google Fonts | Playfair Display"), the soft curves of the serif style offers a warm and personal feeling to welcome users into the website. Playfair Display offers a familiar magazine feeling, helping users to feel comfortable and invited to interact with the recipes and other users. This font was used for recipe titles and headings.

The secondary font family that was chosen for For Goodness Bakes was [Lato](https://fonts.google.com/specimen/Lato "Google Fonts | Lato") due to its readability through its clean letter design and professional yet friendly appearance while remaining neutral enough to not compete with the headings. Lato offers legibility for longer bodies of text making it ideal for recipe descriptions, ingredient lists, instructions and comments.

Together, these font groups help to create visual balance, offering warmth and an easy reading experience. The use of a serif font for headings and a sans-serif font for body text also provides easy visual distinction for users.

### Colour Scheme

To visualise different colours together [Coolors Scheme](https://coolors.co/ "Coolors Scheme Homepage") was used to create a fitting combination for the website. Graphite was chosen for the font colour for the feeling of professionalism and ease of legibility whilst being easier on the eyes which was ideal for body text, headings and icons. Parchment was used to create a calmer, welcoming approach. This creates the feeling of reading from paper, suggesting cookbook pages, giving a better UX, therefore this colour was ideal for the website background. Soft Blossom was used to bring in a comforting, feminine touch whilst not being too overpowering, and was used for buttons, links and navigation. To reinforce the calm atmosphere the website aimed for, Ash Grey was selected, this helped to bring a natural, healthier balance to the Soft Blossom because greens are often associated with food and wellness. The final colour used was Burnt Peach, being a similar colour to spices it felt a natural choice for a baking website, bringing a sharp enphasis among the other colours making it ideal for buttons such as submitting,  commenting or hovers and borders.

![Coolors Scheme](docs/coolors.png)

[Contrast Grid](https://contrast-grid.eightshapes.com/?version=1.1.0&background-colors=&foreground-colors=%23FAF7F2%0D%0A%23E8B7C8%0D%0A%23C97A5D%0D%0A%23A8C3B1%0D%0A%232B2B2B&es-color-form__tile-size=regular&es-color-form__show-contrast=aaa&es-color-form__show-contrast=aa&es-color-form__show-contrast=aa18&es-color-form__show-contrast=dnp "Contrast Grid") was used to determine the best colour combinations to ensure the website was visually appealing whilst remaining easy for the user to read the content.

![Contrast Grid](docs/contrast-grid.png)

|CSS Name               |HEX          |Use
|-----------------------|-------------|------------------------------------------------|
| --primary | #FAF7F2 | Website background colour |
| --secondary | #E8B7C8 | Buttons, links, navigation  |
| --primary-highlight | #C97A5D | Button hover and borders, submission button |
| --secondary-highlight | #A8C3B1 | Secondary buttons, success messages |
| --text | #2B2B2B | Primary text colour |

### Images

Image information to be added here.

### Responsiveness

Responsivness information to be added here.

[Back to contents](#contents)

# Features

Features information to be added here.

## Existing Features

### Header

Header information to be added here.

<b>Mobile header</b>

<b>Tablet header</b>

<b>Desktop header</b>

### Home Section

Home section information to be added here.

<br>

### Registration

Registration information to be added here.

<br>

### Login Section

Login section information to be added here.

<br>

### About Section

About section information to be added here.

<br>

### Success Page

Success page information to be added here.

<br>

### 404 Error Page

Error page information to be added here.

<br>

### Footer

Footer information to be added here.

## Future Enhancements

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

- [Balsamiq](https://balsamiq.com/ "Balsamiq Homepage")
- [Contrast Grid](https://contrast-grid.eightshapes.com/?version=1.1.0&background-colors=&foreground-colors=%23FAF7F2%0D%0A%23E8B7C8%0D%0A%23C97A5D%0D%0A%23A8C3B1%0D%0A%232B2B2B&es-color-form__tile-size=regular&es-color-form__show-contrast=aaa&es-color-form__show-contrast=aa&es-color-form__show-contrast=aa18&es-color-form__show-contrast=dnp "Contrast Grid")
- [Coolors](http://https://coolors.co/ "Coolors")
- [GitHub](https://github.com "GitHub Homepage")
- [Heroku](https://www.heroku.com/ "Heroku")
- [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode "Prettier - Code Formatter")
- [VS Code](https://code.visualstudio.com/ "VS Code Homepage")
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input "W3C CSS Validation Service Homepage")
- [W3C HTML Validation Service](https://validator.w3.org/#validate_by_uri "W3C HTML Validation Service Homepage")

[Back to contents](#contents)

# Testing

## Bugs

|   Bug Description                         | Resolved |    Resolution Description                               |
|-------------------------------------------|----------|---------------------------------------------------------|

## Responsiveness Tests

Responsiveness tests information to be added here.

## Code Validation

### HTML

HTML information to be added here.

### CSS

CSS information to be added here.

### JavaScript

JavaScript information to be added here.

### Python

Python information to be added here.

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

Feature testing information to be added here.

## Accessibility Testing

Accessibility testing information to be added here.

## Lighthouse Testing

Lighthouse testing information to be added here.

## Browser Testing

Browser testing information to be added here.

[Back to contents](#contents)

# Deployment

Deployment information to be added here.

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

- [Favicon.io](https://favicon.io "Favicon.io")

#### Visual Content:

- [Contrast Grid](https://contrast-grid.eightshapes.com/?version=1.1.0&background-colors=&foreground-colors=%23FAF7F2%0D%0A%23E8B7C8%0D%0A%23C97A5D%0D%0A%23A8C3B1%0D%0A%232B2B2B&es-color-form__tile-size=regular&es-color-form__show-contrast=aaa&es-color-form__show-contrast=aa&es-color-form__show-contrast=aa18&es-color-form__show-contrast=dnp "Contrast Grid")
- [Coolors Scheme](https://coolors.co/ "Coolors Scheme Homepage")

[Back to contents](#contents)