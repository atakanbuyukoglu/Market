# Defines a company and related classes


class Company:

    def __init__(self, name, ticker) -> None:
        # Defining properties of the company
        self.name = name
        self.ticker = ticker

        if ticker:
            self.update_variables()

    
    def update_variables(self):
        # TODO: Obtain the parameters online
        pass
