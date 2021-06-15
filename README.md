# Discord Vaccine Alerts

Get discord vaccine alerts for a particular pincode of your choice. 
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip3 install virtualenv
virtualenv -p python3 ./vaccine-alerts
source vaccine-alerts/bin/activate
pip install -r requirements.txt 
```

## Usage

In order to use it, make a .env file with the following contents in the same directory 

```python
PINCODE = <enter pincode here>
DISCORD_WEBHOOK = <enter url here>
```

## Further Notes

The code can be easily modified to search by District, change age group to 45+, get slot2 availability etc. Will try to implement a more modular design with
error checks in the future. 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
