from ask_questions import ask
import click



@click.command()
def interactive_session():
    """Starts an interactive CLI session where the user can ask questions."""
    click.echo("Interactive CLI Session. Type 'exit' to quit.")

    while True:
        # Ask the user for input
        question = click.prompt("Please ask your question")

        # Check if the user wants to exit
        if question.lower() == 'exit':
            click.echo("Exiting interactive session.")
            break

        answer = ask(question)
        click.echo(answer)

if __name__ == '__main__':
    interactive_session()
