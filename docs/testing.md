# Testing

This is the TESTING file for the [Project](#) website.

Return back to the [README.md](#) file.

## Testing Contents  
  
- [Testing](#testing)
  - [Testing Contents](#testing-contents)
  - [Validation](#validation)
    - [HTML Validation](#html-validation)
    - [JavaScript Validation](#javascript-validation)
    - [Python Validation](#python-validation)
    - [CSS Validation](#css-validation)
    - [Lighthouse Scores](#lighthouse-scores)
    - [Wave Accessibility Evaluation](#wave-accessibility-evaluation)
  - [Manual Testing](#manual-testing)
    - [User Input/Form Validation](#user-inputform-validation)
    - [Browser Compatibility](#browser-compatibility)
    - [Testing User Stories](#testing-user-stories)
    - [Dev Tools/Real World Device Testing](#dev-toolsreal-world-device-testing)
  - [Bugs](#bugs)
    - [Known Bugs](#known-bugs)

<p align="right"><a href="#">🔺 Back To Top</a></p>
<hr>

## Validation

### HTML Validation

For my HTML files I have used [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

I have had to follow a different approach for validating my HTML for this project as the majority of my pages are developed using Jinja syntax such as '{% extends "base.html" %}' and '{{ form|crispy }}' and most require user authentication. The HTML validator will throw errors if I were to use my website's URL so I have had to follow the below approach for every page:

- Via the deployed Heroku app link, I have navigated to each individual page.
- Right clicking on the screen/CTRL+U/⌘+U on Mac, allows a menu to appear, giving me the option to 'View page source'.
- The complete HTML code for the deployed page will appear, allowing you to select the entire code using CTRL+A/⌘+A on Mac.
- Paste the copied code into the [validate by input](https://validator.w3.org/#validate_by_input) option.
- Check for errors and warnings, fix any issues, revalidate by following the above steps and record the results.

![html validation](#)  

All HTML pages were validated and received a 'No errors or warning to show' result as shown above.

Initially my Profile and Article Page HTML were receiving [validator errors](#), [error code generated from Summernote code](#) of having an extra p tag due to Summernotes rendering. I fixed this issue by replacing the p tags with divs, redeployed and checked for any styling issues. All clear on re-validation thankfully.


| HTML Source Code/Page | Errors | Warnings |
| ---- | ------ | -------- | 
| Home | 0 | 0 |
| Sign In | 0 | 0 |
| Sign Up | 0 | 0 |
| Profile | 0 | 0 |
| Edit Profile Modal | 0 | 0 |
| Articles | 0 | 0 |
| Add Article | 0 | 0 |
| View Article | 0 | 0 |
| Edit Article | 0 | 0 |
| Delete Article | 0 | 0 |
| Delete Comment | 0 | 0 |
| Booking | 0 | 0 |
| Create Booking | 0 | 0 |
| Edit Booking | 0 | 0 |
| Delete Booking| 0 | 0 |
| Gallery | 0 | 0 |
| Add Photo | 0 | 0 |
| Delete Photo Modal | 0 | 0 |
| Visit Us | 0 | 0 |
| Forgot Password | 0 | 0 |
| Error 403 | 0 | 0 |
| Error 404 | 0 | 0 |
| Error 500 | 0  | 0 |
  
<p align="right"><a href="#">🔺 Back To Top</a></p>
<hr>

### JavaScript Validation

[JSHint](https://jshint.com/) was used to validate the small amount of JavaScript code added to the project. External JS, for Bootstrap purposes, obtained via [CDN](https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.2.3/js/bootstrap.min.js) was not validated through JSHint

| Page | Screenshot | Errors | Warnings |
| ---- | ---------- | ------ | -------- |
| base.html | ![js from base.html](documentation/testing/base_js.png) | none | none |
| gallery.html | ![js from gallery.html](documentation/testing/gallery_js.png) | none | none |
| profile.html | ![js from profile.html](documentation/testing/profile_js.png) | none | none |

<p align="right"><a href="#">🔺 Back To Top</a></p>
<hr>

### Python Validation

Python validation was performed using [CI Python Linter](https://pep8ci.herokuapp.com/#) 

All errors were rectified with the exception of a single overlength line in settings.py\
This was confirmed as ok as part of settings.py files by cohort learning facilitator.

| Feature | admin | apps | asgi | forms | models | settings | urls | views | wsgi |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
| Config | N/A | N/A | No Errors | N/A | N/A | E501 - Ovelength | No Errors | N/A | No Errors |
| Landing | N/A | No Errors | N/A | N/A | N/A | N/A | No Errors | No Errors | N/A |
| List | No Errors | No Errors | N/A | No Errors | No Errors | N/A | No Errors | No Errors | N/A |
| Profiles | No Errors | No Errors | N/A | No Errors | No Errors | N/A | No Errors | No Errors | N/A |

<details><summary>Python Validation Screenshots</summary>



</details>

<p align="right"><a href="#">🔺 Back To Top</a></p>
<hr>

### CSS Validation 

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate my CSS file. External CSS for Bootstrap, provided by [CDN](https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.2.3/css/bootstrap.min.css) was not tested. Warnings were present, these were related to my use of variables for colors and fonts in my CSS file.


  
<p align="right"><a href="#">🔺 Back To Top</a></p>
<hr>
   
## Manual Testing

### User Input/Form Validation

Testing was carried out on desktop using a Chrome browser to ensure all forms take the intended input and process the input appropriately.

| Feature | Tested? | User Input Required | User Feedback Provided | Pass/Fail | Fix |
| :--: | -- | -- | -- | :--: | --: |
| Navbar Logo and Icons | | Click | Logo takes user to 'Home', icons take user to intended location. | Pass  | - |
| Santa's Helper button |  | Click  | When user clicks on the "Santa's helper? Click here" button from the home page they are taken to Santa's "Nice List" where a list of names can be seen | Pass |  |
| Santa's Helper view Wish List |  | Click | When user clicks on a name from the "Nice List" the "Wish List" for that person is presented in a new screen | Pass |  |
| Marking coal on someone's Wish List |  | Click | Santa's helper can click on coal icon at bottom of a person's wish list. Coal icon darkens and coal count for that person increments by 1 for all to see | Pass  |  |
| Deselecting coal on someone's Wish List |  | Click | Santa's helper can click on pre-selected coal icon at bottom of a person's wish list. Coal icon lightens and coal count for that person decrements by 1 for all to see | Fail | Color needs styling to update on click |
| Send a Wish |  | Click | When user clicks on "Send a wish to Santa" button from the home page they are taken to a page with two buttons asking them if they are Naughty or Nice | Pass  |  |
| Naughty button |  | Click | When user selects "Naughty" from the eligibility screen they are presented with a verification screen checking if they are sure they want coal for Christmas with "Yes" and "No" buttons to choose from | N/A | Feature not deployed |
| Confirm Naughty |  | Click | When user confirms "Yes" they are naughty, user is presented with a screen of coal | Pass  |  |
| Don't confirm Naughty |  | Click | When user confirms "No" they are not naughty, user is presented with screen asking them to register to create their wish list | N/A |  |
| Nice button |  | Click | When user selects "Nice" from the eligibility screen they are presented with screen asking them to register to create their wish list | Pass |  |
| Register | | Register form | Upon registering user is presented with their own wish list page | Fail | Implemented to return to home-page instead |
| Add wish |  | Text | Registered user can add wish to their own wish list which can be viewed by anyone | Pass |  |
| Edit wish |  | Text | Registered user can edit items on their own wish list | N/A | Edit functionality not implemented on front end, admin dashboard only |
| Delete wish |  |  | Registered user can delete items on their own wish list | Fail  | Delete functionality not implemented on front end, admin dashboard only |
| Log Out |  | Click | Registered user is presented with "Are you sure..." check | Pass | |  
| Log In |  | Click | Registered user is presented with Login screen, which upon completing, they are taken to their own wish list page | Fail | Implemented to go to home page instead |
| Admin - Add User |  |  | When a user is added via the admin dashboard ensure that they can log in from the application's front end | Pass |  |
| Admin - Delete User |  |  | When a user is deleted via the admin dashboard ensure that they no longer appear on the "Nice List" , can no longer login and no longer have a "Wish List" stored | Pass |  |


<p align="right"><a href="#">🔺 Back To Top</a></p>
<hr>

### Browser Compatibility

Dear Santa was tested on the following browsers:

- Chrome - no issues
- Firefox - no issues

<p align="right"><a href="#">🔺 Back To Top</a></p>
<hr>

### Testing User Stories

User Stories are documented in the Dear Santa [GitHub Projects Board](https://github.com/glaw2000/Christmas-Fun). U

  
### Dev Tools/Real World Device Testing

Responsiveness testing was carried out using Google Dev Tools. Responsiveness was evident on all features throughout. 

## Virtual Test Environment

Using [statcounter](https://gs.statcounter.com/screen-resolution-stats) to attain the latest (_October 2024_) usage stats, I compiled a virtual testing environment using [Responsive Viewer](https://chromewebstore.google.com/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb?hl=en) with the six most popular worldwide screen resolutions. Although the most popular resolution globally is **1920x1080**, the [data](https://gs.statcounter.com/platform-market-share/desktop-mobile-tablet) shows usage stats for **61.63% - Mobile**, **36.52% - Desktop** and the remaining **1.85% - Tablet**, thus reinforcing a mobile first approach to responsive design and UX.

| Rank | Resolution | Global Usage |
| :--: | :--: | --: |
| 1 | 1920x1080 | 9.24% |
| 2 | 350x800 | 6.77% |
| 3 | 375x812 | 4.63% |
| 4 | 390x844 | 4.49% |
| 5 | 1366x768 | 4.28% |
| 6 | 1536x864 | 4.15% |

<p align="right"><a href="#">🔺 Back To Top</a></p>
<hr>

### Known Bugs

- Footer responsivity - requires media qeury to remove images upon reduction to smaller screens

<p align="right"><a href="#">🔺 Back To Top</a></p>
<hr>