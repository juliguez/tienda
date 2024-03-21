from enum import Enum

"""-------------------------------------------------------------------------------
# ENUMERACIONES
-------------------------------------------------------------------------------"""


class Tipo(Enum):

    PAPELERIA = 1 
    SUPERMECADO = 2
    FARMACIA = 3

class Producto:

    """-------------------------------------------------------------------------------
    # CONSTANTE 
    -------------------------------------------------------------------------------"""

    __IVA_PAPELERIA = 0.13
    __IVA_SUPERMERCADO = 0.18
    __IVA_FARMACIA = 0.16

    """-------------------------------------------------------------------------------
    # ATRIBUTOS 
    -------------------------------------------------------------------------------"""
    __nombre = None
    __tipo = Enum('Tipo',('PAPELERIA', 'SUPERMERCADO', 'FARMACIA'))
    __valorUnitario = 0.0
    __cantidadBodega = 0
    __cantidadMinima = 0
    __cantidadUnidadesVedidas = 0

    """-------------------------------------------------------------------------------
    # METODOS 
    -------------------------------------------------------------------------------"""

    def getNombre(self):
        return self.__nombre
    
    def getTipo(self):
        return self.__tipo
    
    def getvalorUnitario(self):
        return self.__valorUnitario
    
    def getcantidadBodega(self):
        return self.__cantidadBodega
    
    def getcantidadMinima(self):
        return self.__cantidadMinima
    
    def getcantidadUnidadesVedidas(self):
        return self.__cantidadUnidadesVedidas
    
    
    
    
    
