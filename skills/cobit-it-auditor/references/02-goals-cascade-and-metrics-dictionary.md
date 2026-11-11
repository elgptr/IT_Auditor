# Bab 2: Mekanisme Goals Cascade, Matriks Pemetaan Resmi (Figure A.1 & A.2), dan Kamus Metrik (EG & AG)

> **Sumber Otoritatif:** *COBIT® 2019 Framework: Introduction and Methodology (Section 4.6)* dan *COBIT® 2019 Framework: Governance and Management Objectives (Chapter 3.3 & Appendix A — Figure A.1 & Figure A.2, hlm. 297–298)*.

---

## 1. Arsitektur COBIT 2019 Goals Cascade

**Goals Cascade** adalah mekanisme penerjemahan kebutuhan pemangku kepentingan (*Stakeholder Needs*) menjadi tujuan korporat yang terukur, lalu diturunkan menjadi tujuan penyelarasan I&T, hingga akhirnya menetapkan prioritas pada **40 Governance and Management Objectives**.

```
[Kebutuhan & Penggerak Pemangku Kepentingan (Stakeholder Drivers & Needs)]
                                    |
                                    v
        [13 Enterprise Goals (EG01 - EG13) — 4 Dimensi BSC Korporat]
                                    |  (Matriks Figure A.1: P = Primary, S = Secondary)
                                    v
        [13 Alignment Goals (AG01 - AG13) — 4 Dimensi BSC Penyelarasan I&T]
                                    |  (Matriks Figure A.2: P = Primary, S = Secondary)
                                    v
   [40 Governance & Management Objectives (EDM01 - MEA04) & Target Capability]
```

### Dua Arah Penggunaan Goals Cascade bagi Auditor TI
1. **Top-Down (Perencanaan Audit Berbasis Strategi & Risiko — *Risk-Based Audit Planning*):**
   - Identifikasi 3–5 *Enterprise Goals* (`EG`) utama dari Rencana Jangka Panjang Perusahaan (RJPP) / Rencana Bisnis.
   - Petakan ke *Alignment Goals* (`AG`) yang memiliki hubungan **P (Primary)** dan **S (Secondary)** pada **Figure A.1**.
   - Turunkan ke *Governance & Management Objectives* yang memiliki hubungan **P (Primary)** pada **Figure A.2** untuk menentukan ruang lingkup audit TI (*Audit Universe Priority*) dan target *Capability Level*.
2. **Bottom-Up (Eskalasi Dampak Bisnis atas Temuan Teknis — *Business Risk Translation*):**
   - Ketika auditor menemukan kelemahan pada suatu praktik/objektif teknis (mis. kegagalan uji *restore backup* pada `DSS04`), telusuri ke atas melalui **Figure A.2** ke `AG` yang memiliki relasi **P** (`AG05`, `AG07`).
   - Telusuri lebih lanjut melalui **Figure A.1** ke `EG` yang memiliki relasi **P** (`EG01`, `EG02`, `EG06`).
   - Gunakan metrik resmi `AG` dan `EG` tersebut untuk mengartikulasikan elemen **Effect (Dampak Bisnis)** pada temuan audit berformat 5C di hadapan Direksi dan Komite Audit.

---

## 2. Kamus Lengkap 13 Enterprise Goals (EG01–EG13) & Metrik Indikator

| Kode EG | Dimensi BSC | Nama Resmi Enterprise Goal | Contoh Metrik Indikator Resmi (Example Metrics) |
| :--- | :--- | :--- | :--- |
| **`EG01`** | Financial | **Portfolio of competitive products and services** | • Percent of products and services that meet or exceed targets in revenues and/or market share<br>• Ratio of profitable products and services per life cycle phase<br>• Customer satisfaction with products and services modularity and integration<br>• Customer retention rate and market share growth |
| **`EG02`** | Financial | **Managed business risk** | • Percent of critical business objectives and services covered by risk assessment<br>• Ratio of significant incidents that were not identified in risk assessments vs. total incidents<br>• Frequency of updating risk profile |
| **`EG03`** | Financial | **Compliance with external laws and regulations** | • Cost of regulatory noncompliance, including settlements and fines<br>• Number of regulatory noncompliance issues causing public comment or negative publicity<br>• Number of noncompliance matters noted by regulators<br>• Number of regulatory noncompliance issues relating to contractual agreements with business partners |
| **`EG04`** | Financial | **Quality of financial information** | • Satisfaction survey of key stakeholders regarding the transparency, level of detail and accuracy of financial information<br>• Cost of regulatory noncompliance regarding financial information, including settlements and fines<br>• Number of regulatory noncompliance issues regarding financial information reported to the board or causing public comment |
| **`EG05`** | Customer | **Customer-oriented service culture** | • Number of customer service disruptions<br>• Percent of business stakeholders satisfied that customer service delivery meets agreed levels<br>• Number of customer complaints<br>• Trend of customer satisfaction survey results |
| **`EG06`** | Customer | **Business service continuity and availability** | • Number of customer service interruptions causing significant incidents<br>• Business cost of incidents<br>• Number of business processing hours lost due to unplanned service interruptions<br>• Percent of complaints as a function of committed service availability targets |
| **`EG07`** | Customer | **Quality of management information** | • Degree of board and executive satisfaction with decision-making information<br>• Number of incidents caused by incorrect business decisions based on flawed information<br>• Time to provide supporting information for effective business decisions<br>• Timeliness of management information |
| **`EG08`** | Internal | **Optimization of internal business process functionality** | • Satisfaction levels of board and executive management with business process capabilities<br>• Satisfaction levels of customers with service delivery capabilities<br>• Satisfaction levels of suppliers with supply chain capabilities |
| **`EG09`** | Internal | **Optimization of business process costs** | • Cost vs. achieved service level<br>• Satisfaction levels of board and executive management with cost of business processes<br>• Reduced cost per processed transaction |
| **`EG10`** | Internal | **Staff skills, motivation and productivity** | • Staff productivity compared to benchmarks<br>• Level of stakeholder satisfaction with staff expertise and skills<br>• Percent of staff whose skills are insufficient for the competency required for their role<br>• Percent of satisfied staff<br>• Staff turnover rate |
| **`EG11`** | Internal | **Compliance with internal policies** | • Number of incidents related to noncompliance with policy<br>• Percent of stakeholders who understand policies<br>• Percent of policies supported by effective standards and working practices<br>• Frequency of policies review and update |
| **`EG12`** | Growth | **Managed digital transformation programs** | • Number of programs on time and within budget<br>• Percent of stakeholders satisfied with program delivery<br>• Percent of business transformation programs stopped<br>• Percent of business transformation programs with regular reported status updates |
| **`EG13`** | Growth | **Product and business innovation** | • Level of awareness and understanding of business innovation opportunities and possibilities<br>• Stakeholder satisfaction with levels of product and innovation expertise and ideas<br>• Number of approved product and service initiatives resulting from innovative ideas<br>• Revenue or value growth attributable to new digital products and services |

---

## 3. Kamus Lengkap 13 Alignment Goals (AG01–AG13) & Metrik Indikator

| Kode AG | Dimensi BSC | Nama Resmi Alignment Goal | Contoh Metrik Indikator Resmi (Example Metrics) |
| :--- | :--- | :--- | :--- |
| **`AG01`** | Financial | **I&T compliance and support for business compliance with external laws and regulations** | • Cost of IT noncompliance, including settlements and fines, and the impact of reputational loss<br>• Number of IT-related noncompliance issues reported to the board, or causing public comment or embarrassment<br>• Number of noncompliance issues relating to contractual agreements with IT service providers<br>• Coverage of compliance assessments over I&T-related external laws and regulations |
| **`AG02`** | Financial | **Managed I&T-related risk** | • Frequency of update of risk profile<br>• Percent of enterprise risk assessments including I&T-related risk<br>• Number of significant I&T-related incidents that were not identified in a risk assessment |
| **`AG03`** | Financial | **Realized benefits from I&T-enabled investments and services portfolio** | • Percent of I&T-enabled investments for which claimed benefits in the business case are met or exceeded<br>• Percent of I&T services for which expected benefits (as stated in service level agreements) are realized |
| **`AG04`** | Financial | **Quality of technology-related financial information** | • Transparency of I&T costs, benefits and risk<br>• Percent of I&T-related investments with clearly defined and approved life cycle costs and benefits in business cases<br>• Satisfaction of key stakeholders regarding the accuracy, transparency and completeness of I&T financial information |
| **`AG05`** | Customer | **Delivery of I&T services in line with business requirements** | • Number of business disruptions due to IT service incidents<br>• Percent of business stakeholders satisfied that IT service delivery meets agreed service levels<br>• Percent of users satisfied with the quality of IT service delivery |
| **`AG06`** | Customer | **Agility to turn business requirements into operational solutions** | • Level of satisfaction of business executives with IT's responsiveness to new requirements<br>• Average time-to-market for new I&T-related services and applications<br>• Average time to turn strategic I&T objectives into an agreed and approved initiative<br>• Number of critical business processes supported by up-to-date infrastructure and applications |
| **`AG07`** | Internal | **Security of information, processing infrastructure and applications, and privacy** | • Number of confidentiality incidents causing financial loss, business disruption or public embarrassment<br>• Number of availability incidents causing financial loss, business disruption or public embarrassment<br>• Number of integrity incidents causing financial loss, business disruption or public embarrassment<br>• Time to identify and resolve security incidents<br>• Number of data privacy breaches reported to regulators or affected data subjects |
| **`AG08`** | Internal | **Enabling and supporting business processes by integrating applications and technology** | • Time to execute business process changes involving I&T<br>• Number of I&T-enabled business programs delayed or incurring additional cost due to technology integration issues<br>• Number of business process changes that need to be delayed or reworked because of technology integration issues<br>• Number of applications or critical infrastructures operating in silos and not integrated |
| **`AG09`** | Internal | **Delivering programs on time, on budget and meeting requirements and quality standards** | • Number of programs/projects on time and within budget<br>• Percent of stakeholders satisfied with program/project quality<br>• Number of programs needing significant rework due to quality defects<br>• Cost of application maintenance vs. overall IT cost |
| **`AG10`** | Internal | **Quality of I&T management information** | • Level of user satisfaction with quality and timeliness and availability of I&T management information<br>• Ratio and extent of erroneous business decisions where erroneous or unavailable I&T-related information was a key factor<br>• Percent of information elements meeting quality criteria (accuracy, completeness, currency, consistency) |
| **`AG11`** | Internal | **I&T compliance with internal policies** | • Number of incidents related to noncompliance with I&T-related policies<br>• Percent of stakeholders who understand I&T-related policies<br>• Percent of I&T-related policies supported by effective standards and working practices<br>• Frequency of I&T-related policies review and update |
| **`AG12`** | Growth | **Competent and motivated staff with mutual understanding of technology and business** | • Percent of IT-competent business staff vs. required<br>• Percent of business-competent IT staff vs. required<br>• Number of learning/training hours per staff member<br>• Turnover rate of I&T staff in key technical and business-interfacing roles |
| **`AG13`** | Growth | **Knowledge, expertise and initiatives for business innovation** | • Level of business executive awareness and understanding of I&T innovation possibilities<br>• Level of stakeholder satisfaction with levels of I&T innovation expertise and ideas<br>• Number of approved initiatives resulting from innovative I&T ideas |

---

## 4. Matriks Resmi Figure A.1: Pemetaan Enterprise Goals (EG) ke Alignment Goals (AG)

> **Keterangan:** **P** = *Primary Relationship* (Hubungan Kuat/Utama, bobot = 2), **S** = *Secondary Relationship* (Hubungan Sedang/Pendukung, bobot = 1), `.` = Tidak ada hubungan langsung.

| Kode AG & Nama Alignment Goal | `EG01` | `EG02` | `EG03` | `EG04` | `EG05` | `EG06` | `EG07` | `EG08` | `EG09` | `EG10` | `EG11` | `EG12` | `EG13` |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`AG01`** — I&T compliance and support for business compliance with external laws and regulations | . | **S** | **P** | . | . | . | . | . | . | . | **S** | . | . |
| **`AG02`** — Managed I&T-related risk | . | **P** | . | . | . | **S** | . | . | . | . | . | . | . |
| **`AG03`** — Realized benefits from I&T-enabled investments and services portfolio | **S** | . | . | . | **S** | . | . | **S** | **S** | . | . | **P** | . |
| **`AG04`** — Quality of technology-related financial information | . | . | . | **P** | . | . | **P** | . | **P** | . | . | . | . |
| **`AG05`** — Delivery of I&T services in line with business requirements | **P** | . | . | . | **S** | **S** | . | **S** | . | . | . | **S** | . |
| **`AG06`** — Agility to turn business requirements into operational solutions | **P** | . | . | . | **S** | . | . | **S** | . | . | . | **S** | **S** |
| **`AG07`** — Security of information, processing infrastructure and applications, and privacy | . | **P** | . | . | . | **P** | . | . | . | . | . | . | . |
| **`AG08`** — Enabling and supporting business processes by integrating applications and technology | **P** | . | . | . | **P** | . | . | **S** | . | **S** | . | **P** | **S** |
| **`AG09`** — Delivering programs on time, on budget and meeting requirements and quality standards | **P** | . | . | . | **S** | . | . | **S** | **S** | . | . | **P** | **S** |
| **`AG10`** — Quality of I&T management information | . | . | . | **P** | . | . | **P** | . | **S** | . | . | . | . |
| **`AG11`** — I&T compliance with internal policies | . | **S** | **P** | . | . | . | . | . | . | . | **P** | . | . |
| **`AG12`** — Competent and motivated staff with mutual understanding of technology and business | . | . | . | . | **S** | . | . | . | . | **P** | . | . | . |
| **`AG13`** — Knowledge, expertise and initiatives for business innovation | **P** | . | **S** | . | . | . | . | . | . | . | . | **S** | **P** |

---

## 5. Matriks Resmi Figure A.2: Pemetaan Alignment Goals (AG) ke 40 Governance & Management Objectives

> **Keterangan:** **P** = *Primary Relationship* (Hubungan Utama, bobot = 2), **S** = *Secondary Relationship* (Hubungan Sekunder, bobot = 1), `.` = Tidak ada hubungan langsung.

| Objektif COBIT 2019 | `AG01` | `AG02` | `AG03` | `AG04` | `AG05` | `AG06` | `AG07` | `AG08` | `AG09` | `AG10` | `AG11` | `AG12` | `AG13` |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`EDM01`** — Ensured Governance Framework Setting and Maintenance | **P** | **S** | **P** | . | . | . | . | **S** | . | . | **S** | . | . |
| **`EDM02`** — Ensured Benefits Delivery | . | . | **P** | . | **S** | **S** | . | **S** | . | . | . | . | **S** |
| **`EDM03`** — Ensured Risk Optimization | **S** | **P** | . | . | . | . | **P** | . | . | . | **S** | . | . |
| **`EDM04`** — Ensured Resource Optimization | . | . | **S** | . | **S** | **S** | . | **S** | **P** | . | . | **S** | . |
| **`EDM05`** — Ensured Stakeholder Engagement | . | . | . | **S** | . | . | . | . | . | **P** | **S** | . | . |
| **`APO01`** — Managed I&T Management Framework | **S** | **S** | **P** | . | **S** | . | **S** | **S** | **S** | **S** | **P** | . | . |
| **`APO02`** — Managed Strategy | . | . | **S** | . | **S** | **S** | . | **P** | . | . | . | **S** | **S** |
| **`APO03`** — Managed Enterprise Architecture | . | . | **S** | . | **S** | **P** | **S** | **P** | . | . | . | . | . |
| **`APO04`** — Managed Innovation | . | . | **S** | . | . | **P** | . | **S** | . | . | . | **S** | **P** |
| **`APO05`** — Managed Portfolio | . | . | **P** | . | **P** | **S** | . | **S** | **S** | . | . | . | . |
| **`APO06`** — Managed Budget and Costs | . | . | **S** | **P** | . | . | . | . | **P** | **S** | . | . | . |
| **`APO07`** — Managed Human Resources | . | . | **S** | . | **S** | . | . | . | **S** | . | . | **P** | **P** |
| **`APO08`** — Managed Relationships | . | . | **S** | . | **P** | **P** | . | **S** | **S** | . | . | **P** | **P** |
| **`APO09`** — Managed Service Agreements | . | . | . | . | **P** | . | . | **S** | . | . | . | . | . |
| **`APO10`** — Managed Vendors | . | . | . | . | **P** | **S** | . | . | **S** | . | . | . | . |
| **`APO11`** — Managed Quality | . | . | **S** | **S** | **S** | . | . | . | **P** | **P** | . | . | . |
| **`APO12`** — Managed Risk | . | **P** | . | . | . | . | **P** | . | . | . | . | . | . |
| **`APO13`** — Managed Security | **S** | **S** | . | . | . | . | **P** | . | . | . | . | . | . |
| **`APO14`** — Managed Data | **S** | **S** | . | **S** | . | . | **S** | . | . | **P** | . | . | . |
| **`BAI01`** — Managed Programs | . | . | **P** | . | . | **S** | . | **S** | **P** | . | . | . | . |
| **`BAI02`** — Managed Requirements Definition | . | . | **S** | . | **P** | **P** | . | **S** | **P** | . | . | **S** | . |
| **`BAI03`** — Managed Solutions Identification and Build | . | . | **S** | . | **P** | **P** | . | **S** | **P** | . | . | . | . |
| **`BAI04`** — Managed Availability and Capacity | . | . | . | . | **P** | . | **S** | . | **S** | . | . | . | . |
| **`BAI05`** — Managed Organizational Change | . | . | **P** | . | **S** | **S** | . | **P** | **P** | . | . | **S** | . |
| **`BAI06`** — Managed IT Changes | . | **S** | . | . | **S** | **P** | . | **S** | . | . | . | . | . |
| **`BAI07`** — Managed IT Change Acceptance and Transitioning | . | **S** | . | . | . | **P** | . | . | **S** | . | . | . | . |
| **`BAI08`** — Managed Knowledge | . | . | **S** | . | . | **S** | . | **S** | **S** | . | . | **P** | **P** |
| **`BAI09`** — Managed Assets | . | . | . | **P** | . | . | . | . | . | **S** | . | . | . |
| **`BAI10`** — Managed Configuration | . | . | . | . | **S** | . | **P** | . | . | . | . | . | . |
| **`BAI11`** — Managed Projects | . | . | **P** | . | **S** | **P** | . | . | **P** | . | . | . | . |
| **`DSS01`** — Managed Operations | . | . | . | . | **P** | . | . | **S** | . | . | . | . | . |
| **`DSS02`** — Managed Service Requests and Incidents | . | **S** | . | . | **P** | . | **S** | . | . | . | . | . | . |
| **`DSS03`** — Managed Problems | . | **S** | . | . | **P** | . | **S** | . | . | . | . | . | . |
| **`DSS04`** — Managed Continuity | . | **S** | . | . | **P** | . | **P** | . | . | . | . | . | . |
| **`DSS05`** — Managed Security Services | **S** | **P** | . | . | **S** | . | **P** | . | . | . | **S** | . | . |
| **`DSS06`** — Managed Business Process Controls | . | **S** | . | . | **S** | . | **S** | **P** | . | . | **S** | . | . |
| **`MEA01`** — Managed Performance and Conformance Monitoring | **S** | . | **S** | . | **P** | . | . | . | **S** | **P** | **S** | . | . |
| **`MEA02`** — Managed System of Internal Control | **S** | **S** | . | **S** | **S** | . | **S** | . | **S** | **S** | **P** | . | . |
| **`MEA03`** — Managed Compliance With External Requirements | **P** | . | . | . | . | . | . | . | . | . | **S** | . | . |
| **`MEA04`** — Managed Assurance | **S** | **S** | . | **S** | **S** | . | **S** | . | . | **S** | **P** | . | . |

---

## 6. Rumus Kuantitatif Perhitungan Skor Prioritas Cascade

Ketika organisasi memberikan bobot kepentingan $W(EG_i) \in [1..5]$ pada masing-masing *Enterprise Goal*, maka:

1. **Skor Kepentingan Alignment Goal ($S(AG_j)$):**
   $$S(AG_j) = \sum_{i=1}^{13} W(EG_i) \times M_1(AG_j, EG_i)$$
   di mana $M_1(AG_j, EG_i) = 2$ jika hubungan **P**, $1$ jika hubungan **S**, dan $0$ jika kosong.

2. **Skor Prioritas Governance/Management Objective ($S(OBJ_k)$):**
   $$S(OBJ_k) = \sum_{j=1}^{13} S(AG_j) \times M_2(OBJ_k, AG_j)$$
   di mana $M_2(OBJ_k, AG_j) = 2$ jika hubungan **P**, $1$ jika hubungan **S**, dan $0$ jika kosong.

3. **Penentuan Target Capability Level Berdasarkan Persentil Skor:**
   - **Persentil $\ge 80\%$ (Top Tier / Critical Priority):** Target **Capability Level 4** (*Predictable*)
   - **Persentil $50\% - 79\%$ (High Priority):** Target **Capability Level 3** (*Established*)
   - **Persentil $20\% - 49\%$ (Medium Priority):** Target **Capability Level 2** (*Managed*)
   - **Persentil $< 20\%$ (Baseline Priority):** Target **Capability Level 1** (*Performed*)

> [!TIP]
> Gunakan tool otomatis `python scripts/cobit_cli.py cascade --eg EG02,EG03,EG06` untuk menghitung secara instan peringkat seluruh *Alignment Goals* dan *40 Governance/Management Objectives* beserta rekomendasi target *Capability Level*-nya.
