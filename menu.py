class Menu (object):
    _keys = ["title", "function"]
    
    def __init__(self, title, options=[], prompt="> "):
        self.title = title
        self.options = options
        self.prompt = prompt
    
    def add_option(self, option):
        for key in self._keys:
            if key not in option:
                raise TypeError("Key '%s' missing in option %d" % (key, i))
        self._options.append(option)
        self._answers[str(len(self._options))] = option
    
    @property
    def options(self):
        return self._options[:]
    
    @options.setter
    def options(self, options):
        for i, item in enumerate(options):
            for key in self._keys:
                if key not in item:
                    raise TypeError("Key '%s' missing in option %d" % (key, i))
            if "arguments" in item and not isinstance(item["arguments"], list):
                raise TypeError("Option %d arguments must be a list" % (i))
            if "keyword arguments" in item and not isinstance(item["keyword arguments"], dict):
                raise TypeError("Option %d keyword arguments must be a dict" % (i))
        self._options = options
        self._answers = {}
        for i, item in enumerate(self._options):
            self._answers[str(i + 1)] = item
    
    @property
    def answers(self):
        a = {}
        a.update(self._answers)
        return a
    
    def run(self, raiseinterrupt=False):
        print()
        print(self.title)
        print()
        width = len(self.options) + 1
        width = len(str(width))
        for i, item in enumerate(self.options):
            print("%*d. %s" % (width, i + 1, item["title"]))
        answer = None
        while answer not in self.answers:
            try:
                answer = input(self.prompt)
            except KeyboardInterrupt:
                if raiseinterrupt:
                    raise
                else:
                    return
        answer = self.answers[answer]
        args = answer.get("arguments", [])
        kwargs = answer.get("keyword arguments", {})
        return answer["function"](*args, **kwargs)
    
    __call__ = run
    
    def runloop(self):
        while True:
            try:
                self.run(raiseinterrupt=True)
            except KeyboardInterrupt:
                break
