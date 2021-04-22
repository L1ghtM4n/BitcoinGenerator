#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author github.com/L1ghtM4n

__all__ = ['init', 'main']

# Trying import required modules
try:
    from bit import Key
    from pathlib import Path
    from rich.console import Console
except ImportError:
    exit('[!] Modules are not installed, install them by writing "pip3 install -r requirements.txt"')


# Create console instance and clear
console = Console()
console.clear()


# Initialyze all
def init() -> bool:
    # Show banner
    with open('banner.txt', 'r', encoding='utf-8') as banner:
        console.print(banner.read())
    # Create directory if not exists
    Path("wallets").mkdir(parents=True, exist_ok=True)
    # Done
    return True


# Main method
def main() -> bool:
    # Console status bar
    with console.status('[cyan bold]Generating bitcoin private keys (Ctrl+C to stop)[cyan bold]', spinner='point') as status:
        # Infinity loop
        while True:
            # Generate private key and fetch balance from blockchain
            privKey = Key()
            balance = privKey.get_balance()
            # Export key as pem if balance is not empty
            if balance != '0':
                console.print(f'[green][+][/green] [yellow bold]Exporing {privKey.address} with balance {balance}[/yellow bold]')
                with open(f'wallets\\{privKey.address}.pem', 'wb') as export:
                    export.write(privKey.to_pem())
            # Continue if empty balance
            else:
                console.print(f'[red][-][/red] [magenta bold]{privKey.address} zero balance ...[/magenta bold]')
    # Done
    return True


# Run app
if __name__ == '__main__':
    try:
        init()
        main()
    except KeyboardInterrupt:
        console.print('[green][+][/green] [yellow bold]Ctrl+C received, exiting ...[/yellow bold]')
