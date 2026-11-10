variable "nombre_contenedor" {
  description = "Nombre que tendrá el contenedor en Docker"
  type        = string
  default     = "servidor-web-nginx"
}

variable "puerto_externo" {
  description = "Puerto de tu computadora por el que accederás a Nginx"
  type        = number
  default     = 8080
}
