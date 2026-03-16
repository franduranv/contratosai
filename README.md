# 📄 ContratosAI

> Agente que genera contratos legales para PyMEs mexicanas en minutos

**Genera contratos legales profesionales en español mexicano con un formulario de 5 minutos.**

---

## ¿Qué es ContratosAI?

ContratosAI usa inteligencia artificial para generar contratos legales adaptados a la realidad jurídica mexicana. Sin abogados caros, sin plantillas genéricas de internet, sin traducir contratos gringos.

**Problema:** El 65% de las PyMEs mexicanas operan sin contratos formales. Los que los tienen usan plantillas desactualizadas o contratos copiados de internet que no tienen validez en México.

**Solución:** ContratosAI genera contratos en lenguaje legal mexicano correcto, adaptados a tu situación específica, listos para firmar en minutos.

---

## MVP — 3 Tipos de Contratos

### 1. Prestación de Servicios
El más común para freelancers, agencias, consultores y proveedores.
- Descripción del servicio
- Montos y forma de pago
- Plazos y entregables
- Propiedad intelectual
- Penalidades

### 2. NDA (Acuerdo de Confidencialidad)
Para proteger tu información antes de una reunión, negociación o partnership.
- Unilateral o bilateral
- Objeto de confidencialidad
- Duración y excepciones
- Penalidades

### 3. Contrato Laboral
Para contratación formal de empleados con prestaciones conforme a LFT.
- Puesto y descripción
- Salario y prestaciones (incluyendo superiores a ley)
- Jornada y modalidad (presencial/remoto/mixto)
- Confidencialidad y no competencia

---

## ¿Cómo funciona?

1. **Selecciona** el tipo de contrato que necesitas
2. **Llena el formulario** — preguntas específicas en lenguaje simple (5-10 min)
3. **Claude genera** el contrato completo en español legal mexicano
4. **Revisa** el preview antes de descargar
5. **Descarga el PDF** listo para firmar

---

## Tech Stack

| Capa | Tecnología |
|------|-----------|
| Frontend | Next.js 14 + TypeScript + Tailwind CSS |
| UI Components | shadcn/ui + React Hook Form |
| Backend | Next.js API Routes |
| Base de datos | Supabase (Postgres) |
| AI/LLM | Claude 3.5 Sonnet (Anthropic) |
| Generación PDF | @react-pdf/renderer |
| Firma electrónica | Mifiel (fase 2) |
| Deploy | Vercel |

### ¿Por qué Claude para contratos?
Claude tiene el mejor razonamiento en español legal de todos los LLMs. Genera cláusulas coherentes, sin redundancias, en el registro formal correcto del derecho mexicano.

---

## Estructura del Proyecto

```
contratosai/
├── app/
│   ├── page.tsx                          # Landing — selección de contrato
│   ├── generar/[tipo]/
│   │   ├── page.tsx                      # Formulario multi-step
│   │   └── resultado/page.tsx            # Preview + Descarga
│   └── api/
│       ├── generar/route.ts              # Generación con Claude
│       └── pdf/route.ts                  # Generación PDF
├── components/
│   ├── FormularioContrato.tsx
│   ├── PreviewContrato.tsx
│   └── DescargaPDF.tsx
├── lib/
│   ├── claude.ts
│   └── pdf-generator.ts
├── prompts/
│   ├── prestacion-servicios.ts
│   ├── nda.ts
│   └── contrato-laboral.ts
├── templates/
│   ├── prestacion-servicios.html
│   ├── nda.html
│   └── contrato-laboral.html
└── docs/
    ├── LFT-referencias.md
    └── clausulas-estandar.md
```

---

## Configuración

```bash
git clone https://github.com/franduranv/contratosai.git
cd contratosai
npm install
cp .env.example .env.local
npm run dev
```

### Variables de entorno

```env
ANTHROPIC_API_KEY=
NEXT_PUBLIC_SUPABASE_URL=
NEXT_PUBLIC_SUPABASE_ANON_KEY=
SUPABASE_SERVICE_ROLE_KEY=
MIFIEL_APP_ID=          # Fase 2 — firma electrónica
MIFIEL_APP_SECRET=      # Fase 2
```

---

## Roadmap

### v0.1 — MVP (48h)
- [x] Formularios multi-step para los 3 tipos
- [x] Generación con Claude
- [x] Preview HTML del contrato
- [x] Descarga PDF

### v0.2 — Beta
- [ ] Historial de contratos (cuenta de usuario)
- [ ] Firma electrónica con Mifiel (validez legal en México)
- [ ] Envío por email y WhatsApp
- [ ] Edición manual post-generación

### v1.0 — Producción
- [ ] Billing (Stripe)
- [ ] Más tipos: Arrendamiento, Compraventa, Sociedad Simple
- [ ] API para integradores (contadores, ERPs)
- [ ] Templates por industria

---

## Validez Legal

Los contratos generados por ContratosAI están basados en la legislación mexicana vigente:
- Código Civil Federal
- Ley Federal del Trabajo (LFT)
- Código de Comercio
- Ley Federal de Protección a la Propiedad Industrial

> **⚠️ Disclaimer:** ContratosAI es una herramienta de asistencia. Los contratos generados son una base sólida pero recomendamos la revisión de un abogado para casos complejos o de alto valor. ContratosAI no es un despacho jurídico.

---

## Parte de ZXY Ventures

ContratosAI es un proyecto de **[ZXY Ventures](https://zxy.vc)** — venture studio construyendo el futuro de las PyMEs mexicanas con AI.

**Contacto:** fran@zxy.vc

---

*Built with ❤️ in León, Guanajuato, México 🇲🇽*
