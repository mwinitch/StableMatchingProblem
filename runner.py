from tkinter import *
from Matches import LeftObject, RightObject

# This program solves a matching problem using the Gale-Shapley algorithm. The program creates 5 red circles on
# the left side and 5 blue circles on the right side. The Gale-Shapley algorithm attempts to create a stable matching
# between the two sets of circles where each one has a list of preferences. The red circles are labelled A-E and the
# blue circles are labelled F-J. The shapes and lines are created in a tkinter canvas frame. To slow down the
# program the root.after() is used. This method waits a given amount of time and can then execute a function that
# was passed into the method. However, when this method is called the code will continue to run and only stops
# updates to the tkinter frame. Therefore, the Gale-Shapley algorithm can not run in a normal while loop as it will
# run faster than the tkinter frame is able to update. 

# Setting up the main Tk window
root = Tk()
root.title('Stable Matching Problem')
canvas_width = 800
canvas_height = 500
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# Preferences for the red circle where each row represents one of the circle's preferences for the blue circle
left_pref = [['H', 'G', 'F', 'I', 'J'],
             ['H', 'F', 'G', 'J', 'I'],
             ['F', 'H', 'J', 'G', 'I'],
             ['H', 'F', 'G', 'I', 'J'],
             ['G', 'I', 'J', 'H', 'F']]

# Preferences for the blue circle where each row represents one of the circle's preferences for the red circle
right_pref = [['A', 'D', 'E', 'B', 'C'],
              ['C', 'D', 'E', 'B', 'A'],
              ['B', 'E', 'A', 'D', 'C'],
              ['B', 'A', 'D', 'E', 'C'],
              ['C', 'E', 'A', 'D', 'B']]

txt = canvas.create_text(60, 20, text='Preferences', font='arial')

# Creates a red circle A and stores its info in a LeftObject
a0_shape = canvas.create_oval(140, 40, 200, 100, fill='red')
a0 = LeftObject('A', a0_shape, left_pref[0])
a0_text = canvas.create_text(170, 70, text=a0.letter, font='arial')
a0_pref = canvas.create_text(60, 70, text=a0.give_pref(), font='arial')

# Creates a red circle B and stores its info in a LeftObject
a1_shape = canvas.create_oval(140, 120, 200, 180, fill='red')
a1 = LeftObject('B', a1_shape, left_pref[1])
a1_text = canvas.create_text(170, 150, text=a1.letter, font='arial')
a1_pref = canvas.create_text(60, 150, text=a1.give_pref(), font='arial')

# Creates a red circle C and stores its info in a LeftObject
a2_shape = canvas.create_oval(140, 200, 200, 260, fill='red')
a2 = LeftObject('C', a2_shape, left_pref[2])
a2_text = canvas.create_text(170, 230, text=a2.letter, font='arial')
a2_pref = canvas.create_text(60, 230, text=a2.give_pref(), font='arial')

# Creates a red circle D and stores its info in a LeftObject
a3_shape = canvas.create_oval(140, 280, 200, 340, fill='red')
a3 = LeftObject('D', a3_shape, left_pref[3])
a3_text = canvas.create_text(170, 310, text=a3.letter, font='arial')
a3_pref = canvas.create_text(60, 310, text=a3.give_pref(), font='arial')

# Creates a red circle E and stores its info in a LeftObject
a4_shape = canvas.create_oval(140, 360, 200, 420, fill='red')
a4 = LeftObject('E', a4_shape, left_pref[4])
a4_text = canvas.create_text(170, 390, text=a4.letter, font='arial')
a4_pref = canvas.create_text(60, 390, text=a4.give_pref(), font='arial')

txt2 = canvas.create_text(740, 20, text='Preferences', font='arial')

# Creates a blue circle F and stores its info in a RightObject
b0_shape = canvas.create_oval(600, 40, 660, 100, fill='dodger blue')
b0 = RightObject('F', b0_shape, right_pref[0])
b0_text = canvas.create_text(630, 70, text=b0.letter, font='arial')
b0_pref = canvas.create_text(740, 70, text=b0.give_pref(), font='arial')

# Creates a blue circle G and stores its info in a RightObject
b1_shape = canvas.create_oval(600, 120, 660, 180, fill='dodger blue')
b1 = RightObject('G', b1_shape, right_pref[1])
b1_text = canvas.create_text(630, 150, text=b1.letter, font='arial')
b1_pref = canvas.create_text(740, 150, text=b1.give_pref(), font='arial')

# Creates a blue circle H and stores its info in a RightObject
b2_shape = canvas.create_oval(600, 200, 660, 260, fill='dodger blue')
b2 = RightObject('H', b2_shape, right_pref[2])
b2_text = canvas.create_text(630, 230, text=b2.letter, font='arial')
b2_pref = canvas.create_text(740, 230, text=b2.give_pref(), font='arial')

# Creates a blue circle I and stores its info in a RightObject
b3_shape = canvas.create_oval(600, 280, 660, 340, fill='dodger blue')
b3 = RightObject('I', b3_shape, right_pref[3])
b3_text = canvas.create_text(630, 310, text=b3.letter, font='arial')
b3_pref = canvas.create_text(740, 310, text=b3.give_pref(), font='arial')

# Creates a blue circle J and stores its info in a RightObject
b4_shape = canvas.create_oval(600, 360, 660, 420, fill='dodger blue')
b4 = RightObject('J', b4_shape, right_pref[4])
b4_text = canvas.create_text(630, 390, text=b4.letter, font='arial')
b4_pref = canvas.create_text(740, 390, text=b4.give_pref(), font='arial')

# List representing the left red circles A - E
choosers = [a0, a1, a2, a3, a4]

# Dictionary mapping the right circle's letter to the corresponding object
dict_chooser = {'F': b0,
                'G': b1,
                'H': b2,
                'I': b3,
                'J': b4}

size = len(choosers)

# Matches the red and blue circle, represented by drawing a line connecting the two
def engage(left_ele, right_ele):
    left_ele.free = False
    right_ele.free = False
    right_ele.match = left_ele
    ax0, ay0, ax1, ay1 = canvas.coords(left_ele.shape)
    bx0, by0, bx1, by1 = canvas.coords(right_ele.shape)
    left_ele.line = canvas.create_line(ax1 + 5, (ay0 + ay1)/2, bx0 - 5, (by0 + by1)/2, fill='green2', width=3)
    root.after(1000, stable_match_making)

# The blue circle breaks up with its old red circle match and now matches with the new red circle
def disengage(choice, old_match, new_match):
    ax0, ay0, ax1, ay1 = canvas.coords(new_match.shape)
    bx0, by0, bx1, by1 = canvas.coords(choice.shape)
    line = canvas.create_line(ax1 + 5, (ay0 + ay1) / 2, bx0 - 5, (by0 + by1) / 2, fill='green2', width=3)
    new_match.line = line
    choice.match = new_match
    root.after(2000, lambda: canvas.delete(old_match.line))
    old_match.free = True
    new_match.free = False
    root.after(4000, stable_match_making)

# If the blue circle is matched and does not prefer the new match, this method draws a line to show the attempted
# match and then destroys the line
def stay_together(right_ele, rejected_left_ele):
    ax0, ay0, ax1, ay1 = canvas.coords(rejected_left_ele.shape)
    bx0, by0, bx1, by1 = canvas.coords(right_ele.shape)
    line = canvas.create_line(ax1 + 5, (ay0 + ay1) / 2, bx0 - 5, (by0 + by1) / 2, fill='green2', width=3)
    root.after(2000, lambda: canvas.delete(line))
    root.after(4000, stable_match_making)

# This is the implementation of the Gale-Shapley algorithm
def stable_match_making():
    button.config(state=DISABLED)
    global size
    # While there is an unmatched red circle
    while size > 0:
        free = None
        # Choose the first red circle that is not matched to a blue circle
        for i in choosers:
            if i.free:
                free = i
                break
        # Gets the first blue circle on red's preference list whom red has not matched with yet
        choice = dict_chooser[free.choose()]
        # If the blue circle is not yet matched then the red and blue circle are matched
        if choice.free:
            size -= 1
            root.after(1000, lambda: engage(free, choice))
            break

        # If the blue circle is already matched
        else:
            # If the blue circle prefers the new match more than their current match
            if choice.prefers(free):
                root.after(1000, lambda: disengage(choice, choice.match, free))
                break
            # If the blue circle prefers their current match more than the new proposer
            else:
                root.after(1000, lambda: stay_together(choice, free))
                break

# Start button that when clicked starts the algorithm
button = Button(root, text='Start', command=stable_match_making, width=10, font='arial', bg='light gray')
button.pack()
root.mainloop()
