from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer, Interpreter
from rasa_nlu import config

command = "not_exit"


def read_and_write(command_value):
    while command_value != "exit":
        command_input = input("Enter a command: ")
        result = interpreter.parse(str(command_input))
        print("Operation: " + str(result['intent']['name']))
        if command_input == "exit":
            print("Exiting..")
            break


training_data = load_data('data/examples/fusion/fusion.md')
trainer = Trainer(config.load("configurations/fusion_configs.yml"))
trainer.train(training_data)
model_directory = trainer.persist('./projects/default/')
interpreter = Interpreter.load(model_directory)

read_and_write(command)
