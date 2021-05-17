

# Search Algorithms Implementation on Python

- Breadth First Search
- Depth First Search
- Uniform Cost Search

This program accepts an argument("file path") to generate graph.
The command for execute on terminal after downloaded;

    $python3 search.py graph.txt

graph.txt file should look like the following example;
**Example graph.txt:**

    A:{A:0, B:6, C:4, D:3, E:0, F:0, G:0}
    B:{A:6, B:0, C:2, D:0, E:4, F:0, G:0}
    C:{A:4, B:2, C:0, D:2, E:0, F:8, G:0}
    D:{A:3, B:0, C:2, D:0, E:3, F:0, G:0}
    E:{A:0, B:4, C:0, D:3, E:0, F:7, G:6}
    F:{A:0, B:0, C:8, D:0, E:7, F:0, G:6}
    G:{A:0, B:0, C:0, D:0, E:6, F:6, G:0}

After execute the program, program will ask for start and goal state for searching path;

Please enter the start state : A
Please enter the goal state : G

Then, program will give an example output as follows.

**Output:**

 - BFS : A - B - E - G 
 - DFS : A - B - C - D - E - F - G 
 - UCS : A - D - E - G

**Resouce;**
For BFS and DFS: https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/
For UCS: https://rextester.com/GDQAJ78015
