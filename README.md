## Mocks

This directory contains static mock responses for testing the fantasy-calculator.

### Usage

To use, run the following command in this directory (using python2):

    python server.py
    
### Mock data

The following leagues have mock data:

 - 1: Empty league
 - 2: League with players on the board
 - 3: League with players on the board and many draft results
 
### Generating new mock cases

Use `MockDataBuilderTest` to add the data you are interested in, and run the test to generate 
the JSON output. Put it in a file `api/league/{leagueId}` and add it to the list above.