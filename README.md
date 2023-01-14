![Banner Image](readme/AmIResponsive.png)
## Live Link
[https://fergalcob.github.io/CiNAMEa/](https://fergalcob.github.io/CiNAMEa/)

## Table of Contents
 - [Site Inspiration](#site-inspiration)
 - [User Stories](#user-stories)
   * [First Time User](#first-time-user)
 - [Features](#features)
   * [Header Section](#header-section)
   * [Answer Field & Answer Results](#answer-field--answer-results)
   * [Archive Buttons](#archive-buttons)
   * [Daily Puzzle & Hint Section](#daily-puzzle--hint-section)
   * [Progression](#progression)
   * [Future Plans](#future-plans)
- [Styling Choices](#styling-choices)
   * [Color Palette](#color-palette)
   * [Typography](#typography)
   * [Favicon](#favicon)
- [Device Testing Results & Known Issues](#device-testing-results--known-issues)
   * [Devices & Browsers Used For Testing](#devices--browsers-used-for-testing)
   * [W3C Validator & Lighthouse Testing](#w3c-validator--lighthouse-testing)
   * [Jigsaw Validation Of CSS](#jigsaw-validation-of-css)
   * [JSHint Validation Of Javascript](#jshint-validation-of-javascript)
   * [Bugs](#bugs)
     - [Solved Issues](#solved-issues)
- [Deployment](#deployment)
  * [Github Pages](#github-pages)
- [Technologies Used](#technologies-used)
- [Credits](#credits)
  * [Code](#code)
 
 
## Site Inspiration

The inspiration for this site came from the recent trend of daily puzzle games beginning with [Wordle](https://www.nytimes.com/games/wordle/index.html) and continuing into more trivia based options such as [Heardle](https://www.spotify.com/heardle/?), [Framed](https://framed.wtf/) and [GuessThe.Game](https://guessthe.game/) among others. These sites all follow the same general set-up of a daily, 6 guesses puzzle. CiNAMEa takes from these and creates a daily puzzle wherein the user is shown a portion of a movie poster with the title removed and based on their guesses are shown additional portions of the image or are provided hints to the film's identity.

## User Stories

### First Time User

 1. As a first time user, I want to be able to easily understand the goal of the site
 2. As a first time user, I want to clearly understand how to interact with the site's content
 3. As a first time user, I want to be able to access previous content on the site used for prior puzzles

### Returning User

 1. As a returning user, I would like to be find new content on a daily basis
 2. As a returning user, I would like to have easy access to content I may have missed if I have not accessed the site for some time

## Features 

### Index.html features

#### Header Section

What we have in the banner for the site includes the CiNAMEa title which we discuss the intentions regarding in the typography section. We also have our help icon located in the header which allows users easy access to the help overlay should they need any guidance as to how to interact with the site on their initial visit. Finally, this section is bordered above and below by a filmstrip-like image incorporating the theme and focus of the site. 

| Laptop/Desktop Banner |
| --- |
| ![Desktop Banner](readme/desktop-banner.png) |

| Mobile Banner |
| --- |
| ![Mobile Banner](readme/mobile-banner.png) |

#### Answer Field & Answer Results
| Answer Submission Field |
| --- |
| ![Answer Field](readme/form-field.png) |

The first thing a user will see after the banner is the text submission field where they can provide the answer to the current puzzle. The field's initial placeholder text is used to provide that information quickly and easily to a new user with the help option being available if they need any other guidance.
Below this field are the six boxes used to show the status of the day's puzzle which will change colour as the user uses up their daily guess count.

| Suggestion Dropdown |
| --- |
| ![Suggestion List](readme/suggestions.png) |

Upon entering any text in the answer field, the user will be presented with a list of titles that match the input they have provided thus far, with additional text narrowing down their choices available. Users can select from this list to autopopulate the answer field or can continue to type their answer freely with the answer check being case insensitive.

| Results Content |
| --- |
| ![Answer Results](readme/results.png)|

Upon either guessing the answer correctly or using all six guesses incorrectly, the answer submission field will then be replaced by the results content which will let users know if they have guessed successfully or unsuccessfully. This also includes a countdown timer to let them know when the next puzzle will be available to answer.

#### Archive Buttons

| Archive Buttons(Desktop) | Archive Buttons(Mobile) |
| --- | --- |
| ![Archive Buttons - Desktop](readme/archive-desktop.png)| ![Archive Buttons - Mobile](readme/archive-mobile.png)

Once a user has completed the day's puzzle either successfully or unsuccessfully, they'll be given the option to view the archives allowing them access to all previous puzzles. By clicking on this option, the archives will be generated up until the current date and once clicked, any button will load that particular puzzle and reset the page to allow them to continue. As you can see, due to the flex nature of the buttons, we reduce the number shown per row on mobile as compared to larger devices in order to allow ease of access to the buttons.

#### Daily Puzzle & Hint Section

The structure of the puzzle itself is then based on the device in question, to avoid the need to reduce the image size on mobile devices, the puzzle and hint section are set to a single-column display with the hints being displayed below the image allowing the image to use the full width of the device as the puzzle progresses. When we move to higher resolution displays, this single-column display then reverts to a dual-column layout with the image taking up the left half of the page and the hints on the right.

| Puzzle & Hints(Desktop) | Puzzle & Hints(Mobile) |
| --- | --- |
| ![Puzzle & Hints - Desktop](readme/puzzle-desktop.png)| ![Puzzle & Hints - Mobile](readme/puzzle-mobile.png)

#### Progression

When a user accesses the site for the first time in a day, the hint section will be empty and there will be a small snippet of the daily image available to view. If they guess correctly or guess incorrectly 6 times, the full image will then be displayed. Otherwise, as the user guesses incorrectly prior to the results being displayed, an additional hint will be provided or more of the image will be revealed as the guesses continue.

| Daily Puzzle(0 Guesses) | Daily Puzzle(3 Guesses) | Daily Puzzle(All Guesses)
| --- | --- | --- |
| ![Daily Puzzle - 0](readme/puzzle0.png) | ![Daily Puzzle - 3](readme/puzzle3.png) | ![Daily Puzzle - All](readme/puzzle6.png) |

| Hint List(0 Guesses) | Hint List(3 Guesses) | Hint List(All Guesses)
| --- | --- | --- |
| ![Hint List - 0](readme/hints0.png) | ![Hint List - 3](readme/hints3.png) | ![Hint List - All](readme/hints6.png) |


### Future Plans

* To implement content on a continuous basis, with the current project there is a fixed number of puzzles available, with continuous content updates this would remove the current need to loop back on previously used puzzles and also reduce the code load as there would be no need for looping
* To implement archive retention, currently when the archive is accessed the guesses are not retained locally when accessing the site, ideally each puzzle would store it's own unique values for guesses attempted allowing users to see how they performed on previous days

## Styling Choices

### Color Palette
![Color Palette](readme/palette.png)

In keeping with other sites in the same genre, the site itself uses a very simple and focused colour palette as the eye should be drawn to the puzzle as the main intention of the site. Using a spread of dark to light grays to keep a general theme in place without any contrast issues

The red(#D30000),green(#3BB143) and grey(#666666) shades are used for the guess boxes to denote unused/incorrect and correct guesses, these choices are due to their ease of understanding by users from their common usage with the red for incorrect, green for correct and grey for unanswered.

### Typography

Nixie One:  
![Nixie One](readme/nixie_one.png)  
Movie Times:  
![Movie Times](readme/movie_times.png)  
Due Credit:  
![Due Credit](readme/due_credit.png)  

For the font choices for the site, we have three primary options, Nixie One, Movie Times & Due Credit which can all be seen above. These choices were to keep in the theme of and to suggest the imagery of movies. With Movie Times being used for the logo title, the font itself with the film strip borders gives an clear initial idea as to what the site itself would be regarding but it was a choice to use this font sparingly due to the large filmstrip borders.

Nixie One and Due Credit are then used for the main content of the page, with Due Credit evoking the text from movie poster credits and being used for the hint and answer titles. Nixie One then being used for the text content such as the hints/answers and the overlay's help text, similarly to Due Credit, this was chosen due to being a typeface similar to typewriter script as would be seen commonly in movies. 

### Favicon

![CiNAMEa Favicon](readme/cinamea-icon.png)

The favicon was personally created the site, reusing the filmstrip imagery from the banner border enclosing a question mark symbol to represent the two primary aspects of the site, movies and puzzles.

## Device Testing Results & Known Issues

### Devices & Browsers Used For Testing

1. Laptop(Acer Nitro 5 & Lenovo Ideapad 5)
    * Chrome
    * Edge
    * Firefox

2. Android Phone(Realme 9 Pro & Samsung S21)
    * Chrome
    * Firefox

3. Android Tablet(Lenovo Tab)
    * Chrome

### W3C Validator & Lighthouse Testing

<details>
  <summary>index.html results - Validator and Lighthouse</summary>
  
  #### W3C Validator Results
  ![Testing Results - contact.html](readme/w3c-html-validation.png)
  
  #### Lighthouse Results - Desktop
  ![Testing Results - contact.html](readme/lighthouse-desktop.png)
  
  #### Lighthouse Results - Mobile
  ![Testing Results - contact.html](readme/lighthouse-mobile.png)
</details>

</details>

### Jigsaw Validation Of CSS
![Testing Results - CSS](readme/w3c-css-validation-test.png)

### JSHint Validation Of Javascript
![Testing Results - JS](readme/jshint-test-results.png)

### Bugs

#### Solved Issues

1. Initially the Google Geocoding API was being used to convert the location provided by the user, however when testing with certain non-specific locations(i.e. Cork, Bray), no result was being found. In place of the Geocoding API the Google Places API was used in its place which remedied the issue.

## Deployment

### Github Pages

1. To deploy the live site, from the Github directory for the project, access the Settings page(indicated by the cog icon) from the navbar.
2. Once in the Settings page, access the Pages subsection from the menu on the left under 'Code and Automation'.
3. From here, you want to choose the source for the site, in this case 'Deploy from branch' is used as the source, followed by choosing the branch, in this case it's 'Main' and '/root'
4. All that needs to be done from there is to save those settings and allow 5-10 minutes for deployment to complete.
5. At that point, the page was then live at [https://fergalcob.github.io/Mail-Matters/](https://fergalcob.github.io/Mail-Matters/)

## Technologies Used
* [HTML5](https://en.wikipedia.org/wiki/HTML5)
   - Used to build the underlying structure of the website and to add the content for users
* [CSS](https://en.wikipedia.org/wiki/CSS)
   - Used to provide the styling necessary to set the final layout of the site and to implement responsiveness across device types
* [GIMP](https://www.gimp.org/) 
   - Used for scaling the banner images for responsiveness
* [Am I Responsive](https://ui.dev/amiresponsive) 
   - For testing and creating the Readme banner image
* [Coolors](https://coolors.co)
  - Used to create the color palette shown in the Readme
* [jQuery](https://jquery.com/)
  - Used to reload the text input field after selecting a puzzle from the Archives
* [Favicon.io](https://favicon.io/)
  - Used for generating the favicon set and code from the personally  created icon

## Credits
### Code

The OWmanager_historical class found in the historical_data.py file is based on the OWmanager class found in the openmeteopy library. The current version of this library does not currently support querying OpenMeteo's Historical Weather API and so this class needed to be updated in order to query the Historical API endpoint. Additional parameters(Start Dates & End Dates) needed to be passed to the historical class and so additional testing needed to be added to this class also to ensure that the new data provided returned a valid query.





Welcome USER_NAME,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!
