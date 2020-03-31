#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import math

class MainHandler(webapp2.RequestHandler):
    def post(self):
        distancia = self.request.get("edDistancia")
        tiempo = self.request.get("edTiempo")
        consumoMedio = self.request.get("edConsumoMedio")

        velocidadMedia = float(distancia) / int(tiempo)
        consumoTotal = (float(distancia) * float(consumoMedio)) / 100
        toret = True

        if math.isnan(float(distancia)) or len(distancia.strip()) == 0 or float(distancia) < 0:
            toret = False
        elif math.isnan(int(tiempo)) or len(tiempo.strip()) == 0 or int(tiempo) <= 0:
            toret = False
        elif math.isnan(float(consumoMedio)) or len(consumoMedio.strip()) == 0 or float(consumoMedio) < 0:
            toret = False

        if toret:
            self.response.write("Velocidad media: {0:.2f} km/h \nConsumo total: {1:.2f} l".format(velocidadMedia, consumoTotal))
        else:
            self.response.write("No se puede realizar el calculo")

app = webapp2.WSGIApplication([
    ('/consumo', MainHandler)
], debug=True)
