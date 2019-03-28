class Scale(object):
    """
    represent a Scale for notes
    """

    sscale = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    fscale = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
    interval_map = {'m': 1, 'M': 2, 'A': 3}
    sharps_scale = ['G', 'D', 'A', 'E', 'B', 'F#', 'e', 'b', 'f#', 'c#', 'g#',\
                   'd#', 'C', 'a']
    flats_scale = ['F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'd', 'g', 'c', 'f', \
                   'bb', 'eb']

    def __init__(self, tonic):
        """ """

        self.scale = None
        self.tonic = tonic

        # determine if tonic Major or minor
        if self.tonic == self.tonic.lower():
            self.scale_type = 'minor'
        else:
            self.scale_type = 'major'

        # assign scale
        self.chromatic()

    def chromatic(self):
        """ return chromatic scale """

        scale = None
        if self.tonic in self.sharps_scale:
            scale = self.sscale
        elif self.tonic in self.flats_scale:
            scale = self.fscale
        else:
            print("error", self.tonic)

        # tonic to note (remove case-format)
        note = self.tonic[0].upper() + self.tonic[1:]

        # rotate scale to make tonic primary element
        idx = scale.index(note)
        self.scale = scale[idx:] + scale[:idx]
        return self.scale

    def interval(self, intervals):
        """ apply given interval to scale """

        idx = 0
        ret = []

        for interval in intervals:
            ret.append(self.scale[idx])
            idx = self.interval_map.get(interval) + idx
        return ret
