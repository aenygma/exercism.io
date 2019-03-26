# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman(object):
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.masked = "_"*len(word)

    def guess(self, char):
        """ process user's guess """

        if self.get_status() != STATUS_ONGOING:
            raise ValueError("Nice try sucka!")

        # iterate over word, unveil where char is present
        tmasked = list(self.masked)
        for idx, ch in enumerate(self.word):
            if ch == char:
                tmasked[idx] = ch
        tmasked = "".join(tmasked)

        # if nothing new is unveiled, counts as an attempt
        if tmasked == self.masked:
            self.remaining_guesses -= 1
        else:
            self.masked = tmasked

    def get_masked_word(self):
        """ return masked word """

        return self.masked

    def get_status(self):
        """ determine current game status """

        if self.remaining_guesses < 0:
            self.status = STATUS_LOSE
        if (self.remaining_guesses >= 0) and (self.masked == self.word):
            self.status = STATUS_WIN

        return self.status

