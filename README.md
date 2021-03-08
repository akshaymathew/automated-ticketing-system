# Automated-parking-ticketing-system
An automated car ticket dispatching application in a parking lot

## Prerequisites
* Ubuntu LTS (either 16.04 or 18.04)
* Python3 (download from [here](https://www.python.org/downloads/release/python-386/))

## Problem Statement
Incoming cars to a parking lot are supposed to be given tickets to the nearest available slot. The parking lot has a capacity of `n`. The slot nearest to the entrypoint is `1` and the one farthest is `n`. The application must log the car registration number, driver's age and the slot to which it has been assigned. 
## Approach
I have used a combination of data structures like min heap, dictionary and lists to achieve an optimal solution.
There are three main classes in my approach:
- Ticket: Entities - `registration number, driver age and slot number`
- Parking Lot - Entities - `Initial capacity`, min heap structure and a dictionary (key = `registration number` and value is a tuple of `(slot assigned,driver age)`)
- Parking SLot - Entities - slot, occupied.
On a high level the systems suppports:
- Allocating tickets to an incoming car: This is done in O(1) Average time complexity as the root of the min heap will be the nearest vacant parking slot.
- Deactivating the ticket - This is done in O(N) average time complexity.
- Get registration numbers of all cars for drivers of particular age - Time complexity O(N)
- Get parking slot for a particular vehicle registration number - Time complexity O(1)
- Get slot numbers of all drivers of a particular age- TIme complexity O(N)
## Running tests
Code smells can be identified using SonarLint. It's avaiableas a plugin to IntelliJ IDE
## Running application
Open terminal in the `app` directory of this project and run the command `python app.py <relative path-to-input-file>`. In this project's case run `python app.py ../input.txt`
## Authors/Acknowledgements
@author : Akshay Mathew (akshaymathew20@gmail.com)

