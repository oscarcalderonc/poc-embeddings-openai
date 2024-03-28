from ask_questions import ask
from gen_embedding import load_embedding
import os
import click

@click.command()
def interactive_session():
    """Starts an interactive CLI session where the user can ask questions."""
    click.echo("Interactive CLI Session. Type 'exit' to quit.")
    load_embedding("business_rules")

    while True:
        # Ask the user for input
        question = click.prompt("Please ask your question")

        # Check if the user wants to exit
        if question.lower() == 'exit':
            click.echo("Exiting interactive session.")
            break

        answer = ask(question)
        click.echo(answer)

@click.command()
def single_question():
    """Starts an interactive CLI session where the user can ask questions."""
    click.echo("Interactive CLI Session. Type 'exit' to quit.")
    load_embedding("business_rules")

    prompts_folder = "prompts"
    question_file_name = "question_prompt.txt"
    question_file_path = os.path.join(os.getcwd(), prompts_folder, question_file_name)
    
    with open(question_file_path, "r") as question_file:
        question = question_file.read()

    report_file_name = "clear_report_data.txt"
    report_file_path = os.path.join(os.getcwd(), prompts_folder, report_file_name)
    
    with open(report_file_path, "r") as report_file:
        report = report_file.read()

    full_question = question + " " + report
    answer = ask(full_question)
    click.echo(answer)

if __name__ == '__main__':
    single_question()
