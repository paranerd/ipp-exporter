# IPP Exporter

[![build](https://github.com/paranerd/ipp-exporter/actions/workflows/main.yml/badge.svg)](https://github.com/paranerd/ipp-exporter/actions/workflows/main.yml)
[![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/paranerd/ipp-exporter?label=Current%20Version&logo=github)](https://github.com/paranerd/ipp-exporter/tags)
[![Docker Image Size (latest semver)](https://shields.api-test.nl:/docker/image-size/paranerd/ipp-exporter?label=Image%20Size&logo=docker)](https://hub.docker.com/repository/docker/paranerd/ipp-exporter)

Prometheus exporter for the Internet Printing Protocol (IPP)

## Run with Docker Run
```
docker run -d -p 9101:80 --name ipp-exporter paranerd/ipp-exporter
```

## Run with Docker Compose

```
---
version: '3'
services:
  ipp-exporter:
    image: paranerd/ipp-exporter
    container_name: ipp-exporter
    restart: unless-stopped
    ports:
      - 9101:80

```

## Query metrics
```
curl "<server_ip>:9101/probe?target=<printer_ipp_url_and_path>
```

## What's my printer's IPP URL?
The best option is to check the printer manual to find the path.

Here are the URLs for some of the major manufacturers:

- Canon: `ipp(s)://<Printer IP>/ipp/print`
- HP: `<Printer IP>:631/ipp/print`
- Kyocera: `<Printer IP>:631/ipp/lp1`

## Example output
```
# HELP busy If printer is currently busy
# TYPE busy gauge
busy 0
# HELP cartridge_level_percent Cartridge fill level by color
# TYPE cartridge_level_percent gauge
cartridge_level_percent{type="black"} 30
cartridge_level_percent{type="color"} 50
# HELP success Displays whether or not the probe was a success
# TYPE success gauge
success 1
```
