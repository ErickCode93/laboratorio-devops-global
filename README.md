# Laboratorio DevOps Global 🌍

Este repositorio contiene la arquitectura completa de un entorno integrado de microservicios, diseñado bajo estándares profesionales utilizando prácticas de **Infraestructura como Código (IaC)**, contenedores, orquestación y observabilidad distribuidos de forma quirúrgica para la separación de responsabilidades.

## 📂 Estructura del Ecosistema

*   **`01-docker/`**: Empaquetado y optimización de una API corporativa construida con FastAPI sobre imágenes ultra ligeras y seguras (Linux Alpine).
*   **`02-kubernetes/`**: Manifiestos de orquestación (`Deployment`, `Service`) configurados con Alta Disponibilidad (2 réplicas) y balanceo de carga.
*   **`04-terraform/`**: Automatización del aprovisionamiento del clúster y componentes base, garantizando la consistencia del entorno mediante la gestión de estado (`.tfstate`).

## 🛠️ Tecnologías Utilizadas
*   **FastAPI / Python 3.11** (Lógica de negocio)
*   **Docker** (Contenedorización portátil)
*   **Kubernetes / Minikube** (Orquestación y escalado dinámico)
*   **Terraform** (Aprovisionamiento automatizado de infraestructura)
