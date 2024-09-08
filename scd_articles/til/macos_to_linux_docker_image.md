

I keep forgetting that to build a Docker image on my Mac and push to GCP / GKE it needs 
to be built for a Linux architecture prior to being pushed.

```
docker buildx build --platform linux/amd64 -t TAG_NAME:VERSION .
```

### Date: 2024-09-07 Saturday