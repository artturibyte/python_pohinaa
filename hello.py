import numpy as np
import typer


typer_app = typer.Typer(add_completion=False)

@typer_app.command()
def greetings(name: str):
    print(f"Hello from python-pohinaa {name}!")

@typer_app.command()
def get_pi():
    print(np.pi)


if __name__ == "__main__":
    typer_app()
