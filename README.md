# Simple API using Flask and Postgree as Database

This is simple api i was learned from teclado channel in yt. there is 3 endpoint created
1. Endpoint for create room  ( endpoint: /api/room , payload: { name } , method = POST )
2. Endpoint for save temperature in certain room ( endpoint: /api/temperature , payload: { room, temperature, date } , method = POST )
3. Endpoint for see average temperature all room ( endpoint: /api/average, payload: none , method = GET )

To install this, just clone :

```bash
  git clone https://github.com/do4zero/python.flask.teclado.create-api-flask-postgree.git myproject
```

Then, go to your command line and your folder location :

```bash
 cd myproject
```

After that install depedencies package using this command :

```bash
 pip install -r requirements.txt
```

Finaly run project using this command :

```bash
  flask run
```
