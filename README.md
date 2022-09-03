# Docker commands

- Building image

```bash

docker build --tag <name> .

```

- Running Container

```bash

docker run --publish 8000:8000 <name>

```

- Getting into container

```bash

docker exec -t -i <containerId> bash

```

---

# API Documentation

```bash
http://localhost:8000/api/schema/swagger-ui/
```