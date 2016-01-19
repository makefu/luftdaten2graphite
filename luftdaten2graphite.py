import csv
import sys
import socket
import datetime as dt
import logging as log


def send_all_data(sensor,kv,host='localhost',port=2003):
    import socket
    data=""
    sock = socket.socket()
    for value,ts in kv:
        data+="{} {} {}\n".format(sensor,value,ts)
    sock.connect((host, port))
    log.info(data.strip())
    sock.sendall(data.encode())
    sock.close()

with open(sys.argv[1]) as csvfile:
    r = csv.DictReader(csvfile,delimiter=";")
    p1 = []
    p2 = []
    for row in r:
        # TODO: multiple ids in csvfile
        sensor_id=row['sensor_id']
        timedate = row['timestamp'].split("+")[0]
        ts = ( dt.datetime.strptime(timedate,"%Y-%m-%dT%H:%M:%S.%f") - dt.datetime.fromtimestamp(0)).total_seconds()
        p1.append([row["P1"],ts])
        p2.append([row["P2"],ts])
    send_all_data("sensors.feinstaub.{}.P1".format(sensor_id),p1)
    send_all_data("sensors.feinstaub.{}.P2".format(sensor_id),p2)
