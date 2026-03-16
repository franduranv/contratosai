"""
ContratosAI - Generador de Contratos Legales para PyMEs mexicanas
"""
from anthropic import Anthropic
from enum import Enum

client = Anthropic()

class TipoContrato(Enum):
    PRESTACION_SERVICIOS = "prestacion_servicios"
    CONTRATO_LABORAL = "contrato_laboral"
    NDA = "nda"

SYSTEM_PROMPT = """Eres ContratosAI, un agente especializado en derecho mexicano que genera contratos legales para PyMEs.

Tienes conocimiento profundo de:
- Código Civil Federal de México
- Ley Federal del Trabajo (LFT)
- LFPDPPP (Ley de Protección de Datos)
- NOM-151 (firma electrónica)

IMPORTANTE: Siempre incluye al final:
"AVISO LEGAL: Este contrato fue generado con inteligencia artificial. ContratosAI no es un despacho de abogados. 
Para situaciones complejas o litigios, consulte con un abogado certificado."

Genera contratos completos, con cláusulas pertinentes para México, con [PLACEHOLDERS] para datos específicos."""

def generar_contrato(tipo: TipoContrato, datos: dict) -> str:
    """Genera un contrato legal completo"""
    
    prompts = {
        TipoContrato.PRESTACION_SERVICIOS: f"""Genera un Contrato de Prestación de Servicios Independientes completo para México.
        
Datos proporcionados: {datos}

Incluye: identificación de partes, descripción del servicio, contraprestación y forma de pago, 
duración, confidencialidad, propiedad intelectual, terminación, jurisdicción Ciudad de México.""",
        
        TipoContrato.CONTRATO_LABORAL: f"""Genera un Contrato Individual de Trabajo completo conforme a la Ley Federal del Trabajo de México.
        
Datos proporcionados: {datos}

Incluye: datos completos del trabajador y empleador, puesto y descripción, salario y forma de pago,
jornada laboral, todas las prestaciones de ley (IMSS, INFONAVIT, vacaciones, aguinaldo, prima vacacional),
duración, causas de rescisión conforme al Art. 47 LFT.""",
        
        TipoContrato.NDA: f"""Genera un Acuerdo de Confidencialidad (NDA) bilateral completo para México.
        
Datos proporcionados: {datos}

Incluye: definición exhaustiva de información confidencial, obligaciones de ambas partes,
excepciones a la confidencialidad, duración (mínimo 5 años), penalidades por incumplimiento,
fundamento en Código Civil Federal y LFPDPPP."""
    }
    
    mensaje = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompts[tipo]}]
    )
    return mensaje.content[0].text

if __name__ == "__main__":
    contrato = generar_contrato(
        TipoContrato.PRESTACION_SERVICIOS,
        {
            "prestador": "Juan Pérez García",
            "cliente": "Mi PyME SA de CV", 
            "servicio": "Desarrollo de software",
            "monto": "$50,000 MXN mensuales",
            "duracion": "6 meses"
        }
    )
    print(contrato)
