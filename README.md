# retailer-search-rank

	Requirements:
------------------
 Python 3.6.9
 Virtual Enviornment


	Steps:
-------------
1) Install Python3
	sudo apt-get install python3

2) create an Virtual Environment
	python3 -m venv environmentName

3) Install all the requirements in the environment
	pip3 install -r requirements.txt

4) Run the retailer_search_rank.py
	python retailer_search_rank.py

5) Inputs are:
	Hair Fall Shampoo, Conditioner, Shampoo


	Example:
----------------

RUN : python retailer_search_rank.py


INPUTS : Hair Fall Shampoo, Conditioner, Shampoo


OUTPUTS :

{
    "result": [
        {
            "keyword": "hair fall shampoo",
            "position": {
                "Wow": "",
                "Loreal": 1,
                "Biotique": 2
            }
        },
        {
            "keyword": "conditioner",
            "position": {
                "Wow": 6,
                "Loreal": 4,
                "Biotique": ""
            }
        },
        {
            "keyword": "shampoo",
            "position": {
                "Wow": 30,
                "Loreal": 1,
                "Biotique": 4
            }
        }
    ]
}