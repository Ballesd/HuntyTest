# TEST DE HUNTY

## Objetivos de la prueba

*Tu objetivo es crear y disponibilizar localmente un servicio API REST que permita realizar las 4
operaciones matemáticas básicas (Suma, Resta, Multiplicación y División) entre dos números que
ingresan como parámetros de la aplicación a través de peticiones HTTP. El servicio debe contar
con Swagger UI, estar Dockerizado y desplegado localmente en un servidor con sistema operativo
de distribución GNU/Linux (Puede ser una máquina virtual en tu PC). El código fuente del servicio
deberá ser almacenado en un repositorio privado de GitHub de tu elección.
Dejamos a tu criterio el lenguaje de programación sobre el que será construido el servicio, el
sistema operativo del servidor sobre el que será desplegado y la estructura de las peticiones
¡Sorprendenos!*

Levantar el contenedor y empezar a programar.

## Despliegue local del proyecto

**Todos estos comandos deben ser ejecutados en la raiz del proyecto**

* Cada vez que haga cambios al contenedor, debe construirlo nuevamente:
```
    docker compose build
```

* Levantar el contenedor: 
```  
    docker compose up
```