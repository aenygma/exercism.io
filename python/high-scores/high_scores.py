class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        """ get the latest score
        """

        if len(self.scores) != 0:
            return self.scores[-1]
        return

    def personal_best(self):
        """ get personal best
        """

        return max(self.scores)

    def personal_top_three(self):
        """ get personal top three scores
        """

        lscore = self.scores.copy()
        while len(lscore) > 3:
            lscore.remove(min(lscore))

        lscore.sort(reverse=True)
        return lscore
