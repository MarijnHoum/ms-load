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
