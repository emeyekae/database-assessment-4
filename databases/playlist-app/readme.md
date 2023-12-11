## Playlist-app

To get this application running, make sure you do the following in the Terminal, in the app directory:

1. python3 -m venv venv
2. source venv/bin/activate
3. Run the command below based you your python version.  You can run `"python3 -V"`  to find out which version you have. 

&ensp;Python 3.7 
```sh
   (venv)$ pip3 install -r requirements3-7.txt
``` 
&ensp;Python 3.8
```sh
   (venv)$ pip3 install -r requirements3-8.txt
``` 
4. `createdb playlist-app`
5. `flask run`

## To load the seed file

1. Open a new linux window in the same "app" directory.
2. python3 -m venv venv
3. source venv/bin/activate
4. python3 seed.py