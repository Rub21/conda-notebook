

```
docker compose run --service-ports asdi bash
python3 -m http.server 8888
docker compose run --publish 8888:8888  asdi bash
jupyter lab --allow-root
```

