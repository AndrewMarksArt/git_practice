class PublicPrivateExample:
    def __init__(self) -> None:
        self.public = "safe"
        self._unsafe = "unsafe"

    def public_method(self):
        # clients can use this
        pass

    def _unsafe_method(self):
        # clients should not use this
        pass
