# Logging
Este modulo nos permite persistir los logs de nuestros programas en un archivo en especifico y discriminarlos por sus diferentes niveles de registro de Logs.

## Niveles de Registro de Logs.
|Level|NumericValue|
|---|------|
|NOTSET |0|
|DEBUG|10|
|INFO |20|
|WARNING|30|
|ERROR|40|
|CRITICAL|50|


## basicConfig
````level=logging.|DEBUG| INFO | WARNING | ERROR | CRITICAL```` nos dice el nivel que Logs que se va a usar para escrribir los logs en el documento, el nivel de registro de logs indica desde que nivel se van a registrar los logs, desde el incado hasta el 50. Si se especifica un nivel, se registrarán los logs de dicho nivel hasta el nivel 50.
