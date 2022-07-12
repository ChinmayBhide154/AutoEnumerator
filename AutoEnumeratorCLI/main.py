import typer

app = typer.Typer()

# open the ascii Art and print it
with open("asciiArt.txt", "r") as file:
    for line in file:
        stripped_line = line.strip()
        print(stripped_line)

@app.command()
def hello(command: str, display_iq: bool = True):
    print(f"{command}")

if __name__ == "__main__":
    app()
