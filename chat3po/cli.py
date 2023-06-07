import os

import click

from chat3po.chat3po import Chat3PO


@click.group()
def cli():
    pass


@cli.command()
def free_chat():
    chatbot = Chat3PO(api_key=os.environ['CHAT3PO_API_KEY'])

    try:
        print("C-3PO: ", chatbot.run("Introduce yourself."))
        while True:
            print("You: ", end='')
            input_ = input()
            print("C-3PO: ", chatbot.run(input_))
    except KeyboardInterrupt:
        print("\nConversation ended.")


if __name__ == '__main__':
    cli()
