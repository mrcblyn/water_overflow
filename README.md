# Water Overflow Coding Challenge
Repository submission for the Water Overflow Coding Challenge.
Built primarily using Python (Flask), basic HTML, and Docker.

Submitted by: Maricia Balayan (mariciabalayan@gmail.com)

## Problem Statement
There is a stack of water glasses in a form of triangle. Each glass has a 250ml capacity.
When a liquid is poured into the top most glass any overflow is evenly distributed between the glasses in the next row. That is, half of the overflow pours into the left glass while the remainder of the overflow pours into the right glass.

Write a program that is able to calculate and illustrate how much liquid is in the `j`th glass of the `i`th row when `K` litres are poured into the top most glass.

## Assumptions
* A diagram has been provided in the project specifications, which seems to have an error in the last row. I have assumed that the values highlighted in red should be replaced by the values in green: 
  <img width="464" alt="image" src="https://user-images.githubusercontent.com/57266799/160277589-8037373b-a318-4be5-b023-f5f98541fcff.png">

* Input is always `i` (row), `j` (column) and `K` (number of liters), where:
  * `i` (row) is always a valid non-negative integer
  * `j` (column) is always a valid non-negative integer
  * `K` (number of liters) is always a valid non-negative number
* Only the `j`th glass of the `i`th row is needed in the output

### Limitations
* The solution does not handle invalid inputs, assumes always valid
* The solution may not work for very large inputs
* The output illustration may break for very large outputs
* The solution and illustration only take into account glasses until the specified row

### Dependencies
* Docker and docker-compose must be installed
* Python modules used have been added as part of the requirements to be installed by Docker. 

### Executing the program
* Clone the repository `git clone https://github.com/mrcblyn/water_overflow.git`
* Change directory into water_overflow `cd water_overflow`
* Start Docker
* Run `docker-compose up`
  <img width="998" alt="image" src="https://user-images.githubusercontent.com/57266799/160278048-e415c9e0-7bc1-4043-bb95-74f84b520ccb.png">
* Open the application in http://localhost:5000
  <img width="925" alt="image" src="https://user-images.githubusercontent.com/57266799/160278063-eff595e4-cb12-4ac2-8cd0-aac6db285f73.png">
* Input all fields and submit to view the output
  <img width="930" alt="image" src="https://user-images.githubusercontent.com/57266799/160278161-e0206c8b-c287-411a-8d88-61f1b4c1e364.png">

### Testing
* Tests have been created and ran using `pytest`:
  <img width="1118" alt="image" src="https://user-images.githubusercontent.com/57266799/160278238-58c35182-26f0-4a13-accd-0db71f5018e9.png">
