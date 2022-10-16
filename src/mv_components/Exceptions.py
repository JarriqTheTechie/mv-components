class AmbiguousError(Exception):
    pass


class NotImplementedError(Exception):
    pass


class FlaskNotInstalledError(Exception):
    def __init__(self) -> None:
        super().__init__("Please install flask in order to use this framework. pip install flask")


class ComponentNotFoundError(Exception):
    def __init__(self, component: str) -> None:
        self.component = component
        self.message = f"No view with the name {component} was found."
        super().__init__(self.message)