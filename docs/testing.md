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
   
### Lighthouse Scores

Lighthouse testing was carried out in Incognito mode to acheive the best result. Performance was lower than preferred due to the site being image heavy. Images used in the sites design were saved in webp and png format, and compressed using [tinypng](https://tinypng.com/) and [Convertio](https://www.convertio.co) to offer the best chance for a decent performance score. The CDNs used for Bootstrap were also noted in the Lighthouse report as causing issue with performance. This report will be reviewed for future development of Freefido to raise this score.

**Desktop**  

![Lighthouse scores desktop](documentation/testing/desktop_lh.png)  
*Desktop Home Page*  
  
![Lighthouse scores desktop](documentation/testing/dt_art_lh.png)  
*Desktop Article Page*
  
**Mobile**  

![Lighthouse scores mobile](documentation/testing/mobile_lh.png) 
*Mobile Home Page*  
  
![Lighthouse scores mobile](documentation/testing/mob_art_lh.png) 
*Mobile Article Page*
  
<p align="right"><a href="#">🔺 Back To Top</a></p>
<hr> 

### Wave Accessibility Evaluation

![WAVE Web Accessibility Evaluation Tools](documentation/testing/wave_report.png)  


<p align="right"><a href="#">🔺 Back To Top</a></p>
<hr> 

## Manual Testing

### User Input/Form Validation

Testing was carried out on desktop using a Chrome browser to ensure all forms take the intended input and process the input appropriately.

| Feature | Tested? | User Input Required | User Feedback Provided | Pass/Fail | Fix |
| :--: | -- | -- | -- | :--: | --: |
| Navbar Logo and Icons | | Click | Logo takes user to 'Home', icons take user to intended location. Tooltips used in desktop/mobile view to provide accessibility and further information about the icons purpose and intention |  | - |
| Santa's Helper button |  | Click  | When user clicks on the "Santa's helper? Click here" button from the home page they are taken to Santa's "Nice List" where a list of names can be seen |  |  |
| Santa's Helper view Wish List |  | Click | When user clicks on a name from the "Nice List" the "Wish List" for that person is presented in a new screen |  |  |
| Marking coal on someone's Wish List |  | Click | Santa's helper can click on coal icon at bottom of a person's wish list. Coal icon darkens and coal count for that person increments by 1 for all to see |  |  |
| Deselecting coal on someone's Wish List |  | Click | Santa's helper can click on pre-selected coal icon at bottom of a person's wish list. Coal icon lightens and coal count for that person decrements by 1 for all to see |  |  |
| Send a Wish |  | Click | When user clicks on "Send a wish to Santa" button from the home page they are taken to a page with two buttons asking them if they are Naughty or Nice |  |  |
| Naughty button |  | Click | When user selects "Naughty" from the eligibility screen they are presented with a verification screen checking if they are sure they want coal for Christmas with "Yes" and "No" buttons to choose from |  |  |
| Confirm Naughty |  | Click | When user confirms "Yes" they are naughty, user is presented with a screen of coal |  |  |
| Don't confirm Naughty |  | Click | When user confirms "No" they are not naughty, user is presented with screen asking them to register to create their wish list |  |  |
| Nice button |  | Click | When user selects "Nice" from the eligibility screen they are presented with screen asking them to register to create their wish list |  |  |
| Register | | Register form | Upon registering user is presented with their own wish list page |  |  |
| Add wish |  | Text | Registered user can add wish to their own wish list which can be viewed by anyone |  |  |
| Edit wish |  | Text | Registered user can edit items on their own wish list |  |  |
| Delete wish |  |  | Registered user can delete items on their own wish list |  |  |
| Log Out |  | Click | Registered user is presented with "Are you sure..." check | | |  
| Log In |  | Click | Registered user is presented with Login screen, which upon completing, they are taken to their own wish list page |  |  |
| Admin - Add User |  |  | When a user is added via the admin dashboard ensure that they can log in from the application's front end |  |  |
| Admin - Delete User |  |  | When a user is deleted via the admin dashboard ensure that they no longer appear on the "Nice List" , can no longer login and no longer have a "Wish List" stored |  |  |


<p align="right"><a href="#">🔺 Back To Top</a></p>
<hr>

### Browser Compatibility

Freefido was tested on the following browsers, new users were created, old users data edited and all features were tested:

- Chrome v114.0.5735.199
- Firefox v114.0.2
- Edge v114.0.1823.79
- Safari v16.5.1

| Browser | Issue | Functionality |
|---------|-------|---------------|
| FireFox | Profile Edit/Upload Image - File input 'Browse' Button centered in input field | Button works as expected |
| FireFox | Profile Dashboard - scrollbars following Mozilla styling | No issue |
| Safari  | Scrollbars following Safari styling | No issue |

<p align="right"><a href="#">🔺 Back To Top</a></p>
<hr>

### Testing User Stories

User Stories are documented in the FreeFido [GitHub Projects Board](https://github.com/users/amylour/projects/4). User Stories are numbered, with Acceptance Criteria and Tasks detailed within. Testing was carried out on Dev Tools for desktop/tablet/mobile, by creating multiple accounts for test users: FidoTest1, FidoTest2, FidoTest3 etc and following through by ensuring that the Acceptance Criteria were met. All features were tested to ensure that they provided the user with the expected output and action.


| User Story | Acceptance Criteria Met? | Tested | Response | Pass/Fail | Fix |
| :--: | -- | -- | -- | :--: | --: |
| [No.](Link) | Yes | Yes | No issues| Pass | - |

<p align="right"><a href="#">🔺 Back To Top</a></p>
<hr>
  
### Dev Tools/Real World Device Testing

Responsiveness testing was carried out using Google Dev Tools on the devices detailed within the below table. Responsiveness was evident on all features throughout all tested devices. Occassionally I would have to refresh the page by clicking the 'FreeFido' logo as the page would load zoomed in or out on the simualted device. When refreshed and CSS checked the desired outcome was observed. I put this down to a caching issue in Chrome as this issue was not observed when testing on the available real world devices.

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

**Dev Tools Device Testing - all features tested, issues noted below**
| Device  | Feature    | Issue  | Fix  |
| ------- | ---------- | ------ |------|
| iPhone 4 | Messages | Text overlap with 'x' close button, article image squashed | Separate media query created for screens max-width: 350px to cope with iPhone4 320px screen width, message font size reduced, article image size reduced |
| iPhone12 Pro | All features | No issues | None needed |
| Samsung Galaxy A51 | All features | No issues | None needed |
| iPad Pro | All features | No issues | None needed |
   
  
**Real World Device Testing**
| Device      | Feature    | Issue  | Fix  | 
| ------------| ---------- | ------ |------|
| OPPO Reno 8 Lite |   All features    | No issues | None needed |
| iPhone XR | All features |  No issues  | None needed |
| iPhone 12  | All features | No issues | None needed |
| iPad Pro 2021 |    All features      |    No issues    |  None needed |
| Acer Aspire 3 2019 laptop | All features | No issues | None needed |


## Bugs  
  
As this was my first Django/Database project, most of the bugs that I encountered were learning and teething issues.\
The below bugs are bugs that I spent a longer length of time investigating or required the assistance of Tutor Support.

| No. | Bug | Solved | Fix | Solution Credit | Commit no. |
| :--: | :--: | :--: | :-- | :-- | --: |
| 1   | # | # | # | [Credited Source](Link) | [######](Link) |

### Known Bugs

- Detail known bugs that have yet to be rectified. 

<p align="right"><a href="#">🔺 Back To Top</a></p>
<hr>