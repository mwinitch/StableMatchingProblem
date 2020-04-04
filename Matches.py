# LeftObject represents a red circle
class LeftObject:
    def __init__(self, letter, shape, pref):
        self.letter = letter
        self.shape = shape
        self.pref = pref
        self.free = True
        self.curr_index = 0
        self.line = None

    # Returns a formatted string of the circle's preferences to be displayed in the GUI
    def give_pref(self):
        result = ""
        for i in self.pref:
            result += (i + ' ')
        return result.rstrip()

    # Chooses the red's circle current preference
    def choose(self):
        x = self.pref[self.curr_index]
        self.curr_index = self.curr_index + 1
        return x

# RightObject represents a blue circle
class RightObject:
    def __init__(self, letter, shape, pref):
        self.letter = letter
        self.shape = shape
        self.pref = pref
        self.free = True
        self.match = None

    # Returns a formatted string of the circle's preferences to be displayed in the GUI
    def give_pref(self):
        result = ""
        for i in self.pref:
            result += (i + ' ')
        return result.rstrip()

    # If a red circle tries to match with a blue circle but the blue circle is already matched, this method
    # will determine if the blue circle prefers the new match more
    def prefers(self, new_match):
        for i in self.pref:
            if i == new_match.letter:
                return True
            if i == self.match.letter:
                return False