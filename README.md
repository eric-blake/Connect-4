# Connect-4

<img src="" alt="Screenshot from http://ami.responsivedesign.is/ website, that show how the website looks on commons screen sizes">

## How to play:
Connect 4 is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.

Connect 4 is a two-player connection rack game. My verison of the game has been modified in to a one player game, where the player plays against the computer. The player take turns dropping colored tokens into a six-row, seven-column vertically suspended grid. The pieces fall straight down, occupying the lowest available space within the column. The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four of one's own tokens. You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Connect_Four "Wikipedia")

-By Eric Blake

# [Live site](https://connect-4-eb-e1e4322e00d6.herokuapp.com/ "Live site") 

## UX design:

### Wireframe

As this is a Python terminal game, a wireframe was not required

### Structure & Logical Flow

A flowchart of the game flow and logic was created using Microsoft Visio.  The flow charts shows how the game will flow and allows consideration for the inputs, outputs and validation required.
<img src="assets/documentation/" alt="Screenshot of flowchart">

## Features:
### Existing Features
### Welcome page
* The first section is welcoming the user to the quiz and requesting a username. This is validated so that the username msut be two or more letters.
<img src="assets/documentation/" alt="Screenshot of flowchart">

### Instructions
* The next section gives the user information and instructions on how to play the game. the user must select a chip colour - "y" for yellow or "r" for red.
<img src="assets/documentation/" alt="Screenshot of flowchart">

* The user is then prompted to enter a column number between 1 and 7. This is validated to only accept number between 1 and 7.
<img src="assets/documentation/" alt="Screenshot of flowchart">

* The board is printed and the user is promoted to select a column between 1 and 7. After selecting a number the chip will be dropped in the board and the board re-printed. 
<img src="assets/documentation/" alt="Screenshot of flowchart">

* The computer then selects a column at random and drops a chip.
<img src="assets/documentation/" alt="Screenshot of flowchart">

* If the user wins a congratulation message will be displayed.
<img src="assets/documentation/" alt="Screenshot of flowchart">

* If the user loses a hard luck message will be displayed.
<img src="assets/documentation/" alt="Screenshot of flowchart">


* If there is no winner a game over - draw message will be displayed.
<img src="assets/documentation/" alt="Screenshot of flowchart">

* At the end of the game the user will have the option to play again or quit. This is validated to only accept the letters "r" for restart or "q" for quit.
<img src="assets/documentation/" alt="Screenshot of flowchart">


## Future Features
* Allow player to select the board size by inputting the number of rows and columns

## Technologies Used

### Coding languages used
The only coding laugauge used in this project was Python3.

### External resources:
* Microsoft Visio was used for the Flowchart
* Heroku: Heroku is used to deploy the programme in the form of an app. This is supported by the Code Institute template that allows a python terminal to be run using a web page.
* Codeanywhere was used as the IDE to code the website.
* Code Institute template - To run the game in the terminal using Heroku.

### Libraries Used
(random) was used to generate column number for the computers move
(time) was used to puase between player move and computer move
(sys) wasused for the print slow function
(os) was used for the clear function


## Testing:

### Manual Testing
| Test | Result |
| ------------- | ------------- |
|  | |
### Validator Testing:


## Bugs
* ### Fixed bugs
| Test | Result |
| ------------- | ------------- |
|  | |


* ### Unfixed Bugs
No unfixed bugs

## Deployment
### ## Deployment
* This project was deployed using Code Institutes mock Terminal for Heroku
* Steps for Deployment 
    * From Heroku Dashboard, select Create new app from the dropdown menu.
    * Add a unique app name and then choose a region closest to you (EU or USA).
    * Click on Create App.
    * Go to support dependencies and select Add Buildpack.
    * The order of the buildpacks is important. Select Python first, then save changes. Then add Node.js second and save changes. If they are not in this order, you can drag them to rearrange them.
    * Add config VAR - key is PORT and the value is 8000
    * Go to Deploy tab and select deployment method - Github, then click connect
    * Enable automatic deploy so Heroku updates app everytime changes pushed to Github
    * Click on View button to take you to your deployed link.

### Cloning the repository
The repository was cloned to my local PC. The steps to clone are as follows.
* In the Github repository, navigate to the main page of the repository.
* Click on the green Code button and copy the URL.
* Select Clone by HTTPS option.
* Open the code editor and within the terminal change the directory to the location you want to clone the repository to.
* Type git clone and paste the URL copied earlier.
* Press enter to create the local clone.

### Forking the repository
By forking the repository, you can make a copy of the repository and make changes without affecting the original repository. the steps to fork are as follows
* Locate the repository in Github.
* On the top right corner of the page click Fork.
* A copy of the repository will now be created in your own repository

## Credits
 * Instructions throughout project was taken from [Code Institute](https://codeinstitute.net/ie/ "Code Institute") Tutorials and Love Sandwiches project.
 * The flowchart was created using Microsoft Visio
 * The Favicon was taken from [Icons8](https://icons8.com/ "Icons8").
 * isalpha method from stack overflow  [Stack overflow](https://stackoverflow.com/  "Stack overflow")
 * Details of Connect-4 game [Wikipedia](https://en.wikipedia.org/wiki/Connect_Four "Wikipedia")

## Acknowledgements
