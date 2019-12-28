## The script

In your project folder, run:

```sh
./run
```

This will start a server for the frontend and a server for the backend.

You can access the frontend in the web browser at the URL that the frontend starts on.

Below describes the problems that this script solves.

## Problem 1: Ports

Every time you start a session on CSE, either via the lab, vlab, or ssh, you are using a particular server. For example, all vlab connections use one of 4 servers: vx1, vx2, vx3, vx4.

Each *server* can only have a student using *a* port on it once.

E.G.
* Andrew is on vx1
* Sally is on vx2
* Yunsar is on vx2

This means that is Sally starts a flask server on port 5000, that Andrew would also be able to (since they're on a different server), but Yunsar no longer can.

Our script above automatically looks for un-used ports no your server and will run your application(s) on that port. This means no more looking for ports.

## Problem 2: Running two flask servers

The way we've setup the frontend is to run on its own flask server.

You can run it directly by running

```sh
python3 frontend/static.py
```

Our script will run both flask servers at the same time for you.