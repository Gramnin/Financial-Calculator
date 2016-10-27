class Menu (object):
    r"""
    A basic menu module
    """
    
    _keys = ["title", "function"]
    
    def __init__(self, title, options=[], prompt="> "):
        self.title = title
        self.options = options
        self.prompt = prompt
    
    def add_option(self, option):
        r"""
        Append a new option
        
        Raises TypeError on invalid options
        
        Options must be a dict with the following keys:
        'title' is the name of the option (required)
        'function' is the function to run if selected (required)
        'arguments' is a list of the arguments to pass to the called function (optional)
        'keyword arguments' is a dict of the arguments to pass to the called function (optional)
        """
        for key in self._keys:
            if key not in option:
                raise TypeError("Key '%s' missing in option %d" % (key, i))
        self._options.append(option)
        self._answers[str(len(self._options))] = option
    
    @property
    def options(self):
        r"""
        The list of option items
        """
        return self._options[:]
    
    @options.setter
    def options(self, options):
        r"""
        Set options and answers
        
        Raises TypeError on invalid options
        """
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
        r"""
        A map of numbers to options
        """
        a = {}
        a.update(self._answers)
        return a
    
    def run(self, raiseinterrupt=False):
        r"""
        Run the menu once
        
        prompt until KeyboardInterrupt or number of valid option
        """
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
        r"""
        Run the menu until keyboard interrupt
        """
        while True:
            try:
                self.run(raiseinterrupt=True)
            except KeyboardInterrupt:
                break
