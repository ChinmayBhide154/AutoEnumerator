import typer
from Scanner import Scanner
import os

app = typer.Typer()

scanner = Scanner(None, "w", "nmap2.txt", "nikto.txt", "gobuster.txt", None)
# open the ascii Art and print it
with open("asciiArt.txt", "r") as file:
    for line in file:
        stripped_line = line.strip()
        print(stripped_line)

@app.command()
def command(command: str, ip_address: str):
    scanner.target = ip_address
    if command == "run":
        os.system("nmap " + scanner.target)




if __name__ == "__main__":
    app()
