import formatters as f
import types
import re

class SolidityTypeUReal(types.SolidityType):

    def __init__(self):
        self._inputFormatter = f.formatInputReal
        self._outputFormatter = f.formatOutputReal

    @classmethod
    def isType(self, name):
        return re.match(r"^ureal([0-9]*)?(\[([0-9]*)\])*$", name) is not None

    @classmethod
    def staticPartLength(self, name):
        return 32 * self.staticArrayLength(name)