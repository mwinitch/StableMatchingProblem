# Stable Matching Problem

The stable matching problem, also referred to as the stable marriage problem, is a problem of finding matches between two sets of elements of the same size. Each element has a list of preferences for the elements of the other set. The problem can be solved with the Gale-Shapley algorithm. This program creates a visualization of the algorithm in action, where the elements being matched are a set of red circles and a set of blue circles.  

The Gale-Shapley Algorithm runs as follows:
1. Find the first unmatched red circle and let it go to the blue circle they prefer the most who has not rejected them
2. If that blue circle is unmatched, then the red and blue circle are matched
3. If the blue circle is already matched but prefers the new red circle more, the blue circle breaks the old match and forms a new one with the new red circle
4. If the blue circle is already matched and prefers their current match to the new one, then the blue circle does not break their current match and rejects the new red circle
5. Repeat steps 1-4 until all red circles are matched

The matches are defined to be stable as follows:
There does not exist a match between a red and blue circle where both would prefer each other more than their current match

The program creates a tkinter window that has five circles on each side of the screen. The five circles on the left side are red, while the five circle on the right side are blue. Each one of the circles has a set of preferences for the other colored group of circles. A line is created between the red and blue circle when a match is attempted to be made. The line will be destroyed if the match is not made and the red circle stays unmatched.

The two files in this program are the runner file and the Matches file. The runner file is the main file that creates the window and runs the matching algorithm. The Matches final contains classes for the red and blue circle objects and holds information about each one.   



