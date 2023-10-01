class Madlib:
    def __init__(self, inputs):
        self.inputs = inputs

    def printMadlib(self):
        print(
            f"""
            
            In a mystical realm, there lived a {self.inputs['adjective_1']} basketball player named {self.inputs['name']}. {self.inputs['name']} possessed a {self.inputs['noun_1']} that granted them incredible {self.inputs['adjective_2']} powers. Whenever they stepped onto the court, the basketball would {self.inputs['verb_1']} through the air. During a game against a rival team known for their {self.inputs['adjective_3']} skills, {self.inputs['name']} unleashed their {self.inputs['adjective_2']} abilities. The basketball seemed to {self.inputs['verb_2']} on its own, and {self.inputs['name']} scored an {self.inputs['adjective_4']} shot, leaving both fans and opponents in awe of the truly {self.inputs['adjective_5']} basketball wizard.
            
            """
        )


if __name__ == "__main__":
    input_words = {
        "name": input("Enter your name: "),
        "adjective_1": input("Enter an adjective about a basketball player: "),
        "noun_1": input("Enter a noun of your choice: "),
        "adjective_2": input("Enter a adjective about magic: "),
        "verb_1": input("Enter verb of your choice: "),
        "adjective_3": input("Enter an adjective of your choice: "),
        "verb_2": input("Enter a verb of your choice: "),
        "adjective_4": input("Enter an adjective of your choice: "),
        "adjective_5": input("Enter an adjective about yourself: "),
    }

    print("Here is your madlib")
    madlib = Madlib(input_words)
    madlib.printMadlib()
