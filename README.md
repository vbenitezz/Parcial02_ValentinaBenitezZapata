En lugar de retornar el json, lo enviaría con la librería request al otro microservicio, así cada uno mantiene su función de forma independiente, uno se encarga de realizar el procesamiento y el otro de almacenar.

### Ejecutar:
docker compose up --build    
http://localhost:5000/respuesta_json/num
