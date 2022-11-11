# IPP Exporter

[![build](https://github.com/paranerd/ipp-exporter/actions/workflows/main.yml/badge.svg)](https://github.com/paranerd/ipp-exporter/actions/workflows/main.yml)
[![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/paranerd/ipp-exporter?label=Current%20Version&logo=github)](https://github.com/paranerd/ipp-exporter/tags)
[![Docker Image Size (latest semver)](https://shields.api-test.nl:/docker/image-size/paranerd/ipp-exporter?label=Image%20Size&logo=docker)](https://hub.docker.com/repository/docker/paranerd/ipp-exporter)

Prometheus exporter for the Internet Printer Protocol (IPP)

## Docker Compose

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
