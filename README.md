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

sudo docker exec -t -i <containerId> bash

```

---

## Restaurants


### 1. Create

<ul>
    <li><strong>Endpoint</strong>: /api/restaurants/ </li>
    <li><strong>Request</strong>: POST</li>
    <li> <strong>Fields</strong>:
    <ul>
        <li>name: String</li>
        <li>location: String</li>
    </ul>
    </li>
</ul>

### 2. Read

<ul>
    <li><strong>Endpoint</strong>: /api/restaurants/{int:id} </li>
    <li><strong>Endpoint</strong>: /api/restaurants/{String:slug} </li>
    <li><strong>Request</strong>: GET</li>
    <li> <strong>Output</strong>:
    <ul>
        <li>id: int</li>
        <li>name: String</li>
        <li>slug: String</li>
        <li>location: String</li>
    </ul>
    </li>
</ul>

### 3. List

<ul>
    <li><strong>Endpoint</strong>: /api/restaurants/ </li>
    <li><strong>Request</strong>: GET</li>

</ul>

### 4. Update

<ul>
    <li><strong>Endpoint</strong>: /api/restaurants/{int:id} </li>
    <li><strong>Endpoint</strong>: /api/restaurants/{String:slug} </li>
    <li><strong>Request</strong>: PATCH</li>
    <li> <strong>Fields</strong> <i>(One or multiple)</i>:
    <ul>
        <li>name: String</li>
        <li>location: String</li>
    </ul>
    </li>
</ul>


### 5. Delete

<ul>
    <li><strong>Endpoint</strong>: /api/restaurants/{int:id} </li>
    <li><strong>Endpoint</strong>: /api/restaurants/{String:slug} </li>
    <li><strong>Request</strong>: DELETE</li>

</ul>

<hr/>

## Categories

### 1. Create

<ul>
    <li><strong>Endpoint</strong>: /api/categories/ </li>
    <li><strong>Request</strong>: POST</li>
    <li> <strong>Fields</strong>:
    <ul>
        <li>name: String</li>
    </ul>
    </li>
</ul>

### 2. Read

<ul>
    <li><strong>Endpoint</strong>: /api/categories/{int:id} </li>
    <li><strong>Endpoint</strong>: /api/categories/{String:slug} </li>
    <li><strong>Request</strong>: GET</li>
    <li> <strong>Output</strong>:
    <ul>
        <li>id: int</li>
        <li>name: String</li>
        <li>slug: String</li>
    </ul>
    </li>
</ul>

### 3. List

<ul>
    <li><strong>Endpoint</strong>: /api/categories/ </li>
    <li><strong>Request</strong>: GET</li>

</ul>

### 4. Update

<ul>
    <li><strong>Endpoint</strong>: /api/categories/{int:id} </li>
    <li><strong>Endpoint</strong>: /api/categories/{String:slug} </li>
    <li><strong>Request</strong>: PATCH</li>
    <li> <strong>Fields</strong> <i>(One or multiple)</i>:
    <ul>
        <li>name: String</li>
    </ul>
    </li>
</ul>


### 5. Delete

<ul>
    <li><strong>Endpoint</strong>: /api/categories/{int:id} </li>
    <li><strong>Endpoint</strong>: /api/categories/{String:slug} </li>
    <li><strong>Request</strong>: DELETE</li>

</ul>

<hr/>

## Products

### 1. Create

<ul>
    <li><strong>Endpoint</strong>: /api/products/ </li>
    <li><strong>Request</strong>: POST</li>
    <li> <strong>Fields</strong>:
    <ul>
        <li>categoryId: int</li>
        <li>restaurantId: int</li>
        <li>name: String</li>
        <li>price: float</li>
        <li>description: String</li>
        <li>imageUrl: Image</li>
    </ul>
    </li>
</ul>

### 2. Read

<ul>
    <li><strong>Endpoint</strong>: /api/products/{int:id} </li>
    <li><strong>Request</strong>: GET</li>
    <li> <strong>Output</strong>:
    <ul>
        <li>id: int</li>
        <li>categoryId: int</li>
        <li>restaurantId: int</li>
        <li>name: String</li>
        <li>price: float</li>
        <li>description: String</li>
        <li>imageUrl: String</li>
    </ul>
    </li>
</ul>

### 3. List

<ul>
    <li><strong>Endpoint</strong>: /api/products/ </li>
    <li><strong>Request</strong>: GET</li>

</ul>

### 4. Update

<ul>
    <li><strong>Endpoint</strong>: /api/products/{int:id} </li>
    <li><strong>Request</strong>: PATCH</li>
    <li> <strong>Fields</strong> <i>(One or multiple)</i>:
    <ul>
        <li>categoryId: int</li>
        <li>restaurantId: int</li>
        <li>name: String</li>
        <li>price: float</li>
        <li>description: String</li>
        <li>imageUrl: Image</li>
    </ul>
    </li>
</ul>


### 5. Delete

<ul>
    <li><strong>Endpoint</strong>: /api/products/{int:id} </li>
    <li><strong>Request</strong>: DELETE</li>

</ul>

<hr/>




