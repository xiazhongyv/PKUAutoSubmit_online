sudo cp -p ./chromedriver/bin/chromedriver /usr/bin/
chmod -R 777 /usr/bin/chromedriver
chmod -R 777 ./chromedriver/bin/chromedriver
python main.py --ID ${{ID}} --PASSWORD ${{PASSWORD}} --SENDKEY ${{SENDKEY}}