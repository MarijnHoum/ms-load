Load service 
------------

Load service es servicio para fingir diferentes tipos de carga de un sistema web.

Es basado en el framework FastAPI.

Se puede utilizar en los siguienes maneras

* /noop : Haz nada. Retorna Null
* /anoop : Modelo asincrónica. Haz nada. Retorna Null

* /cpu/{seconds} : Carga un nucleo de computo durante n segundos. 
* /acpu/{seconds} : Modelo asincrónica. Carga un nucleo de computo durante n segundos, modo asyncronica.

* /wait/{seconds} : Espera durante N segundos.
* /await/{seconds} : Modelo asincrónica. Espera durante N segundos.

* /mem/{megabytes}/{seconds} : Ocupa N megabytes de memoria en el proceso durante una determinada cantidad de segundos.


# Performance results 

Installing wrk on linux
`$ sudo apt install wrk`

Running a test instance doing nothing. 
```shell
$ uvicorn main:app --port 8000
INFO:     Started server process [2143839]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Using work
```shell
$ wrk http://localhost:8000/noop 
Running 10s test @ http://localhost:8000/noop
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     3.01ms    1.31ms  28.74ms   95.31%
    Req/Sec     1.72k   173.99     1.94k    88.00%
  34232 requests in 10.00s, 4.18MB read
Requests/sec:   3421.55
Transfer/sec:    427.72KB
```

## Shortest response time 
Indicating the absolute minimum overhead of the FastAPI framework 

* Start Uvicorn with `$ uvicorn main:app --port 8000 --workers 1 --no-access-log` -- Just worker, no access-logs
* And wrk with `wrk -t 1 -c 1 http://localhost:8000/anoop` -- One thread, one connection.  
Gets an framework overhead time of 254µs or just under 4k requests per second per core. 
