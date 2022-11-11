# IPP Exporter

Prometheus exporter for the Internet Printer Protocol (IPP)

## Docker Compose

```
---
services:
  app:
    image: paranerd/ipp-exporter
    container_name: ipp-exporter
    restart: unless-stopped
    ports:
      - 9101:80
```
