# Min Occupancy Rate
A large technology company owns a huge building and the director of the company wants to
find the best area within the building to install the new high performance computing (HPC)
facility which will arrive soon. Unfortunately, the company does not have any empty spaces
to be utilised for this purpose. Instead, the director will have to use some of the its currently
underused spaces. In fact, office areas have not been fully used since Covid-19.

Staff offices are placed in each level in a rectangular area with m aisles/columns. Each aisle
has n rows where n > m. The HPC facility will require an area of size n connected sections.
This means that only one section from each row has to be removed, so we end up with one
empty aisle after some shuffling for the remaining sections within each row. Once we identify
the location of those sections, the director and his team will decide what should be done with
team members in these sections.

### Occupancy data:
The director knows the occupancy probability for each section, which is an integer between 0
and 100 (inclusive) that represents the percent of working hours this section is usually occupied
(on average).
Given a matrix of n rows and m aisles/columns P[0...n − 1][0...m − 1], which contains the
occupancy probability values for a total of n · m sections, the task is simply to identify the list
of locations (i, j) for n sections which has the lowest total occupancy rate.

### Selection conditions:
Specifically, we wish to remove only one section from each of the n rows (Condition #1).

To minimise the amount of shuffling work required before the installation, sections selected for
removal in two adjacent rows must be in the same or adjacent columns (Condition #2). This
means that any successive sections from the top row to the bottom row in the final selected
sections should be adjacent vertically or diagonally.

The final solution would be the list of indices of n sections from top to down that has the total
minimum occupancy rate (Condition #3).

To solve this problem, you will write a function select_sections(occupancy_probability).
If there are multiple solutions with same total minimum occupancy rate, you can return any
one of them.

## Input
occupancy_probability is a list of lists. There are n interior lists. All interior lists are length m
(columns/aisles). Each interior list represents a different row of sections. occupancy_probability[i][j]
is an integer number between 0 and 100 (inclusive) which represents the occupancy probability
for a section located at row i and column/aisle j.

## Output
Your algorithm will return a list of 2 items:
* minimum_total_occupancy is an integer, which is the total occupancy for the selected n
sections to be removed
* sections_location is a list of n tuples in the form of (i, j). Each tuple represents the
location of one section selected for removal. i refers to the row index and can range from
0 to n − 1. j refers to the column index and can range from 0 to m − 1.

## Complexity
select_sections should run in O(nm) time and space, where n is the number of rows, and m
is the number of columns/aisles. In the above example, n = 8, m = 5.
