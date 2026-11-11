# Bab 7: Domain DSS (Deliver, Service and Support) — Objektif Manajemen (DSS01–DSS06)

> **Fokus Area:** *Management of Enterprise I&T — Operations, Incident & Service Requests, Problem Management, Continuity (BCP/DRP), Security Services & Business Process Controls*.
> Domain **DSS** berfokus pada pengiriman operasional dan dukungan layanan I&T sehari-hari, termasuk ketahanan layanan, penanganan insiden dan masalah, keamanan teknis, serta kontrol aplikasi bisnis.

---

## DSS01 — Managed Operations

- **Area:** Management | **Domain:** Deliver, Service and Support
- **Referensi Halaman Resmi (COBIT 2019 Framework):** hlm. 231–236
- **Deskripsi Resmi:** Coordinate and execute the activities and operational procedures required to deliver internal and outsourced I&T services. Include the execution of predefined standard operating procedures and the required monitoring activities.
- **Tujuan (Purpose Statement):** Deliver I&T operational product and service outcomes as planned.

### 1. Pemetaan Goals Cascade & Metrik Tujuan (DSS01)

| Kategori Tujuan | Kode | Nama Tujuan Resmi | Dimensi BSC | Hubungan | Contoh Metrik Indikator (KPI / KGI) |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **Enterprise Goal** | `EG01` | Portfolio of competitive products and services | Financial | **P** | • Percent of products and services that meet or exceed targets in revenues and/or market share<br>• Ratio of profitable products and services per life cycle phase |
| **Alignment Goal** | `AG05` | Delivery of I&T services in line with business requirements | Customer | **P** | • Number of business disruptions due to IT service incidents<br>• Percent of business stakeholders satisfied that IT service delivery meets agreed service levels |
| **Alignment Goal** | `AG08` | Enabling and supporting business processes by integrating applications and technology | Internal | **S** | • Time to execute business process changes involving I&T |

### 2. Komponen A: Praktik Proses, Metrik, Aktivitas & Level Kapabilitas (DSS01)

#### DSS01.01 — Perform operational procedures

> **Deskripsi Praktik:** Maintain and perform operational procedures and operational tasks reliably and consistently.

**Contoh Metrik Praktik (Example Metrics):**
- a. Number of incidents caused by operational problems
- b. Number of nonstandard operational procedures executed

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Develop and maintain operational procedures and related activities to support all delivered services. | **Level 2** |
| 2 | 2. Maintain a schedule of operational activities and perform the activities. | **Level 2** |
| 3 | 3. Verify that all data expected for processing are received and processed completely, accurately and in a timely manner. Deliver output in accordance with enterprise requirements. Support restart and reprocessing needs. Ensure that users are receiving the right outputs in a secure and timely manner. | **Level 3** |
| 4 | 4. Manage the performance and throughput of the scheduled activities. | **Level 4** |
| 5 | 5. Monitor incidents and problems dealing with operational procedures and take appropriate action to improve reliability of operational tasks performed. | **Level 5** |

**Standar & Panduan Terkait (Related Guidance):**
- CMMI Cybermaturity Platform, 2018 TP .SE Safeguard Operational Environment
- HITRUST CSF version 9, September 2017 09.01 Document Operating Procedures
- ISO/IEC 27002:2013/Cor.2:2015(E) 12.1 Operational procedures and responsibilities
- ITIL V3, 2011 Service Operation, 4.1 Event Management
- National Institute of Standards and Technology Special Publication
- 800-53, Revision 5 (Draft), August 2017
- 3.13 Physical and environmental protection (PE-13, PE-14, PE-15)
- Management Practice Example Metrics

#### DSS01.02 — Manage outsourced I&T services

> **Deskripsi Praktik:** Manage the operation of outsourced I&T services to maintain the protection of enterprise information and reliability of service delivery.

**Contoh Metrik Praktik (Example Metrics):**
- a. Number of specific/smart KPIs included in outsourcing contracts
- b. Frequency of failure by outsourcing partner to meet KPIs

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Ensure that the enterprise’s requirements for security of information processes adhere to contracts and SLAs with third parties hosting or providing services. | **Level 3** |
| 2 | 2. Ensure that the enterprise’s operational business and IT processing requirements and priorities for service delivery adhere to contracts and SLAs with third parties hosting or providing services. | **Level 3** |
| 3 | 3. Integrate critical internal IT management processes with those of outsourced service providers. This should cover, for example, performance and capacity planning, change management, configuration management, service request and incident management, problem management, security management, business continuity, and the monitoring of process performance and reporting. | **Level 3** |
| 4 | 4. Plan for independent audit and assurance of the operational environments of outsourced providers to confirm that agreed requirements are being adequately addressed. | **Level 4** |

**Standar & Panduan Terkait (Related Guidance):**
- ISF , The Standard of Good Practice for Information Security 2016 SC1.2 Outsourcing
- ISO/IEC 20000-1:2011(E) 4.2 Governance of processes operated by other parties
- Management Practice Example Metrics

#### DSS01.03 — Monitor I&T infrastructure

> **Deskripsi Praktik:** Monitor the I&T infrastructure and related events. Store sufficient chronological information in operations logs to reconstruct and review time sequences of operations and other activities surrounding or supporting operations.

**Contoh Metrik Praktik (Example Metrics):**
- a. Percent of critical operational event types covered by automatic detection systems
- b. Percent of infrastructure assets monitored based on service criticality and the relationship between configuration items and services that depend on them

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Log events. Identify the level of information to be recorded, based on a consideration of risk and performance. | **Level 2** |
| 2 | 2. Identify and maintain a list of infrastructure assets that need to be monitored, based on service criticality and the relationship between configuration items and services that depend on them. | **Level 3** |
| 3 | 3. Define and implement rules that identify and record threshold breaches and event conditions. Find a balance between generating spurious minor events and significant events so event logs are not overloaded with unnecessary information. | **Level 3** |
| 4 | 4. Produce event logs and retain them for an appropriate period to assist in future investigations. | **Level 3** |
| 5 | 5. Ensure that incident tickets are created in a timely manner when monitoring identified deviations from defined thresholds. | **Level 3** |
| 6 | 6. Establish procedures for monitoring event logs. Conduct regular reviews. | **Level 4** |

**Standar & Panduan Terkait (Related Guidance):**
- National Institute of Standards and Technology Special Publication
- 800-53, Revision 5 (Draft), August 2017
- 3.10 Maintenance (MA-2, MA-3)
- Management Practice Example Metrics

#### DSS01.04 — Manage the environment

> **Deskripsi Praktik:** Maintain measures for protection against environmental factors. Install specialized equipment and devices to monitor and control the environment.

**Contoh Metrik Praktik (Example Metrics):**
- a. Number of people trained to respond to environmental alarm procedures
- b. Number of risk scenarios defined for environmental threats

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Identify natural and man-made disasters that might occur in the area where the IT facilities are located. Assess the potential effect on the IT facilities. | **Level 2** |
| 2 | 2. Identify how I&T equipment, including mobile and off-site equipment, is protected against environmental threats. Ensure that the policy limits or excludes eating, drinking and smoking in sensitive areas, and prohibits storage of stationery and other supplies that pose a fire hazard within computer rooms. | **Level 2** |
| 3 | 3. Keep the IT sites and server rooms clean and in a safe condition at all times (i.e., no mess, no paper or cardboard boxes, no filled dustbins, no flammable chemicals or materials). | **Level 2** |
| 4 | 4. Situate and construct IT facilities to minimize and mitigate susceptibility to environmental threats (e.g., theft, air, fire, smoke, water, vibration, terror, vandalism, chemicals, explosives). Consider specific security zones and/or fireproof cells (e.g., locating production and development environments/servers away from each other). | **Level 3** |
| 5 | 5. Compare measures and contingency plans against insurance policy requirements and report results. Address points of noncompliance in a timely manner. | **Level 3** |
| 6 | 6. Respond to environmental alarms and other notifications. Document and test procedures, which should include prioritization of alarms and contact with local emergency response authorities. Train personnel in these procedures. | **Level 3** |
| 7 | 7. Regularly monitor and maintain devices that proactively detect environmental threats (e.g., fire, water, smoke, humidity). | **Level 4** |

**Standar & Panduan Terkait (Related Guidance):**
- National Institute of Standards and Technology Special Publication
- 800-37, Revision 2 (Draft), May 2018
- 2.1 System and system elements; 3.2 Categorization (Task 5, 6)
- Management Practice Example Metrics

#### DSS01.05 — Manage facilities

> **Deskripsi Praktik:** Manage facilities, including power and communications equipment, in line with laws and regulations, technical and business requirements, vendor specifications, and health and safety guidelines.

**Contoh Metrik Praktik (Example Metrics):**
- a. Time since last test of uninterruptible power supply
- b. Number of people trained on health and safety guidelines

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Examine the IT facilities’ requirement for protection against power fluctuations and outages, in conjunction with other business continuity planning requirements. Procure suitable uninterruptible supply equipment (e.g., batteries, generators) to support business continuity planning. | **Level 2** |
| 2 | 2. Regularly test the uninterruptible power supply’s mechanisms. Ensure that power can be switched to the supply without any significant effect on business operations. | **Level 2** |
| 3 | 3. Ensure that the facilities housing the I&T systems have more than one source for dependent utilities (e.g., power, telecommunications, water, gas). Separate the physical entrance of each utility. | **Level 2** |
| 4 | 4. Confirm that cabling external to the IT site is located underground or has suitable alternative protection. Determine that cabling within the IT site is contained within secured conduits, and access to wiring cabinets is restricted to authorized personnel. Properly protect cabling against damage caused by fire, smoke, water, interception and interference. | **Level 2** |
| 5 | 5. Ensure that cabling and physical patching (data and phone) are structured and organized. Cabling and conduit structures should be documented (e.g., blueprint building plan and wiring diagrams). | **Level 2** |
| 6 | 6. On regular basis, educate personnel on health and safety laws, regulations, and relevant guidelines. Educate personnel on fire and rescue drills to ensure knowledge and actions taken in case of fire or similar incidents. | **Level 2** |
| 7 | 7. Ensure that IT sites and equipment are maintained according to the supplier’s recommended service intervals and specifications. Ensure that maintenance is carried out only by authorized personnel. | **Level 3** |
| 8 | 8. Analyze the facilities housing’s high-availability systems for redundancy and fail-over cabling requirements (external and internal). | **Level 3** |
| 9 | 9. Ensure that IT sites and facilities are in ongoing compliance with relevant health and safety laws, regulations, guidelines, and vendor specifications. | **Level 3** |
| 10 | 10. Record, monitor, manage and resolve facilities incidents in line with the I&T incident management process. Make available reports on facilities incidents for which disclosure is required by laws and regulations. | **Level 4** |
| 11 | 11. Analyze physical alterations to IT sites or premises to reassess the environmental risk (e.g., fire or water damage). Report results of this analysis to business continuity and facilities management. | **Level 4** |

### 3. Komponen B: Struktur Organisasi & Matriks RACI (DSS01)

| Kode Praktik | Nama Praktik | Accountable (A) — Penanggung Jawab Tunggal | Responsible (R) — Pelaksana Operasional |
| :--- | :--- | :--- | :--- |
| `DSS01.01` | Perform operational procedures | **Chief Information Officer** | Chief Operating Officer, Head IT operations, Chief Technology Officer |
| `DSS01.02` | Manage outsourced I&T services | **Chief Information Officer** | Head IT operations, Information Security Manager, Privacy Officer, Chief Technology Officer |
| `DSS01.03` | Monitor I&T infrastructure | **Chief Technology Officer** | Chief Information Officer, Head IT operations, Information Security Manager |
| `DSS01.04` | Manage the environment | **Chief Technology Officer** | Chief Information Officer, Head IT operations, Information Security Manager |
| `DSS01.05` | Manage facilities | **Chief Technology Officer** | Chief Information Officer, Head IT operations, Information Security Manager |

### 4. Komponen C, D, E, F, dan G (DSS01)

- **Komponen C — Aliran & Item Informasi (Information Flows and Items):**
  - Ringkasan Input/Output Praktik: `(see also Section 3.6) ; Management Practice Inputs Outputs ; DSS01.01 Perform operational procedures. From Description Description To ; BAI05.05 Operation and use plan Backup log Internal ; Operational schedule Internal ; DSS01.02 Manage outsourced I&T services. APO09.03 • SLAs ; • OLAs ; Independent assurance ; plans ; MEA04.02 ; BAI05.05 Operation and use plan ; DSS01.03 Monitor I&T infrastructure. BAI03.11 Service definitions Asset monitoring rules ; and event conditions ; DSS02.01; ; DSS02.02 ; Incident tickets DSS02.02 ; Event logs Internal ; DSS01.04 Manage the environment. Environmental policies APO01.09`
- **Komponen D — SDM, Keterampilan & Kompetensi (People, Skills and Competencies — SFIA V6 / e-CF):**
  - Referensi Kompetensi: `Skill Related Guidance (Standards, Frameworks, Compliance Requirements) Detailed Reference | Database administration Skills Framework for the Information Age V6, 2015 DBAD | Facilities management Skills Framework for the Information Age V6, 2015 DCMA | IT infrastructure Skills Framework for the Information Age V6, 2015 ITOP | Methods and tools Skills Framework for the Information Age V6, 2015 METL | Service delivery e-Competence Framework (e-CF)—A common European Framework for ICT | Professionals in all industry sectors—Part 1: Framework, 2016 | C. Run—C.3. Service Delivery | Storage management Skills Framework for the Information Age V6, 2015 STMG`
- **Komponen E — Kebijakan & Prosedur (Policies and Procedures):**
  - Kebijakan Kunci: `Relevant Policy Policy Description Related Guidance Detailed Reference | Service management policy Provides direction and guidance to | ensure effective management and | implementation of all I&T services | to meet business and customer | requirements, within a framework | of performance measurement. | Covers management of risk | related to I&T services. (The ITIL | V3 framework offers detailed | guidance on service management | and optimization of risk related to`
- **Komponen F — Budaya, Etika & Perilaku (Culture, Ethics and Behavior):**
  - Elemen Budaya: `Key Culture Elements Related Guidance Detailed Reference | Create a culture of habitual excellence throughout the organization. | Encourage employees to excel. Create an environment in which | operational procedures deliver (more than) the necessary services while | also allowing employees to question the status quo and try new ideas. | Manage operational excellence through employee engagement and | continuous improvement. Apply a customer-centric approach (for both | internal and external customers).`
- **Komponen G — Layanan, Infrastruktur & Aplikasi (Services, Infrastructure and Applications):**
  - Cloud hosting services
  - Infrastructure monitoring tools
  - Service level monitoring tools

### 5. Program Kerja Audit TI (Kertas Kerja Audit / KKA) — DSS01

- **Fokus Pengujian Audit:** Pengelolaan Operasional TI (IT Operations): prosedur operasional harian, penjadwalan batch job, pemantauan infrastruktur, dan pengamanan fasilitas Data Center.
- **Daftar Permintaan Dokumen Bukti (PBC — *Provided by Client*):**
  1. SOP Operasional TI (Runbooks), jadwal dan log eksekusi batch jobs, serta laporan pemantauan NOC/infrastruktur.
  1. Log akses fisik Data Center/Server Room, catatan pemeliharaan perangkat pendukung (UPS, Genset, PAC/HVAC, Fire Suppression, CCTV).
  1. Kontrak dan laporan pemantauan operasional layanan terkelola (Managed Services / Cloud Infrastructure).
- **Prosedur Pengujian Kontrol (Test of Design / ToD & Test of Operating Effectiveness / ToE):**
  - ToD: Periksa kelengkapan SOP operasional, pemantauan otomatis 24/7, dan kontrol keamanan fisik/lingkungan fasilitas Data Center.
  - ToE: Uji sampel kegagalan batch job dan pastikan telah ditindaklanjuti; lakukan inspeksi fisik/virtual atas kontrol akses ruang server, suhu/kelembapan, uji beban genset/UPS, dan sistem pemadam kebakaran.
- **Indikator Temuan / Red Flags Audit:**
  - ⚠️ Kegagalan proses batch akhir hari (End-of-Day) tidak terdeteksi hingga pagi hari berikutnya karena tidak adanya alert otomatis.
  - ⚠️ Ruang server/Data Center dapat diakses oleh pihak tidak berwenang tanpa log akses, atau tabung pemadam/UPS sudah kedaluwarsa masa ujinya.

---

## DSS02 — Managed Service Requests and Incidents

- **Area:** Management | **Domain:** Deliver, Service and Support
- **Referensi Halaman Resmi (COBIT 2019 Framework):** hlm. 237–242
- **Deskripsi Resmi:** Provide timely and effective response to user requests and resolution of all types of incidents. Restore normal service; record and fulfil user requests; and record, investigate, diagnose, escalate and resolve incidents.
- **Tujuan (Purpose Statement):** Achieve increased productivity and minimize disruptions through quick resolution of user queries and incidents. Assess the impact of changes and deal with service incidents. Resolve user requests and restore service in response to incidents.

### 1. Pemetaan Goals Cascade & Metrik Tujuan (DSS02)

| Kategori Tujuan | Kode | Nama Tujuan Resmi | Dimensi BSC | Hubungan | Contoh Metrik Indikator (KPI / KGI) |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **Enterprise Goal** | `EG01` | Portfolio of competitive products and services | Financial | **P** | • Percent of products and services that meet or exceed targets in revenues and/or market share<br>• Ratio of profitable products and services per life cycle phase |
| **Alignment Goal** | `AG02` | Managed I&T-related risk | Financial | **S** | • Frequency of update of risk profile |
| **Alignment Goal** | `AG05` | Delivery of I&T services in line with business requirements | Customer | **P** | • Number of business disruptions due to IT service incidents<br>• Percent of business stakeholders satisfied that IT service delivery meets agreed service levels |
| **Alignment Goal** | `AG07` | Security of information, processing infrastructure and applications, and privacy | Internal | **S** | • Number of confidentiality incidents causing financial loss, business disruption or public embarrassment |

### 2. Komponen A: Praktik Proses, Metrik, Aktivitas & Level Kapabilitas (DSS02)

#### DSS02.01 — Define classification schemes for incidents and service requests

> **Deskripsi Praktik:** Define classification schemes and models for incidents and service requests.

**Contoh Metrik Praktik (Example Metrics):**
- a. Total number of service requests and incidents per priority level
- b. Total number of incidents escalated

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Define incident and service request classification and prioritization schemes, and criteria for problem registration. Use this information to ensure consistent approaches for handling and informing users about problems and conducting trend analysis. | **Level 3** |
| 2 | 2. Define incident models for known errors to enable efficient and effective resolution. | **Level 3** |
| 3 | 3. Define service request models according to service request type to enable self-help and efficient service for standard requests. | **Level 3** |
| 4 | 4. Define incident escalation rules and procedures, especially for major incidents and security incidents. | **Level 3** |
| 5 | 5. Define knowledge sources on incidents and requests and describe how to use them. | **Level 3** |

**Standar & Panduan Terkait (Related Guidance):**
- CMMI Cybermaturity Platform, 2018 IA.IP Implement Incident Investigation Processes
- HITRUST CSF version 9, September 2017 11.01 Reporting Information Security Incidents and Weaknesses
- ISF , The Standard of Good Practice for Information Security 2016 TM2 Security Incident Management
- ISO/IEC 20000-1:2011(E) 8.1 Incident and service request management
- ISO/IEC 27002:2013/Cor.2:2015(E) 16. Information security incident management
- Management Practice Example Metrics

#### DSS02.02 — Record, classify and prioritize requests and incidents

> **Deskripsi Praktik:** Identify, record and classify service requests and incidents and assign a priority according to business criticality and service agreements.

**Contoh Metrik Praktik (Example Metrics):**
- a. Number of types and categories defined for recording service requests and incidents
- b. Number of service requests and incidents that are not categorized

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Log all service requests and incidents, recording all relevant information, so they can be handled effectively and a full historical record can be maintained. | **Level 2** |
| 2 | 2. To enable trend analysis, classify service requests and incidents by identifying type and category. | **Level 2** |
| 3 | 3. Prioritize service requests and incidents based on the SLA service definition of business impact and urgency. | **Level 2** |

**Standar & Panduan Terkait (Related Guidance):**
- Management Practice Example Metrics

#### DSS02.03 — Verify, approve and fulfill service requests

> **Deskripsi Praktik:** Select the appropriate request procedures and verify that the service requests fulfill defined request criteria. Obtain approval, if required, and fulfill the requests.

**Contoh Metrik Praktik (Example Metrics):**
- a. Mean elapsed time for handling each type of service request
- b. Percent of service requests that fulfill defined request criteria

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Verify entitlement for service requests using, where possible, a predefined process flow and standard changes. | **Level 2** |
| 2 | 2. Obtain financial and functional approval or sign-off, if required, or predefined approvals for agreed standard changes. | **Level 2** |
| 3 | 3. Fulfill the requests by performing the selected request procedure. Where possible, use self-help automated menus and predefined request models for frequently requested items. | **Level 3** |

**Standar & Panduan Terkait (Related Guidance):**
- ITIL V3, 2011 Service Operation, 4.3 Request Fulfilment
- Management Practice Example Metrics

#### DSS02.04 — Investigate, diagnose and allocate incidents

> **Deskripsi Praktik:** Identify and record incident symptoms, determine possible causes, and allocate for resolution.

**Contoh Metrik Praktik (Example Metrics):**
- a. Number of identified and recorded incident symptoms
- b. Number of correctly determined symptom causes
- c. Number of duplicate problems in the reference log

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Identify and describe relevant symptoms to establish the most probable causes of the incidents. Reference available knowledge resources (including known errors and problems) to identify possible incident resolutions (temporary workarounds and/or permanent solutions). | **Level 2** |
| 2 | 2. If a related problem or known error does not already exist and if the incident satisfies agreed criteria for problem registration, log a new problem. | **Level 2** |
| 3 | 3. Assign incidents to specialist functions if deeper expertise is needed. Engage the appropriate level of management, where and if needed. | **Level 2** |

**Standar & Panduan Terkait (Related Guidance):**
- Management Practice Example Metrics

#### DSS02.05 — Resolve and recover from incidents

> **Deskripsi Praktik:** Document, apply and test the identified solutions or workarounds. Perform recovery actions to restore the I&T-related service.

**Contoh Metrik Praktik (Example Metrics):**
- a. Percent of incidents resolved within agreed SLA
- b. Percent of stakeholder satisfaction with resolution and recovery from incident

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Select and apply the most appropriate incident resolutions (temporary workaround and/or permanent solution). | **Level 2** |
| 2 | 2. Record whether workarounds were used for incident resolution. | **Level 2** |
| 3 | 3. Perform recovery actions, if required. | **Level 2** |
| 4 | 4. Document incident resolution and assess if the resolution can be used as a future knowledge source. | **Level 2** |

**Standar & Panduan Terkait (Related Guidance):**
- ITIL V3, 2011 Service Operation, 4.2 Incident Management
- National Institute of Standards and Technology Framework for Improving
- Critical Infrastructure Cybersecurity v1.1, April 2018
- RC.RP Recovery Planning
- National Institute of Standards and Technology Special Publication
- 800-53, Revision 5 (Draft), August 2017
- 3.9 Incident response (IR-4, IR-5, IR-6)
- The CIS Critical Security Controls for Effective Cyber Defense Version
- 6.1, August 201
- CSC 19: Incident Response and Management
- Management Practice Example Metrics

#### DSS02.06 — Close service requests and incidents

> **Deskripsi Praktik:** Verify satisfactory incident resolution and/or fulfilment of requests, and close.

**Contoh Metrik Praktik (Example Metrics):**
- a. Level of user satisfaction with service request fulfilment
- b. Percent of incidents resolved within an agreed/acceptable period of time

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Verify with the affected users that the service request has been fulfilled satisfactorily or the incident has been resolved satisfactorily and within an agreed/acceptable period of time. | **Level 2** |
| 2 | 2. Close service requests and incidents. | **Level 2** |

**Standar & Panduan Terkait (Related Guidance):**
- Management Practice Example Metrics

#### DSS02.07 — Track status and produce reports

> **Deskripsi Praktik:** Regularly track, analyze and report incidents and fulfilment of requests. Examine trends to provide information for continual improvement.

**Contoh Metrik Praktik (Example Metrics):**
- a. Mean time between incidents for the I&T -enabled service
- b. Number and percent of incidents causing disruption to business-critical processes

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Monitor and track incident escalations and resolutions and request handling procedures to progress toward resolution or completion. | **Level 2** |
| 2 | 2. Identify information stakeholders and their needs for data or reports. Identify reporting frequency and medium. | **Level 2** |
| 3 | 3. Produce and distribute timely reports or provide controlled access to online data. | **Level 4** |
| 4 | 4. Analyze incidents and service requests by category and type. Establish trends and identify patterns of recurring issues, SLA breaches or inefficiencies. | **Level 4** |
| 5 | 5. Use the information as input to continual improvement planning. | **Level 5** |

**Standar & Panduan Terkait (Related Guidance):**
- CMMI Cybermaturity Platform, 2018 MI.IM Ensure Incident Mitigation; IR.IR Incident Reporting
- National Institute of Standards and Technology Special Publication
- 800-53, Revision 5 (Draft), August 2017
- 3.9 Incident response (IR-7, IR-8)

### 3. Komponen B: Struktur Organisasi & Matriks RACI (DSS02)

| Kode Praktik | Nama Praktik | Accountable (A) — Penanggung Jawab Tunggal | Responsible (R) — Pelaksana Operasional |
| :--- | :--- | :--- | :--- |
| `DSS02.01` | Define classification schemes for incidents and service requests | **Chief Technology Officer** | Head Development, Head IT operations, Service Manager |
| `DSS02.02` | Record, classify and prioritize requests and incidents | **Chief Technology Officer** | Head IT operations, Service Manager |
| `DSS02.03` | Verify, approve and fulfill service requests | **Chief Technology Officer** | Business Process Owners, Head Development, Head IT operations, Service Manager |
| `DSS02.04` | Investigate, diagnose and allocate incidents | **Chief Technology Officer** | Business Process Owners, Head IT operations, Service Manager |
| `DSS02.05` | Resolve and recover from incidents | **Chief Technology Officer** | Head Development, Head IT operations, Service Manager, Information Security Manager |
| `DSS02.06` | Close service requests and incidents | **Chief Technology Officer** | Head IT operations, Service Manager, Information Security Manager |
| `DSS02.07` | Track status and produce reports | **Chief Technology Officer** | Head IT operations, Service Manager |

### 4. Komponen C, D, E, F, dan G (DSS02)

- **Komponen C — Aliran & Item Informasi (Information Flows and Items):**
  - Ringkasan Input/Output Praktik: `(see also Section 3.6) ; Management Practice Inputs Outputs ; DSS02.01 Define classification schemes for incidents ; and service requests. ; From Description Description To ; APO09.03 SLAs Criteria for problem ; registration ; DSS03.01 ; BAI10.02 Configuration repository Rules for incident ; escalation ; Internal ; BAI10.03 Updated repository with ; configuration items ; Incident and service ; request classification ; schemes and models ; Internal ; BAI10.04 Configuration status`
- **Komponen D — SDM, Keterampilan & Kompetensi (People, Skills and Competencies — SFIA V6 / e-CF):**
  - Referensi Kompetensi: `Skill Related Guidance (Standards, Frameworks, Compliance Requirements) Detailed Reference | Application support Skills Framework for the Information Age V6, 2015 ASUP | Customer service support Skills Framework for the Information Age V6, 2015 CSMG | Incident management Skills Framework for the Information Age V6, 2015 USUP | Network support Skills Framework for the Information Age V6, 2015 NTAS | User support e-Competence Framework (e-CF)—A common European Framework for ICT | Professionals in all industry sectors—Part 1: Framework, 2016 | C. Run—C.1. User Support`
- **Komponen E — Kebijakan & Prosedur (Policies and Procedures):**
  - Kebijakan Kunci: `Relevant Policy Policy Description Related Guidance Detailed Reference | Service request policy States rationale and provides | guidance for service and incident | requests and their documentation. | ITIL V3, 2011 Service Operation, 3. Service | operation principles`
- **Komponen F — Budaya, Etika & Perilaku (Culture, Ethics and Behavior):**
  - Elemen Budaya: `Key Culture Elements Related Guidance Detailed Reference | Enable employees to identify incidents on a correct and timely basis and | implement appropriate escalation paths. Encourage prevention. Respond | to and resolve incidents immediately. Avoid a hero culture.`
- **Komponen G — Layanan, Infrastruktur & Aplikasi (Services, Infrastructure and Applications):**
  - Incident tracking tools and system

### 5. Program Kerja Audit TI (Kertas Kerja Audit / KKA) — DSS02

- **Fokus Pengujian Audit:** Pengelolaan Permintaan Layanan dan Insiden TI (Service Request & Incident Management): pencatatan, klasifikasi, eskalasi, resolusi, dan penutupan tiket.
- **Daftar Permintaan Dokumen Bukti (PBC — *Provided by Client*):**
  1. SOP Manajemen Insiden & Permintaan Layanan (termasuk matriks prioritas/severity dan jalur eskalasi Major Incident).
  1. Data ekspor seluruh tiket insiden dan service request dari aplikasi ITSM/Service Desk selama periode audit.
  1. Laporan Major Incident Review (Post-Mortem) dan metrik Mean Time to Detect (MTTD) / Mean Time to Resolve (MTTR).
- **Prosedur Pengujian Kontrol (Test of Design / ToD & Test of Operating Effectiveness / ToE):**
  - ToD: Evaluasi prosedur klasifikasi, prioritisasi, dan eskalasi insiden (termasuk integrasi dengan protokol respons insiden keamanan siber).
  - ToE: Analisis populasi tiket insiden untuk menguji tingkat kepatuhan SLA resolusi, ketepatan waktu eskalasi Major Incident, dan konfirmasi pengguna sebelum tiket ditutup.
- **Indikator Temuan / Red Flags Audit:**
  - ⚠️ Insiden dilaporkan lewat chat pribadi (WhatsApp/grup chat) tanpa dicatat di sistem ITSM sehingga jejak audit dan statistik SLA menjadi bias.
  - ⚠️ Tiket insiden ditutup secara sepihak oleh teknisi demi mengejar target SLA padahal gangguan belum tuntas teratasi.

---

## DSS03 — Managed Problems

- **Area:** Management | **Domain:** Deliver, Service and Support
- **Referensi Halaman Resmi (COBIT 2019 Framework):** hlm. 243–248
- **Deskripsi Resmi:** Identify and classify problems and their root causes. Provide timely resolution to prevent recurring incidents. Provide recommendations for improvements.
- **Tujuan (Purpose Statement):** Increase availability, improve service levels, reduce costs, improve customer convenience and satisfaction by reducing the number of operational problems, and identify root causes as part of problem resolution.

### 1. Pemetaan Goals Cascade & Metrik Tujuan (DSS03)

| Kategori Tujuan | Kode | Nama Tujuan Resmi | Dimensi BSC | Hubungan | Contoh Metrik Indikator (KPI / KGI) |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **Enterprise Goal** | `EG01` | Portfolio of competitive products and services | Financial | **P** | • Percent of products and services that meet or exceed targets in revenues and/or market share<br>• Ratio of profitable products and services per life cycle phase |
| **Alignment Goal** | `AG02` | Managed I&T-related risk | Financial | **S** | • Frequency of update of risk profile |
| **Alignment Goal** | `AG05` | Delivery of I&T services in line with business requirements | Customer | **P** | • Number of business disruptions due to IT service incidents<br>• Percent of business stakeholders satisfied that IT service delivery meets agreed service levels |
| **Alignment Goal** | `AG07` | Security of information, processing infrastructure and applications, and privacy | Internal | **S** | • Number of confidentiality incidents causing financial loss, business disruption or public embarrassment |

### 2. Komponen A: Praktik Proses, Metrik, Aktivitas & Level Kapabilitas (DSS03)

#### DSS03.01 — Identify and classify problems

> **Deskripsi Praktik:** Define and implement criteria and procedures to identify and report problems. Include problem classification, categorization and prioritization.

**Contoh Metrik Praktik (Example Metrics):**
- a. Percent of major incidents for which problems were logged
- b. Percent of incidents solved in accordance with agreed SLAs
- c. Percent of problems appropriately identified, including classification, categorization and prioritization

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Identify problems through the correlation of incident reports, error logs and other problem identification resources. | **Level 2** |
| 2 | 2. Handle all problems formally with access to all relevant data. Include information from the IT change management system and IT configuration/asset and incident details. | **Level 2** |
| 3 | 3. Define appropriate support groups to assist with problem identification, root cause analysis and solution determination to support problem management. Determine support groups based on predefined categories, such as hardware, network, software, applications and support software. | **Level 2** |
| 4 | 4. Define priority levels through consultation with the business to ensure that problem identification and root cause analysis are handled in a timely manner according to the agreed SLAs. Base priority levels on business impact and urgency. | **Level 2** |
| 5 | 5. Report the status of identified problems to the service desk so customers and IT management can be kept informed. | **Level 2** |
| 6 | 6. Maintain a single problem management catalog to register and report problems identified. Use the catalog to establish audit trails of the problem management processes, including the status of each problem (i.e., open, reopen, in progress or closed). | **Level 2** |

**Standar & Panduan Terkait (Related Guidance):**
- ISO/IEC 20000-1:2011(E) 8.2 Problem management
- Management Practice Example Metrics

#### DSS03.02 — Investigate and diagnose problems

> **Deskripsi Praktik:** Investigate and diagnose problems using relevant subject matter experts to assess and analyze root causes.

**Contoh Metrik Praktik (Example Metrics):**
- a. Number of identified problems classified as known errors
- b. Percent of problems investigated and diagnosed throughout their life cycle

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Identify problems that may be known errors by comparing incident data with the database of known and suspected errors (e.g., those communicated by external vendors). Classify problems as known errors. | **Level 3** |
| 2 | 2. Associate the affected configuration items to the established/known error. | **Level 3** |
| 3 | 3. Produce reports to communicate the progress in resolving problems and to monitor the continuing impact of problems not solved. Monitor the status of the problem-handling process throughout its life cycle, including input from IT change and configuration management. | **Level 3** |

**Standar & Panduan Terkait (Related Guidance):**
- Management Practice Example Metrics

#### DSS03.03 — Raise known errors

> **Deskripsi Praktik:** As soon as root causes of problems are identified, create known-error records, document appropriate workarounds and identify potential solutions.

**Contoh Metrik Praktik (Example Metrics):**
- a. Number of problems with satisfactory resolution that addressed root causes
- b. Percent of stakeholder satisfaction with identification of root causes, creation of known-error records and appropriate workarounds, and identification of potential solutions

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. As soon as the root causes of problems are identified, create known-error records and develop a suitable workaround. | **Level 2** |
| 2 | 2. Identify, evaluate, prioritize and process (via IT change management) solutions to known errors, based on a cost/benefit business case and business impact and urgency. | **Level 3** |

**Standar & Panduan Terkait (Related Guidance):**
- Management Practice Example Metrics

#### DSS03.04 — Resolve and close problems

> **Deskripsi Praktik:** Identify and initiate sustainable solutions addressing the root cause. Raise change requests via the established change management process, if required, to resolve errors. Ensure that the personnel affected are aware of the actions taken and the plans developed to prevent future incidents from occurring.

**Contoh Metrik Praktik (Example Metrics):**
- a. Decrease in number of recurring incidents caused by unresolved problems
- b. Percent of workarounds defined for open problems

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Close problem records either after confirmation of successful elimination of the known error or after agreement with the business on how to alternatively handle the problem. | **Level 2** |
| 2 | 2. Inform the service desk of the schedule for problem closure (e.g., the schedule for fixing the known errors, the possible workaround or the fact that the problem will remain until the change is implemented) and the consequences of the approach taken. Keep affected users and customers informed as appropriate. | **Level 2** |
| 3 | 3. Throughout the resolution process, obtain regular reports from IT change management on progress in resolving problems and errors. | **Level 3** |
| 4 | 4. Monitor the continuing impact of problems and known errors on services. | **Level 4** |
| 5 | 5. Review and confirm the success of resolutions of major problems. | **Level 4** |
| 6 | 6. Make sure the knowledge learned from the review is incorporated into a service review meeting with the business customer. | **Level 5** |

**Standar & Panduan Terkait (Related Guidance):**
- Management Practice Example Metrics

#### DSS03.05 — Perform proactive problem management

> **Deskripsi Praktik:** Collect and analyze operational data (especially incident and change records) to identify emerging trends that may indicate problems. Log problem records to enable assessment.

**Contoh Metrik Praktik (Example Metrics):**
- a. Percent of problems logged as part of the proactive problem management activity
- b. Percent of key stakeholder satisfaction with the communication of problem information related to IT changes and incidents

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Capture problem information related to I&T changes and incidents and communicate it to key stakeholders. Communicate via reports and periodic meetings among incident, problem, change and configuration management process owners to consider recent problems and potential corrective actions. | **Level 3** |
| 2 | 2. Ensure that process owners and managers from incident, problem, change and configuration management meet regularly to discuss known problems and future planned changes. | **Level 3** |
| 3 | 3. Identify and initiate sustainable solutions (permanent fixes) addressing the root cause. Raise change requests via the established change management processes. | **Level 3** |
| 4 | 4. To enable the enterprise to monitor the total costs of problems, capture change efforts resulting from problem management process activities (e.g., fixes to problems and known errors) and report on them. | **Level 4** |
| 5 | 5. Produce reports to monitor problem resolution against the business requirements and SLAs. Ensure the proper escalation of problems, such as escalating to a higher management level according to agreed criteria, contacting external vendors, or referring to the change advisory board to increase the priority of an urgent request for change (RFC) to implement a temporary workaround. | **Level 4** |
| 6 | 6. To optimize the use of resources and reduce workarounds, track problem trends. | **Level 4** |

**Standar & Panduan Terkait (Related Guidance):**
- CMMI Cybermaturity Platform, 2018 MI.IC Ensure Incident Containment
- ITIL V3, 2011 Service Operation, 4.4 Problem Management

### 3. Komponen B: Struktur Organisasi & Matriks RACI (DSS03)

| Kode Praktik | Nama Praktik | Accountable (A) — Penanggung Jawab Tunggal | Responsible (R) — Pelaksana Operasional |
| :--- | :--- | :--- | :--- |
| `DSS03.01` | Identify and classify problems | **Chief Technology Officer** | Chief Information Officer, Head Development, Head IT operations, Service Manager |
| `DSS03.02` | Investigate and diagnose problems | **Chief Technology Officer** | Head IT operations, Service Manager, Information Security Manager |
| `DSS03.03` | Raise known errors | **Chief Technology Officer** | Head IT operations, Service Manager, Information Security Manager |
| `DSS03.04` | Resolve and close problems | **Chief Technology Officer** | Head IT operations, Service Manager |
| `DSS03.05` | Perform proactive problem management | **Chief Technology Officer** | Head IT operations, Service Manager, Executive Committee |

### 4. Komponen C, D, E, F, dan G (DSS03)

- **Komponen C — Aliran & Item Informasi (Information Flows and Items):**
  - Ringkasan Input/Output Praktik: `(see also Section 3.6) ; Management Practice Inputs Outputs ; DSS03.01 Identify and classify problems. From Description Description To ; APO12.06 Risk-related root causes Problem classification ; scheme ; DSS02.01 ; DSS02.01 Criteria for problem ; registration ; Problem status reports DSS02.07 ; DSS02.04 Problem log Problem register Internal ; DSS03.02 Investigate and diagnose problems. APO12.06 Risk-related root causes Problem resolution reports DSS02.07 ; Root causes of problems Internal; ; DSS03.05 ; DSS03.03 Raise known errors. APO12.06 Risk-related root causes Proposed solutions to ; known errors ; BAI06.01 ; DSS02.05 Incident resolutions Known error records DSS02.05 ; DSS03.04 Resolve and close problems. DSS02.05 Incident resolutions Communication of`
- **Komponen D — SDM, Keterampilan & Kompetensi (People, Skills and Competencies — SFIA V6 / e-CF):**
  - Referensi Kompetensi: `Skill Related Guidance (Standards, Frameworks, Compliance Requirements) Detailed Reference | Application support Skills Framework for the Information Age V6, 2015 ASUP | Network support Skills Framework for the Information Age V6, 2015 NTAS | Problem management e-Competence Framework (e-CF)—A common European Framework for ICT | Professionals in all industry sectors—Part 1: Framework, 2016 | C. Run—C.4. Problem | Management | Problem management Skills Framework for the Information Age V6, 2015 PBMG`
- **Komponen E — Kebijakan & Prosedur (Policies and Procedures):**
  - Kebijakan Kunci: `Relevant Policy Policy Description Related Guidance Detailed Reference | Problem resolution policy Documents rationale and provides | guidance for addressing problems | that result from incidents and | identifying validated workarounds. | ITIL V3, 2011 Service Operation, 3. Service | operation principles`
- **Komponen F — Budaya, Etika & Perilaku (Culture, Ethics and Behavior):**
  - Elemen Budaya: `Key Culture Elements Related Guidance Detailed Reference | Support a culture of proactive problem management (detection, action | and prevention) with clearly defined roles and responsibilities. Ensure a | transparent and open environment for reporting problems by providing | independent reporting mechanisms and/or rewarding people who bring | problems forward.`
- **Komponen G — Layanan, Infrastruktur & Aplikasi (Services, Infrastructure and Applications):**
  - Problem tracking/resolution system

### 5. Program Kerja Audit TI (Kertas Kerja Audit / KKA) — DSS03

- **Fokus Pengujian Audit:** Pengelolaan Masalah (Problem Management): identifikasi akar penyebab (Root Cause Analysis / RCA), Known Error, dan pencegahan insiden berulang.
- **Daftar Permintaan Dokumen Bukti (PBC — *Provided by Client*):**
  1. SOP Manajemen Masalah (Problem Management) dan kriteria pemicu pembuatan tiket Problem dari insiden berulang/Major Incident.
  1. Daftar Problem Register, laporan Root Cause Analysis (RCA), dan Known Error Database (KEDB).
  1. Bukti keterkaitan antara rekomendasi perbaikan permanen di tiket Problem dengan pembuatan Request for Change (RFC).
- **Prosedur Pengujian Kontrol (Test of Design / ToD & Test of Operating Effectiveness / ToE):**
  - ToD: Periksa apakah organisasi membedakan secara jelas antara penanganan gejala cepat (Incident Management) dengan pencarian akar masalah permanen (Problem Management).
  - ToE: Uji apakah seluruh Major Incident dan insiden berulang (recurring incidents) telah dibuatkan tiket Problem, dilakukan RCA mendalam, dan ditindaklanjuti melalui RFC.
- **Indikator Temuan / Red Flags Audit:**
  - ⚠️ Insiden yang sama terus berulang setiap minggu/bulan karena tim TI hanya melakukan restart server (workaround) tanpa pernah melakukan Root Cause Analysis.
  - ⚠️ Rekomendasi tindakan korektif permanen dari hasil RCA tidak pernah dieksekusi (tidak dihubungkan ke Change Management).

---

## DSS04 — Managed Continuity

- **Area:** Management | **Domain:** Deliver, Service and Support
- **Referensi Halaman Resmi (COBIT 2019 Framework):** hlm. 249–256
- **Deskripsi Resmi:** Establish and maintain a plan to enable the business and IT organizations to respond to incidents and quickly adapt to disruptions. This will enable continued operations of critical business processes and required I&T services and maintain availability of resources, assets and information at a level acceptable to the enterprise.
- **Tujuan (Purpose Statement):** Adapt rapidly, continue business operations and maintain availability of resources and information at a level acceptable to the enterprise in the event of a significant disruption (e.g., threats, opportunities, demands).

### 1. Pemetaan Goals Cascade & Metrik Tujuan (DSS04)

| Kategori Tujuan | Kode | Nama Tujuan Resmi | Dimensi BSC | Hubungan | Contoh Metrik Indikator (KPI / KGI) |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **Enterprise Goal** | `EG01` | Portfolio of competitive products and services | Financial | **P** | • Percent of products and services that meet or exceed targets in revenues and/or market share<br>• Ratio of profitable products and services per life cycle phase |
| **Enterprise Goal** | `EG02` | Managed business risk | Financial | **P** | • Percent of critical business objectives and services covered by risk assessment<br>• Ratio of significant incidents that were not identified in risk assessments vs. total incidents |
| **Enterprise Goal** | `EG06` | Business service continuity and availability | Customer | **P** | • Number of customer service interruptions causing significant incidents<br>• Business cost of incidents |
| **Alignment Goal** | `AG02` | Managed I&T-related risk | Financial | **S** | • Frequency of update of risk profile |
| **Alignment Goal** | `AG05` | Delivery of I&T services in line with business requirements | Customer | **P** | • Number of business disruptions due to IT service incidents<br>• Percent of business stakeholders satisfied that IT service delivery meets agreed service levels |
| **Alignment Goal** | `AG07` | Security of information, processing infrastructure and applications, and privacy | Internal | **P** | • Number of confidentiality incidents causing financial loss, business disruption or public embarrassment<br>• Number of availability incidents causing financial loss, business disruption or public embarrassment |

### 2. Komponen A: Praktik Proses, Metrik, Aktivitas & Level Kapabilitas (DSS04)

#### DSS04.01 — Define the business continuity policy, objectives and scope

> **Deskripsi Praktik:** Define business continuity policy and scope, aligned with enterprise and stakeholder objectives, to improve business resilience.

**Contoh Metrik Praktik (Example Metrics):**
- a. Percent of business continuity objectives and scope reworked due to misidentified processes and activities
- b. Percent of key stakeholders participating, defining and agreeing on continuity policy and scope

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Identify internal and outsourced business processes and service activities that are critical to the enterprise operations or necessary to meet legal and/or contractual obligations. | **Level 2** |
| 2 | 2. Identify key stakeholders and roles and responsibilities for defining and agreeing on continuity policy and scope. | **Level 2** |
| 3 | 3. Define and document the agreed minimum policy objectives and scope for business resilience. | **Level 2** |
| 4 | 4. Identify essential supporting business processes and related I&T services. | **Level 2** |

**Standar & Panduan Terkait (Related Guidance):**
- HITRUST CSF version 9, September 2017 12.01 Information Security Aspects of Business Continuity Management
- ISF , The Standard of Good Practice for Information Security 2016 BC1.1 Business Continuity Strategy; BC1.2 Business Continuity Programme
- ISO/IEC 27002:2013/Cor.2:2015(E) 17. Information security aspects of business continuity management
- National Institute of Standards and Technology Special Publication
- 800-53, Revision 5 (Draft), August 2017
- 3.6 Contingency planning (CP-1)
- Management Practice Example Metrics

#### DSS04.02 — Maintain business resilience

> **Deskripsi Praktik:** Evaluate business resilience options and choose a cost-effective and viable strategy that will ensure enterprise continuity, disaster recovery and incident response in the face of a disaster or other major incident or disruption.

**Contoh Metrik Praktik (Example Metrics):**
- a. Total downtime resulting from major incident or disruption
- b. Percent of key stakeholders involved in business impact analyses evaluating the impact over time of a disruption to critical business functions and the effect that a disruption would have on them

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Identify potential scenarios likely to give rise to events that could cause significant disruptive incidents. | **Level 2** |
| 2 | 2. Conduct a business impact analysis to evaluate the impact over time of a disruption to critical business functions and the effect that a disruption would have on them. | **Level 2** |
| 3 | 3. Establish the minimum time required to recover a business process and supporting I&T, based on an acceptable length of business interruption and maximum tolerable outage. | **Level 2** |
| 4 | 4. Determine the conditions and owners of key decisions that will cause the continuity plans to be invoked. | **Level 2** |
| 5 | 5. Assess the likelihood of threats that could cause loss of business continuity. Identify measures that will reduce the likelihood and impact through improved prevention and increased resilience. | **Level 3** |
| 6 | 6. Analyze continuity requirements to identify possible strategic business and technical options. | **Level 3** |
| 7 | 7. Identify resource requirements and costs for each strategic technical option and make strategic recommendations. | **Level 3** |
| 8 | 8. Obtain executive business approval for selected strategic options. | **Level 3** |

**Standar & Panduan Terkait (Related Guidance):**
- ISF , The Standard of Good Practice for Information Security 2016 BC1.3 Resilient Technical Environments
- ITIL V3, 2011 Service Design, 4.6 IT Continuity Management
- National Institute of Standards and Technology Special Publication
- 800-53, Revision 5 (Draft), August 2017
- 3.6 Contingency planning (CP-2)
- Management Practice Example Metrics

#### DSS04.03 — Develop and implement a business continuity response

> **Deskripsi Praktik:** Develop a business continuity plan (BCP) and disaster recovery plan (DRP) based on the strategy. Document all procedures necessary for the enterprise to continue critical activities in the event of an incident.

**Contoh Metrik Praktik (Example Metrics):**
- a. Number of critical business systems not covered by the plan
- b. Percent of key stakeholders involved in developing BCPs and DRPs

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Define the incident response actions and communications to be taken in the event of disruption. Define related roles and responsibilities, including accountability for policy and implementation. | **Level 2** |
| 2 | 2. Ensure that key suppliers and outsource partners have effective continuity plans in place. Obtain audited evidence as required. | **Level 2** |
| 3 | 3. Define the conditions and recovery procedures that would enable resumption of business processing. Include updating and reconciliation of information databases to preserve information integrity. | **Level 2** |
| 4 | 4. Develop and maintain operational BCPs and DRPs that contain the procedures to be followed to enable continued operation of critical business processes and/or temporary processing arrangements. Include links to plans of outsourced service providers. | **Level 2** |
| 5 | 5. Define and document the resources required to support the continuity and recovery procedures, considering people, facilities and IT infrastructure. | **Level 2** |
| 6 | 6. Define and document the information backup requirements required to support the plans. Include plans and paper documents as well as data files. Consider the need for security and off-site storage. | **Level 2** |
| 7 | 7. Determine required skills for individuals involved in executing the plan and procedures. | **Level 2** |
| 8 | 8. Distribute the plans and supporting documentation securely to appropriately authorized interested parties. Make sure the plans and documentation are accessible under all disaster scenarios. | **Level 3** |

**Standar & Panduan Terkait (Related Guidance):**
- ISF , The Standard of Good Practice for Information Security 2016 BC1.4 Crisis Management; BC2.1 Business Continuity Planning
- National Institute of Standards and Technology Special Publication
- 800-53, Revision 5 (Draft), August 2017
- 3.6 Contingency planning (CP-6, CP-9, CP-10)
- Management Practice Example Metrics

#### DSS04.04 — Exercise, test and review the business continuity plan (BCP) and disaster response plan (DRP)

> **Deskripsi Praktik:** Test continuity on a regular basis to exercise plans against predetermined outcomes, uphold business resilience and allow innovative solutions to be developed.

**Contoh Metrik Praktik (Example Metrics):**
- a. Frequency of tests
- b. Number of exercises and tests that achieved recovery objectives

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Define objectives for exercising and testing the business, technical, logistical, administrative, procedural and operational systems of the plan to verify completeness of the BCP and DRP in meeting business risk. | **Level 2** |
| 2 | 2. Define and agree on stakeholder exercises that are realistic and validate continuity procedures. Include roles and responsibilities and data retention arrangements that cause minimum disruption to business processes. | **Level 2** |
| 3 | 3. Assign roles and responsibilities for performing continuity plan exercises and tests. | **Level 2** |
| 4 | 4. Schedule exercises and test activities as defined in the continuity plans. | **Level 3** |
| 5 | 5. Conduct a post-exercise debriefing and analysis to consider the achievement. | **Level 4** |
| 6 | 6. Based on the results of the review, develop recommendations for improving the current continuity plans. | **Level 5** |

**Standar & Panduan Terkait (Related Guidance):**
- CMMI Cybermaturity Platform, 2018 PP .RS Develop and Maintain Response Plans; PP .RP Develop and
- Maintain Recovery Plans
- ISF , The Standard of Good Practice for Information Security 2016 BC2.3 Business Continuity Testing
- The CIS Critical Security Controls for Effective Cyber Defense Version
- 6.1, August 2016
- CSC 20: Penetration Tests and Red Team Exercises
- Management Practice Example Metrics

#### DSS04.05 — Review, maintain and improve the continuity plans

> **Deskripsi Praktik:** Conduct a management review of the continuity capability at regular intervals to ensure its continued suitability, adequacy and effectiveness. Manage changes to the plans in accordance with the change control process to ensure that continuity plans are kept up to date and continually reflect actual business requirements.

**Contoh Metrik Praktik (Example Metrics):**
- a. Percent of agreed improvements to the plan that have been reflected in the plan
- b. Percent of continuity plans and business impact assessments that are up to date

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. On a regular basis, review the continuity plans and capability against any assumptions made and current business operational and strategic objectives. | **Level 3** |
| 2 | 2. On a regular basis, review the continuity plans to consider the impact of new or major changes to enterprise organization, business processes, outsourcing arrangements, technologies, infrastructure, operating systems and application systems. | **Level 3** |
| 3 | 3. Consider whether a revised business impact assessment may be required, depending on the nature of the change. | **Level 3** |
| 4 | 4. Recommend changes in policy, plans, procedures, infrastructure, and roles and responsibilities. Communicate them as appropriate for management approval and processing via the IT change management process. | **Level 3** |

**Standar & Panduan Terkait (Related Guidance):**
- Management Practice Example Metrics

#### DSS04.06 — Conduct continuity plan training

> **Deskripsi Praktik:** Provide all concerned internal and external parties with regular training sessions regarding procedures and their roles and responsibilities in case of disruption.

**Contoh Metrik Praktik (Example Metrics):**
- a. Percent of internal and external stakeholders who received training
- b. Percent of relevant internal and external parties whose skills and competencies are current

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Roll out BCP and DRP awareness and training. | **Level 2** |
| 2 | 2. Define and maintain training requirements and plans for those performing continuity planning, impact assessments, risk assessments, media communication and incident response. Ensure that the training plans consider frequency of training and training delivery mechanisms. | **Level 3** |
| 3 | 3. Develop competencies based on practical training, including participation in exercises and tests. | **Level 3** |
| 4 | 4. Based on the exercise and test results, monitor skills and competencies. | **Level 4** |

**Standar & Panduan Terkait (Related Guidance):**
- National Institute of Standards and Technology Special Publication
- 800-53, Revision 5 (Draft), August 2017
- 3.6 Contingency planning (CP-4)
- Management Practice Example Metrics

#### DSS04.07 — Manage backup arrangements

> **Deskripsi Praktik:** Maintain availability of business-critical information.

**Contoh Metrik Praktik (Example Metrics):**
- a. Percent of backup media transferred and stored securely
- b. Percent of successful and timely restoration from backup or alternate media copies

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Back up systems, applications, data and documentation according to a defined schedule. Consider frequency (monthly, weekly, daily, etc.), mode of backup (e.g., disk mirroring for real-time backups vs. DVD-ROM for long-term retention), type of backup (e.g., full vs. incremental), and type of media. Consider also automated online backups, data types (e.g., voice, optical), creation of logs, critical end-user computing data (e.g., spreadsheets), physical and logical location of data sources, security and access rights, and encryption. | **Level 2** |
| 2 | 2. Define requirements for on-site and off-site storage of backup data that meet the business requirements. Consider the accessibility required to back up data. | **Level 2** |
| 3 | 3. Periodically test and refresh archived and backup data. | **Level 2** |
| 4 | 4. Ensure that systems, applications, data and documentation maintained or processed by third parties are adequately backed up or otherwise secured. Consider requiring return of backups from third parties. Consider escrow or deposit arrangements. | **Level 2** |

**Standar & Panduan Terkait (Related Guidance):**
- CMMI Cybermaturity Platform, 2018 IP .BP Apply Backup Processes
- HITRUST CSF version 9, September 2017 09.05 Information Back-Up
- ISF , The Standard of Good Practice for Information Security 2016 SY2.3 Backup
- ISO/IEC 27002:2013/Cor.2:2015(E) 12.3 Backup
- National Institute of Standards and Technology Special Publication
- 800-53, Revision 5 (Draft), August 2017
- 3.6 Contingency planning (CP-3)
- The CIS Critical Security Controls for Effective Cyber Defense Version
- 6.1, August 2016
- CSC 10: Data Recovery Capability
- Management Practice Example Metrics

#### DSS04.08 — Conduct post-resumption review

> **Deskripsi Praktik:** Assess the adequacy of the business continuity plan (BCP) and disaster response plan (DRP) following successful resumption of business processes and services after a disruption.

**Contoh Metrik Praktik (Example Metrics):**
- a. Percent of issues identified and subsequently addressed in the plan
- b. Percent of issues identified and subsequently addressed in training materials

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Assess adherence to the documented BCP and DRP. | **Level 4** |
| 2 | 2. Determine the effectiveness of the plans, continuity capabilities, roles and responsibilities, skills and competencies, resilience to the incident, technical infrastructure, and organizational structures and relationships. | **Level 4** |
| 3 | 3. Identify weaknesses or omissions in the plans and capabilities and make recommendations for improvement. Obtain management approval for any changes to the plans and apply via the enterprise change control process. | **Level 5** |

### 3. Komponen B: Struktur Organisasi & Matriks RACI (DSS04)

| Kode Praktik | Nama Praktik | Accountable (A) — Penanggung Jawab Tunggal | Responsible (R) — Pelaksana Operasional |
| :--- | :--- | :--- | :--- |
| `DSS04.01` | Define the business continuity policy, objectives and scope | **Chief Operating Officer** | Business Process Owners, Chief Information Security Officer, Chief Information Officer, Head IT operations, Service Manager, Business Continuity Manager, Executive Committee |
| `DSS04.02` | Maintain business resilience | **Chief Operating Officer** | Business Process Owners, Chief Information Officer, Head Architect, Head IT operations, Information Security Manager, Business Continuity Manager, Executive Committee |
| `DSS04.03` | Develop and implement a business continuity response | **Business Continuity Manager** | Business Process Owners, Chief Information Officer, Head IT operations, Information Security Manager, Chief Technology Officer |
| `DSS04.04` | Exercise, test and review the business continuity plan (BCP) and disaster response plan (DRP) | **Business Continuity Manager** | Business Process Owners, Chief Information Officer, Head IT operations, Information Security Manager, Chief Technology Officer |
| `DSS04.05` | Review, maintain and improve the continuity plans | **Chief Operating Officer** | Business Process Owners, Chief Information Security Officer, Chief Information Officer, Head IT operations, Business Continuity Manager, Chief Technology Officer |
| `DSS04.06` | Conduct continuity plan training | **Business Continuity Manager** | Business Process Owners, Chief Information Officer, Head Development, Head IT operations, Information Security Manager, Chief Technology Officer |
| `DSS04.07` | Manage backup arrangements | **Chief Technology Officer** | Head IT operations, Information Security Manager, Business Continuity Manager, Data Mgmt Function |
| `DSS04.08` | Conduct post-resumption review | **Business Continuity Manager** | Business Process Owners, Chief Information Security Officer, Chief Information Officer, Head IT operations, Chief Technology Officer |

### 4. Komponen C, D, E, F, dan G (DSS04)

- **Komponen C — Aliran & Item Informasi (Information Flows and Items):**
  - Ringkasan Input/Output Praktik: `(see also Section 3.6) ; Management Practice Inputs Outputs ; DSS04.01 Define the business continuity policy, ; objectives and scope. ; From Description Description To ; APO09.03 SLAs Policy and objectives for ; business continuity ; APO01.02 ; Assessments of current ; continuity capabilities ; and gaps ; Internal ; Disruptive incident ; scenarios ; Internal ; DSS04.02 Maintain business resilience. APO12.06 •  Risk impact ; communication ; •  Risk-related root`
- **Komponen D — SDM, Keterampilan & Kompetensi (People, Skills and Competencies — SFIA V6 / e-CF):**
  - Referensi Kompetensi: `Skill Related Guidance (Standards, Frameworks, Compliance Requirements) Detailed Reference | Continuity management Skills Framework for the Information Age V6, 2015 COPL`
- **Komponen E — Kebijakan & Prosedur (Policies and Procedures):**
  - Kebijakan Kunci: `Relevant Policy Policy Description Related Guidance Detailed Reference | Business continuity policy Outlines management’s | commitment to the business | impact assessment (BIA), business | contingency plan (including | trusted recovery), recovery | requirements for critical systems, | defined thresholds and triggers | for contingencies, escalation plan, | data recovery plan, training and | testing. | Crisis management policy Sets guidelines and sequence of`
- **Komponen F — Budaya, Etika & Perilaku (Culture, Ethics and Behavior):**
  - Elemen Budaya: `Key Culture Elements Related Guidance Detailed Reference | Embed the need for business resilience in the enterprise culture. | Regularly and frequently update employees about core values, desired | behaviors and strategic objectives to maintain the enterprise’s composure | and image in every situation. Regularly test business continuity | procedures and disaster recovery.`
- **Komponen G — Layanan, Infrastruktur & Aplikasi (Services, Infrastructure and Applications):**
  - External hosting services
  - Incident monitoring tools
  - Remote storage facility services

### 5. Program Kerja Audit TI (Kertas Kerja Audit / KKA) — DSS04

- **Fokus Pengujian Audit:** Pengelolaan Keberlangsungan Layanan (Business Continuity Plan / BCP & IT Disaster Recovery Plan / DRP), analisis BIA, backup & restore, serta uji DRP.
- **Daftar Permintaan Dokumen Bukti (PBC — *Provided by Client*):**
  1. Dokumen Business Impact Analysis (BIA) yang menetapkan target RTO (Recovery Time Objective) dan RPO (Recovery Point Objective).
  1. Dokumen Business Continuity Plan (BCP) dan IT Disaster Recovery Plan (DRP) serta arsitektur replikasi DRC.
  1. Kebijakan & log pencadangan data (Backup Logs, Offsite/Immutable Backup), laporan uji pemulihan backup (Restore Test), dan laporan pelaksanaan DRP Exercise/Simulasi.
- **Prosedur Pengujian Kontrol (Test of Design / ToD & Test of Operating Effectiveness / ToE):**
  - ToD: Evaluasi keselarasan kapabilitas teknis DRC dan jadwal backup dengan target RTO dan RPO yang ditetapkan pada dokumen BIA.
  - ToE: Periksa log keberhasilan backup harian, bukti pengujian restore data secara berkala, serta laporan hasil simulasi uji DRP (termasuk skenario switch-over ke DRC dan uji penanggulangan ransomware).
- **Indikator Temuan / Red Flags Audit:**
  - ⚠️ Backup dijalankan setiap hari tetapi tidak pernah diuji restore (ketika terjadi insiden, file backup ternyata korup/tidak dapat dipulihkan).
  - ⚠️ Uji DRP hanya dilakukan secara tabletop/parsial tanpa pernah menguji perpindahan transaksi riil ke DRC, atau waktu pemulihan aktual jauh melampaui target RTO.

---

## DSS05 — Managed Security Services

- **Area:** Management | **Domain:** Deliver, Service and Support
- **Referensi Halaman Resmi (COBIT 2019 Framework):** hlm. 257–264
- **Deskripsi Resmi:** Protect enterprise information to maintain the level of information security risk acceptable to the enterprise in accordance with the security and privacy policy. Establish and maintain information security and privacy roles and access privileges. Perform security monitoring.
- **Tujuan (Purpose Statement):** Minimize the business impact of operational information security and privacy vulnerabilities and incidents.

### 1. Pemetaan Goals Cascade & Metrik Tujuan (DSS05)

| Kategori Tujuan | Kode | Nama Tujuan Resmi | Dimensi BSC | Hubungan | Contoh Metrik Indikator (KPI / KGI) |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **Enterprise Goal** | `EG02` | Managed business risk | Financial | **P** | • Percent of critical business objectives and services covered by risk assessment<br>• Ratio of significant incidents that were not identified in risk assessments vs. total incidents |
| **Enterprise Goal** | `EG06` | Business service continuity and availability | Customer | **P** | • Number of customer service interruptions causing significant incidents<br>• Business cost of incidents |
| **Alignment Goal** | `AG01` | I&T compliance and support for business compliance with external laws and regulations | Financial | **S** | • Cost of IT noncompliance, including settlements and fines, and the impact of reputational loss |
| **Alignment Goal** | `AG02` | Managed I&T-related risk | Financial | **P** | • Frequency of update of risk profile<br>• Percent of enterprise risk assessments including I&T-related risk |
| **Alignment Goal** | `AG05` | Delivery of I&T services in line with business requirements | Customer | **S** | • Number of business disruptions due to IT service incidents |
| **Alignment Goal** | `AG07` | Security of information, processing infrastructure and applications, and privacy | Internal | **P** | • Number of confidentiality incidents causing financial loss, business disruption or public embarrassment<br>• Number of availability incidents causing financial loss, business disruption or public embarrassment |
| **Alignment Goal** | `AG11` | I&T compliance with internal policies | Internal | **S** | • Number of incidents related to noncompliance with I&T-related policies |

### 2. Komponen A: Praktik Proses, Metrik, Aktivitas & Level Kapabilitas (DSS05)

#### DSS05.01 — Protect against malicious software

> **Deskripsi Praktik:** Implement and maintain preventive, detective and corrective measures (especially up-to-date security patches and virus control) across the enterprise to protect information systems and technology from malicious software (e.g., malware, ransomware, viruses, worms, spyware, spam).

**Contoh Metrik Praktik (Example Metrics):**
- a. Number of successful malicious software attacks
- b. Percent of employees failing tests on malicious attacks (e.g., test of phishing email)

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Install and activate malicious software protection tools on all processing facilities, with malicious software definition files that are updated as required (automatically or semi-automatically). | **Level 2** |
| 2 | 2. Filter incoming traffic, such as email and downloads, to protect against unsolicited information (e.g., spyware, phishing emails). | **Level 2** |
| 3 | 3. Communicate malicious software awareness and enforce prevention procedures and responsibilities. Conduct periodic training about malware in email and Internet usage. Train users to not open, but report, suspicious emails and to not install shared or unapproved software. | **Level 3** |
| 4 | 4. Distribute all protection software centrally (version and patch-level) using centralized configuration and IT change management. | **Level 3** |
| 5 | 5. Regularly review and evaluate information on new potential threats (e.g., reviewing vendors’ products and services security advisories). | **Level 4** |

**Standar & Panduan Terkait (Related Guidance):**
- CMMI Cybermaturity Platform, 2018 DP .DC Detect Malicious Code; RI.VT Vulnerability and Threat
- Identification
- HITRUST CSF version 9, September 2017 09.04 Protection Against Malicious & Mobile Code
- SF , The Standard of Good Practice for Information Security 2016 TS1 Security Solutions
- SO/IEC 27002:2013/Cor.2:2015(E) 12.2 Protection against malware
- The CIS Critical Security Controls for Effective Cyber Defense Version
- 6.1, August 2016
- CSC 4: Continuous Vulnerability Assessment and Remediation; CSC 8:
- Malware Defenses
- Management Practice Example Metrics

#### DSS05.02 — Manage network and connectivity security

> **Deskripsi Praktik:** Use security measures and related management procedures to protect information over all methods of connectivity.

**Contoh Metrik Praktik (Example Metrics):**
- a. Number of firewall breaches
- b. Number of vulnerabilities discovered
- c. Percent of time network and systems not available due to security incident

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Allow only authorized devices to have access to corporate information and the enterprise network. Configure these devices to force password entry. | **Level 2** |
| 2 | 2. Implement network filtering mechanisms, such as firewalls and intrusion detection software. Enforce appropriate policies to control inbound and outbound traffic. | **Level 2** |
| 3 | 3. Apply approved security protocols to network connectivity. | **Level 2** |
| 4 | 4. Configure network equipment in a secure manner. | **Level 2** |
| 5 | 5. Encrypt information in transit according to its classification. | **Level 3** |
| 6 | 6. Based on risk assessments and business requirements, establish and maintain a policy for security of connectivity. | **Level 3** |
| 7 | 7. Establish trusted mechanisms to support the secure transmission and receipt of information. | **Level 3** |
| 8 | 8. Carry out periodic penetration testing to determine adequacy of network protection. | **Level 4** |
| 9 | 9. Carry out periodic testing of system security to determine adequacy of system protection. | **Level 4** |

**Standar & Panduan Terkait (Related Guidance):**
- CMMI Cybermaturity Platform, 2018 AC.MI Manage Network Integrity & Segregation; CM.MN Monitor
- Networks; AC.CP Manage Communication Protections
- HITRUST CSF version 9, September 2017 01.04 Network Access Control
- ISF , The Standard of Good Practice for Information Security 2016 PA2.3 Mobile Device Connectivity; NC1.1 Network Device Configuration
- ISO/IEC 27002:2013/Cor.2:2015(E) 13.1 Network security management
- National Institute of Standards and Technology Special Publication
- 800-53, Revision 5 (Draft), August 2017
- 3.20 System and information integrity (SI-8)
- The CIS Critical Security Controls for Effective Cyber Defense Version
- 6.1, August 2016
- CSC 9: Limitation and Control of Network Ports, Protocols, and Services;
- CSC 11: Secure Configurations for Network Devices such as Firewalls,
- Routers, and Switches
- Management Practice Example Metrics

#### DSS05.03 — Manage endpoint security

> **Deskripsi Praktik:** Ensure that endpoints (e.g., laptop, desktop, server, and other mobile and network devices or software) are secured at a level that is equal to or greater than the defined security and privacy requirements for the information processed, stored or transmitted.

**Contoh Metrik Praktik (Example Metrics):**
- a. Number of incidents involving endpoint devices
- b. Number of unauthorized devices detected on the network or in the end-user environment
- c. Percent of individuals receiving awareness training relating to use of endpoint devices

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Configure operating systems in a secure manner. | **Level 2** |
| 2 | 2. Implement device lockdown mechanisms. | **Level 2** |
| 3 | 3. Manage remote access and control (e.g., mobile devices, teleworking). | **Level 2** |
| 4 | 4. Manage network configuration in a secure manner. | **Level 2** |
| 5 | 5. Implement network traffic filtering on endpoint devices. | **Level 2** |
| 6 | 6. Protect system integrity. | **Level 2** |
| 7 | 7. Provide physical protection of endpoint devices. | **Level 2** |
| 8 | 8. Dispose of endpoint devices securely. | **Level 2** |
| 9 | 9. Manage malicious access through email and web browsers. For example, block certain websites and deactivate click-through on links for smartphones. | **Level 2** |
| 10 | 10. Encrypt information in storage according to its classification. | **Level 3** |

**Standar & Panduan Terkait (Related Guidance):**
- CMMI Cybermaturity Platform, 2018 IP .MM Apply Mobile Device Management; TP .MP Apply Media Protection;
- DP .DP Detect Mobile Code and Browser Protection
- ISF , The Standard of Good Practice for Information Security 2016 PM1.3 Remote Working; PA2.1 Mobile Device Configuration; PA2.4
- Employee-owned Devices; PA2.5 Portable Storage Devices; NC1.6
- Remote Maintenance
- National Institute of Standards and Technology Special Publication
- 800-53, Revision 5 (Draft), August 2017
- 3.4 Assessment, authorization and monitoring (CA-8, CA-9); 3.19 System
- and communications protection (SC-10)
- The CIS Critical Security Controls for Effective Cyber Defense Version
- 6.1, August 2016
- CSC 3: Secure Configurations for Hardware and Software on Mobile
- Devices, Laptops, Workstations, and Servers; CSC 7: Email and Web
- Browser Protections
- Management Practice Example Metrics

#### DSS05.04 — Manage user identity and logical access

> **Deskripsi Praktik:** Ensure that all users have information access rights in accordance with the business unit's privacy policy and business requirements. Coordinate with business units that manage their own access rights within business processes.

**Contoh Metrik Praktik (Example Metrics):**
- a. Average time between change and update of accounts
- b. Number of accounts (vs. number of authorized users/staff)
- c. Number of incidents relating to unauthorized access to information

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Maintain user access rights in accordance with business function, process requirements and security policies. Align the management of identities and access rights to the defined roles and responsibilities, based on least-privilege, need-to-have and need-to-know principles. | **Level 2** |
| 2 | 2. Administer all changes to access rights (creation, modifications and deletions) in a timely manner based only on approved and documented transactions authorized by designated management individuals. | **Level 3** |
| 3 | 3. Segregate, reduce to the minimum number necessary and actively manage privileged user accounts. Ensure monitoring on all activity on these accounts. | **Level 3** |
| 4 | 4. Uniquely identify all information processing activities by functional roles. Coordinate with business units to ensure that all roles are consistently defined, including roles that are defined by the business itself within business process applications. | **Level 3** |
| 5 | 5. Authenticate all access to information assets based on the individual's role or business rules. Coordinate with business units that manage authentication within applications used in business processes to ensure that authentication controls have been properly administered. | **Level 3** |
| 6 | 6. Ensure that all users (internal, external and temporary) and their activity on IT systems (business application, IT infrastructure, system operations, development and maintenance) are uniquely identifiable. | **Level 3** |
| 7 | 7. Maintain an audit trail of access to information dependent upon its sensitivity and regulatory requirements. | **Level 4** |
| 8 | 8. Perform regular management review of all accounts and related privileges. | **Level 4** |

**Standar & Panduan Terkait (Related Guidance):**
- HITRUST CSF version 9, September 2017 10.03 Cryptographic Controls
- ISF , The Standard of Good Practice for Information Security 2016 PM1.1 Employment Life Cycle; SA1 Access Management
- ISO/IEC 27002:2013/Cor.2:2015(E) 7.3 Termination and change of employment; 9. Access control
- ITIL V3, 2011 Service Operation, 4.5 Access Management
- National Institute of Standards and Technology Special Publication
- 800-53, Revision 5 (Draft), August 2017
- 3.1 Access control (AC-11, AC-12); 3.11 Media protection
- (MP-2, MP-4, MP-7); 3.13 Physical and environmental protection
- (PE-2, PE-3, PE-6)
- The CIS Critical Security Controls for Effective Cyber Defense Version
- 6.1, August 2016
- CSC 1: Inventory of Authorized and Unauthorized Devices; CSC 2:
- Inventory of Authorized and Unauthorized Software; CSC 5: Controlled
- Use of Administrative Privileges; CSC 16: Account Monitoring and
- Control
- Management Practice Example Metrics

#### DSS05.05 — Manage physical access to I&T assets

> **Deskripsi Praktik:** Define and implement procedures (including emergency procedures) to grant, limit and revoke access to premises, buildings and areas, according to business need. Access to premises, buildings and areas should be justified, authorized, logged and monitored. This requirement applies to all persons entering the premises, including staff, temporary staff, clients, vendors, visitors or any other third party.

**Contoh Metrik Praktik (Example Metrics):**
- a. Average rating for physical security assessments
- b. Number of physical information security-related incidents

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Log and monitor all entry points to IT sites. Register all visitors, including contractors and vendors, to the site. | **Level 2** |
| 2 | 2. Ensure all personnel display properly approved identification at all times. | **Level 2** |
| 3 | 3. Require visitors to be escorted at all times while on-site. | **Level 2** |
| 4 | 4. Restrict and monitor access to sensitive IT sites by establishing perimeter restrictions, such as fences, walls, and security devices on interior and exterior doors. | **Level 2** |
| 5 | 5. Manage requests to allow appropriately authorized access to the computing facilities. | **Level 3** |
| 6 | 6. Ensure that access profiles remain current. Base access to IT sites (server rooms, buildings, areas or zones) on job function and responsibilities. | **Level 3** |
| 7 | 7. Conduct regular physical information security awareness training. | **Level 3** |

**Standar & Panduan Terkait (Related Guidance):**
- CMMI Cybermaturity Platform, 2018 AC.MA Manage Access; ID.DI Determine Impacts
- HITRUST CSF version 9, September 2017 01.01 Business Requirement for Access Control; 01.02 Authorized
- Access to Information Systems; 02.0 Human Resources Security
- ISF , The Standard of Good Practice for Information Security 2016 NC1.2 Physical Network Management
- ISO/IEC 27002:2013/Cor.2:2015(E) 11. Physical and environmental security
- Management Practice Example Metrics

#### DSS05.06 — Manage sensitive documents and output devices

> **Deskripsi Praktik:** Establish appropriate physical safeguards, accounting practices and inventory management regarding sensitive I&T assets, such as special forms, negotiable instruments, special-purpose printers or security tokens.

**Contoh Metrik Praktik (Example Metrics):**
- a. Number of stolen output devices
- b. Percent of sensitive documents and output devices identified in inventory

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Establish procedures to govern the receipt, use, removal and disposal of sensitive documents and output devices into, within, and outside of the enterprise. | **Level 2** |
| 2 | 2. Ensure cryptographic controls are in place to protect sensitive electronically stored information. | **Level 2** |
| 3 | 3. Assign access privileges to sensitive documents and output devices based on the least-privilege principle, balancing risk and business requirements. | **Level 3** |
| 4 | 4. Establish an inventory of sensitive documents and output devices, and conduct regular reconciliations. | **Level 3** |
| 5 | 5. Establish appropriate physical safeguards over sensitive documents. | **Level 3** |
| 6 | 6. Put cryptographic controls in place to ensure the protection of sensitive information (confidentiality, authenticity, integrity). | **Level 3** |

**Standar & Panduan Terkait (Related Guidance):**
- CMMI Cybermaturity Platform, 2018 CM.Ph Monitor Physical
- HITRUST CSF version 9, September 2017 01.06 Application & Information Access Control; 01.07 Mobile
- Computing & Teleworking; 08.0 Physical & Environmental Security; 10.03
- Cryptographic Controls; 10.04 Security of System Files
- ISF , The Standard of Good Practice for Information Security 2016 IR2.3 Business Impact Assessment - Confidentiality Requirements; IR2.4
- Business Impact Assessment - Integrity Requirements; IR2.5 Business
- Impact Assessment - Availability Requirements; IM2.2 Sensitive Physical
- Information; PA2.2 Enterprise Mobility Man
- ISO/IEC 27002:2013/Cor.2:2015(E) 10. Cryptography
- National Institute of Standards and Technology Special Publication
- 800-53, Revision 5 (Draft), August 2017
- 3.1 Access control (AC-2, AC-3, AC-4, AC-5, AC-6, AC-13, AC-24); 3.7
- Identification and authentication (IA-2, IA-10, IA-11)
- The CIS Critical Security Controls for Effective Cyber Defense Version
- 6.1, August 2016
- CSC 15: Wireless Access Control
- Management Practice Example Metrics

#### DSS05.07 — Manage vulnerabilities and monitor the infrastructure for security-related events

> **Deskripsi Praktik:** Using a portfolio of tools and technologies (e.g., intrusion detection tools), manage vulnerabilities and monitor the infrastructure for unauthorized access. Ensure that security tools, technologies and detection are integrated with general event monitoring and incident management.

**Contoh Metrik Praktik (Example Metrics):**
- a. Number of vulnerability tests carried out on perimeter devices
- b. Number of vulnerabilities discovered during testing
- c. Time taken to remediate any vulnerabilities
- d. Percent of tickets created in a timely manner when monitoring systems identify potential security incidents

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Continually use a portfolio of supported technologies, services and assets (e.g., vulnerability scanners, fuzzers and sniffers, protocol analyzers) to identify information security vulnerabilities. | **Level 2** |
| 2 | 2. Define and communicate risk scenarios so they can be easily recognized and the likelihood and impacts understood. | **Level 2** |
| 3 | 3. Regularly review the event logs for potential incidents. | **Level 2** |
| 4 | 4. Ensure that security-related incident tickets are created in a timely manner when monitoring identifies potential incidents. | **Level 2** |
| 5 | 5. Log security-related events and retain records for appropriate period. | **Level 3** |

**Standar & Panduan Terkait (Related Guidance):**
- ISF , The Standard of Good Practice for Information Security 2016 IR2.6 Threat Profiling
- National Institute of Standards and Technology Special Publication
- 800-53, Revision 5 (Draft), August 2017
- 3.7 Identification and authentication (IA-3); 3.11 Media protection
- (MP-1); 3.13 Physical and environmental protection (PE-5);
- 3.19 System and communications protection (SC-15)
- The CIS Critical Security Controls for Effective Cyber Defense Version
- 6.1, August 2016
- Maintenance, Monitoring, and Analysis of Audit Logs

### 3. Komponen B: Struktur Organisasi & Matriks RACI (DSS05)

| Kode Praktik | Nama Praktik | Accountable (A) — Penanggung Jawab Tunggal | Responsible (R) — Pelaksana Operasional |
| :--- | :--- | :--- | :--- |
| `DSS05.01` | Protect against malicious software | **Chief Information Security Officer** | Business Process Owners, Head Human Resources, Head Development, Head IT operations, Information Security Manager |
| `DSS05.02` | Manage network and connectivity security | **Chief Information Security Officer** | Head Development, Head IT operations, Information Security Manager |
| `DSS05.03` | Manage endpoint security | **Chief Information Security Officer** | Head Development, Head IT operations, Information Security Manager |
| `DSS05.04` | Manage user identity and logical access | **Chief Information Security Officer** | Business Process Owners, Head IT operations, Information Security Manager, Privacy Officer |
| `DSS05.05` | Manage physical access to I&T assets | **Chief Information Security Officer** | Head IT operations, Information Security Manager, Privacy Officer |
| `DSS05.06` | Manage sensitive documents and output devices | **Chief Information Officer** | Head IT operations, Privacy Officer |
| `DSS05.07` | Manage vulnerabilities and monitor the infrastructure for security-related events | **Chief Information Security Officer** | Head IT operations, Information Security Manager, Privacy Officer |

### 4. Komponen C, D, E, F, dan G (DSS05)

- **Komponen C — Aliran & Item Informasi (Information Flows and Items):**
  - Ringkasan Input/Output Praktik: `(see also Section 3.6) ; Management Practice Inputs Outputs ; DSS05.01 Protect against malicious software. From Description Description To ; Malicious software ; prevention policy ; APO01.02 ; Evaluations of potential ; threats ; APO12.02; ; APO12.03 ; DSS05.02 Manage network and connectivity security. APO01.07 Data classification ; guidelines ; Connectivity security ; policy ; APO01.02 ; APO09.03 SLAs Results of penetration ; tests ; MEA04.07`
- **Komponen D — SDM, Keterampilan & Kompetensi (People, Skills and Competencies — SFIA V6 / e-CF):**
  - Referensi Kompetensi: `Skill Related Guidance (Standards, Frameworks, Compliance Requirements) Detailed Reference | Information security Skills Framework for the Information Age V6, 2015 SCTY | Information security management e-Competence Framework (e-CF)—A common European Framework for ICT | Professionals in all industry sectors—Part 1: Framework, 2016 | E. Manage— E.8. Information | Security Management | Penetration testing Skills Framework for the Information Age V6, 2015 PENT | Security administration Skills Framework for the Information Age V6, 2015 SCAD`
- **Komponen E — Kebijakan & Prosedur (Policies and Procedures):**
  - Kebijakan Kunci: `Relevant Policy Policy Description Related Guidance Detailed Reference | Information security policy Sets guidelines to protect | corporate information and | associated systems and | infrastructure.`
- **Komponen F — Budaya, Etika & Perilaku (Culture, Ethics and Behavior):**
  - Elemen Budaya: `Key Culture Elements Related Guidance Detailed Reference | Create a culture of awareness regarding user responsibility to maintain | security and privacy practices. | 1) HITRUST CSF version 9, | September 2017; (2) ISF , The | Standard of Good Practice for | Information Security 2016 | (1) 01.03 User Responsibilities;`
- **Komponen G — Layanan, Infrastruktur & Aplikasi (Services, Infrastructure and Applications):**
  - Directory services
  - Email filtering systems
  - Identity and access management system
  - Security awareness services
  - Security information and event management (SIEM) tools
  - Security operations center (SOC) services
  - Third-party security assessment services
  - URL filtering systems

### 5. Program Kerja Audit TI (Kertas Kerja Audit / KKA) — DSS05

- **Fokus Pengujian Audit:** Pengelolaan Layanan Keamanan Teknis (Security Services): anti-malware/EDR, keamanan jaringan/firewall, keamanan endpoint, manajemen kerentanan/patching, IAM/PAM, dan fisik.
- **Daftar Permintaan Dokumen Bukti (PBC — *Provided by Client*):**
  1. Dokumentasi arsitektur keamanan jaringan (Firewall rules, segmentasi VLAN/DMZ, WAF, IDS/IPS) dan laporan Firewall Rule Review.
  1. Laporan Vulnerability Assessment (VA), Penetration Testing (Pentest), serta status penerapan Security Patching pada OS/DB/Aplikasi.
  1. Kebijakan & daftar akun Identity and Access Management (IAM), Privileged Access Management (PAM), log User Access Review (UAR), dan pemantauan SIEM/SOC.
- **Prosedur Pengujian Kontrol (Test of Design / ToD & Test of Operating Effectiveness / ToE):**
  - ToD: Tinjau desain pertahanan berlapis (Defense-in-Depth) mencakup jaringan, endpoint, identitas (MFA & Least Privilege), enkripsi, dan pemantauan log keamanan.
  - ToE: Uji sampel perubahan aturan firewall, ketepatan waktu patching kerentanan kritis, penutupan temuan Pentest, serta pelaksanaan User Access Review (UAR) berkala atas akun biasa dan akun privileged (admin/root).
- **Indikator Temuan / Red Flags Audit:**
  - ⚠️ Server produksi menggunakan sistem operasi yang sudah End-of-Life (EoL) atau belum di-patch terhadap kerentanan kritis (>90 hari).
  - ⚠️ Penggunaan akun administrator bersama (shared admin/root account) tanpa MFA, atau terdapat aturan firewall 'ANY to ANY' menuju jaringan produksi.

---

## DSS06 — Managed Business Process Controls

- **Area:** Management | **Domain:** Deliver, Service and Support
- **Referensi Halaman Resmi (COBIT 2019 Framework):** hlm. 265–271
- **Deskripsi Resmi:** Define and maintain appropriate business process controls to ensure that information related to and processed by in-house or outsourced business processes satisfies all relevant information control requirements. Identify the relevant information control requirements. Manage and operate adequate input, throughput and output controls (application controls) to ensure that information and information processing satisfy these requirements.
- **Tujuan (Purpose Statement):** Maintain information integrity and the security of information assets handled within business processes in the enterprise or its outsourced operation.

### 1. Pemetaan Goals Cascade & Metrik Tujuan (DSS06)

| Kategori Tujuan | Kode | Nama Tujuan Resmi | Dimensi BSC | Hubungan | Contoh Metrik Indikator (KPI / KGI) |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **Enterprise Goal** | `EG01` | Portfolio of competitive products and services | Financial | **P** | • Percent of products and services that meet or exceed targets in revenues and/or market share<br>• Ratio of profitable products and services per life cycle phase |
| **Enterprise Goal** | `EG05` | Customer-oriented service culture | Customer | **P** | • Number of customer service disruptions<br>• Percent of business stakeholders satisfied that customer service delivery meets agreed levels |
| **Enterprise Goal** | `EG12` | Managed digital transformation programs | Growth | **P** | • Number of programs on time and within budget<br>• Percent of stakeholders satisfied with program delivery |
| **Alignment Goal** | `AG02` | Managed I&T-related risk | Financial | **S** | • Frequency of update of risk profile |
| **Alignment Goal** | `AG05` | Delivery of I&T services in line with business requirements | Customer | **S** | • Number of business disruptions due to IT service incidents |
| **Alignment Goal** | `AG07` | Security of information, processing infrastructure and applications, and privacy | Internal | **S** | • Number of confidentiality incidents causing financial loss, business disruption or public embarrassment |
| **Alignment Goal** | `AG08` | Enabling and supporting business processes by integrating applications and technology | Internal | **P** | • Time to execute business process changes involving I&T<br>• Number of I&T-enabled business programs delayed or incurring additional cost due to technology integration issues |
| **Alignment Goal** | `AG11` | I&T compliance with internal policies | Internal | **S** | • Number of incidents related to noncompliance with I&T-related policies |

### 2. Komponen A: Praktik Proses, Metrik, Aktivitas & Level Kapabilitas (DSS06)

#### DSS06.01 — Align control activities embedded in business processes with enterprise objectives

> **Deskripsi Praktik:** Continually assess and monitor the execution of business process activities and related controls (based on enterprise risk), to ensure that processing controls align with business needs.

**Contoh Metrik Praktik (Example Metrics):**
- a. Percent of completed inventory of critical processes and key controls
- b. Percent of processing controls aligned with business needs

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Identify and document the necessary control activities for key business processes to satisfy control requirements for strategic, operational, reporting and compliance objectives. | **Level 2** |
| 2 | 2. Prioritize control activities based on the inherent risk to the business. Identify key controls. | **Level 2** |
| 3 | 3. Ensure ownership of key control activities. | **Level 2** |
| 4 | 4. Implement automated controls. | **Level 3** |
| 5 | 5. Continually monitor control activities on an end-to-end basis to identify opportunities for improvement. | **Level 4** |
| 6 | 6. Continually improve the design and operation of business process controls. | **Level 5** |

**Standar & Panduan Terkait (Related Guidance):**
- National Institute of Standards and Technology Special Publication
- 800-37, Revision 2 (Draft), May 2018
- 3.1 Preparation (Task 10, 11)
- The CIS Critical Security Controls for Effective Cyber Defense Version
- 6.1, August 2016
- CSC 14: Controlled Access Based on the Need to Know
- Management Practice Example Metrics

#### DSS06.02 — Control the processing of information

> **Deskripsi Praktik:** Operate the execution of the business process activities and related controls, based on enterprise risk. Ensure that information processing is valid, complete, accurate, timely and secure (i.e., reflects legitimate and authorized business use).

**Contoh Metrik Praktik (Example Metrics):**
- a. Number of incidents and audit report findings indicating failure of key controls
- b. Percent of coverage of key controls within test plans

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Authenticate the originator of transactions and verify that the individual has the authority to originate the transaction. | **Level 2** |
| 2 | 2. Ensure adequate segregation of duties regarding the origination and approval of transactions. | **Level 2** |
| 3 | 3. Verify that transactions are accurate, complete and valid. Controls may include sequence, limit, range, validity, reasonableness, table look-ups, existence, key verification, check digit, completeness, duplicate and logical relationship checks, and time edits. Validation criteria and parameters should be subject to periodic reviews and confirmations. Validate input data and edit or, where applicable, send back for correction as close to the point of origination as possible. | **Level 3** |
| 4 | 4. Without compromising original transaction authorization levels, correct and resubmit data that were erroneously input. Where appropriate for reconstruction, retain original source documents for the appropriate amount of time. | **Level 3** |
| 5 | 5. Maintain the integrity and validity of data throughout the processing cycle. Ensure that detection of erroneous transactions does not disrupt processing of valid transactions. | **Level 3** |
| 6 | 6. Handle output in an authorized manner, deliver it to the appropriate recipient and protect the information during transmission. Verify the accuracy and completeness of the output. | **Level 3** |
| 7 | 7. Maintain the integrity of data during unexpected interruptions in business processing. Confirm data integrity after processing failures. | **Level 3** |
| 8 | 8. Before passing transaction data between internal applications and business/operational functions (inside or outside the enterprise), check for proper addressing, authenticity of origin and integrity of content. Maintain authenticity and integrity during transmission or transport. | **Level 3** |

**Standar & Panduan Terkait (Related Guidance):**
- HITRUST CSF version 9, September 2017 13.01 Openness and Transparency; 13.02 Individual Choice and
- Participation
- ISF , The Standard of Good Practice for Information Security 2016 BA1.4 Information Validation
- Management Practice Example Metrics

#### DSS06.03 — Manage roles, responsibilities, access privileges and levels of authority

> **Deskripsi Praktik:** Manage business roles, responsibilities, levels of authority and segregation of duties needed to support the business process objectives. Authorize access to all information assets related to business information processes, including those under the custody of the business, IT and third parties. This ensures that the business knows where the data are and who is handling data on its behalf.

**Contoh Metrik Praktik (Example Metrics):**
- a. Number of incidents and audit findings due to access or separation- of-duties violations
- b. Percent of business process roles with assigned access rights and levels of authority
- c. Percent of business process roles with clear separation of duties

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Allocate roles and responsibilities based on approved job descriptions and business process activities. | **Level 2** |
| 2 | 2. Allocate levels of authority for approval of transactions, transaction limits and any other decisions relating to the business process, based on approved job roles. | **Level 2** |
| 3 | 3. Allocate roles for sensitive activities so there is a clear segregation of duties. | **Level 2** |
| 4 | 4. Allocate access rights and privileges based on the minimum that is required to perform job activities, based on pre-defined job roles. Remove or revise access rights immediately if the job role changes or a staff member leaves the business process area. Periodically review to ensure that the access is appropriate for the current threats, risk, technology and business need. | **Level 3** |
| 5 | 5. On a regular basis, provide awareness and training regarding roles and responsibilities so that everyone understands their responsibilities; the importance of controls; and the security, integrity, confidentiality and privacy of company information in all its forms. | **Level 3** |
| 6 | 6. Ensure administrative privileges are sufficiently and effectively secured, tracked and controlled to prevent misuse. | **Level 3** |
| 7 | 7. Periodically review access control definitions, logs and exception reports. Ensure that all access privileges are valid and aligned with current staff members and their allocated roles. | **Level 4** |

**Standar & Panduan Terkait (Related Guidance):**
- HITRUST CSF version 9, September 2017 13.04 Collection, Use and Disclosure
- ISO/IEC 27002:2013/Cor.2:2015(E) 7. Human resource security
- The CIS Critical Security Controls for Effective Cyber Defense Version
- 6.1, August 2016
- CSC 5: Controlled Use of Administrative Privileges
- Management Practice Example Metrics

#### DSS06.04 — Manage errors and exceptions

> **Deskripsi Praktik:** Manage business process exceptions and errors and facilitate remediation, executing defined corrective actions and escalating as necessary. This treatment of exceptions and errors provides assurance of the accuracy and integrity of the business information process.

**Contoh Metrik Praktik (Example Metrics):**
- a. Frequency of processing inefficiencies due to incomplete data entry
- b. Number of errors detected in a timely manner
- c. Number of data processing errors that were efficiently remediated

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Review errors, exceptions and deviations. | **Level 2** |
| 2 | 2. Follow up, correct, approve and resubmit source documents and transactions. | **Level 2** |
| 3 | 3. Maintain evidence of remedial actions. | **Level 2** |
| 4 | 4. Define and maintain procedures to assign ownership for errors and exceptions, correct errors, override errors and handle out-of-balance conditions. | **Level 3** |
| 5 | 5. Report relevant business information process errors in a timely manner to perform root cause and trending analysis. | **Level 4** |

**Standar & Panduan Terkait (Related Guidance):**
- Management Practice Example Metrics

#### DSS06.05 — Ensure traceability and accountability for information events

> **Deskripsi Praktik:** Ensure that business information can be traced to an originating business event and associated with accountable parties. This discoverability provides assurance that business information is reliable and has been processed in accordance with defined objectives.

**Contoh Metrik Praktik (Example Metrics):**
- a. Number of incidents in which transaction history cannot be recovered
- b. Percent of completeness of traceable transaction log

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Capture source information, supporting evidence and the record of transactions. | **Level 2** |
| 2 | 2. Define retention requirements, based on business requirements, to meet operational, financial reporting and compliance needs. | **Level 3** |
| 3 | 3. Dispose of source information, supporting evidence and the record of transactions in accordance with the retention policy. | **Level 3** |

**Standar & Panduan Terkait (Related Guidance):**
- Management Practice Example Metrics

#### DSS06.06 — Secure information assets

> **Deskripsi Praktik:** Secure information assets accessible by the business through approved methods, including information in electronic form (e.g., portable media devices, user applications and storage devices, or other methods that create new assets in any form), information in physical form (e.g., source documents or output reports) and information during transit. This benefits the business by providing end-to-end safeguarding of information.

**Contoh Metrik Praktik (Example Metrics):**
- a. Cases of sensitive transaction data delivered to wrong recipient
- b. Frequency of compromised integrity of critical data

**Daftar Lengkap Aktivitas & Target Level Kapabilitas (CMMI 2–5):**

| No. | Aktivitas Praktik Resmi COBIT 2019 | Capability Level |
| :---: | :--- | :---: |
| 1 | 1. Restrict use, distribution and physical access of information according to its classification. | **Level 2** |
| 2 | 2. Provide acceptable use awareness and training. | **Level 2** |
| 3 | 3. Apply data classification and acceptable use and security policies and procedures to protect information assets under the control of the business. | **Level 3** |
| 4 | 4. Identify and implement processes, tools and techniques to reasonably verify compliance. | **Level 3** |
| 5 | 5. Report to business and other stakeholders on violations and deviations. | **Level 4** |

**Standar & Panduan Terkait (Related Guidance):**
- CMMI Cybermaturity Platform, 2018 AC.MP Manage Access Permissions
- The CIS Critical Security Controls for Effective Cyber Defense Version
- 6.1, August 2016
- CSC 18: Application Software Security

### 3. Komponen B: Struktur Organisasi & Matriks RACI (DSS06)

| Kode Praktik | Nama Praktik | Accountable (A) — Penanggung Jawab Tunggal | Responsible (R) — Pelaksana Operasional |
| :--- | :--- | :--- | :--- |
| `DSS06.01` | Align control activities embedded in business processes with enterprise objectives | **I&T Governance Board** | Business Process Owners, Executive Committee |
| `DSS06.02` | Control the processing of information | **I&T Governance Board** | Business Process Owners, Chief Information Security Officer, Chief Information Officer, Data Mgmt Function, Legal Counsel |
| `DSS06.03` | Manage roles, responsibilities, access privileges and levels of authority | **I&T Governance Board** | Business Process Owners, Chief Information Security Officer, Chief Information Officer, Information Security Manager |
| `DSS06.04` | Manage errors and exceptions | **Business Process Owners** | Chief Information Security Officer, Chief Information Officer, Service Manager |
| `DSS06.05` | Ensure traceability and accountability for information events | **Business Process Owners** | Chief Information Security Officer, Chief Information Officer |
| `DSS06.06` | Secure information assets | **Business Process Owners** | Chief Information Security Officer, Chief Information Officer |

### 4. Komponen C, D, E, F, dan G (DSS06)

- **Komponen C — Aliran & Item Informasi (Information Flows and Items):**
  - Ringkasan Input/Output Praktik: `(see also Section 3.6) ; Management Practice Inputs Outputs ; DSS06.01 Align control activities embedded in business ; processes with enterprise objectives. ; From Description Description To ; APO01.07 •  Data classification ; guidelines ; •  Data integrity ; procedures ; Root cause analyses and ; recommendations ; BAI06.01; ; MEA02.04; ; MEA04.04; ; MEA04.06; ; MEA04.07 ; Results of processing ; effectiveness reviews`
- **Komponen D — SDM, Keterampilan & Kompetensi (People, Skills and Competencies — SFIA V6 / e-CF):**
  - Referensi Kompetensi: `Skill Related Guidance (Standards, Frameworks, Compliance Requirements) Detailed Reference | Information security Skills Framework for the Information Age V6, 2015 SCTY | Security administration Skills Framework for the Information Age V6, 2015 SCAD`
- **Komponen E — Kebijakan & Prosedur (Policies and Procedures):**
  - Kebijakan Kunci: `Relevant Policy Policy Description Related Guidance Detailed Reference | Business controls guidance Defines business process controls | to ensure proper control and | reduce risk of fraud and errors. | Identifies manual controls to | protect documents (e.g., source, | input, processing and output | documents); identifies supervisory | controls to review the flow of | documents and ensure correct | processing. Includes I&T general | controls (e.g., physical security,`
- **Komponen F — Budaya, Etika & Perilaku (Culture, Ethics and Behavior):**
  - Elemen Budaya: `Key Culture Elements Related Guidance Detailed Reference | Create a culture that embraces the need for sound controls in business | processes, building them into applications in development or requiring | them in applications bought or accessed as a service. Encourage all | employees to have a controls consciousness to protect all assets of the | organization (e.g., paper records and facilities).`
- **Komponen G — Layanan, Infrastruktur & Aplikasi (Services, Infrastructure and Applications):**
  - Automated application controls
  - Event log auditing tools
  - 4.5 Monitor, Evaluate and Assess (MEA)
  - 01 Managed Performance and Conformance Monitoring
  - 02	 Managed	System	of	Internal	Control
  - 03	 Managed	Compliance	With	External	Requirements
  - 04 Managed Assurance

### 5. Program Kerja Audit TI (Kertas Kerja Audit / KKA) — DSS06

- **Fokus Pengujian Audit:** Pengelolaan Kontrol Proses Bisnis (Business Process Controls): kontrol aplikasi (Input, Processing, Output), pemisahan tugas (SoD) di dalam aplikasi, dan pengamanan aset informasi.
- **Daftar Permintaan Dokumen Bukti (PBC — *Provided by Client*):**
  1. Dokumentasi kontrol terprogram pada aplikasi inti (validasi input, batas transaksi, kontrol rekonsiliasi otomatis, dan log jejak audit aplikasi).
  1. Matriks hak akses aplikasi (Role-Based Access Control / RBAC Matrix) dan aturan Segregation of Duties (SoD) antar fungsi bisnis.
  1. Laporan rekonsiliasi transaksi antarsistem (interface reconciliation), penanganan suspense account, dan log perubahan master data kritis.
- **Prosedur Pengujian Kontrol (Test of Design / ToD & Test of Operating Effectiveness / ToE):**
  - ToD: Evaluasi desain kontrol aplikasi (IT Application Controls / ITAC) untuk menjamin kelengkapan, akurasi, validitas, dan otorisasi transaksi sejak input hingga output.
  - ToE: Lakukan pengujian konflik Segregation of Duties (SoD) pada tabel hak akses pengguna aplikasi ERP/Core System (mis. pembuat vendor vs. penyetuju pembayaran) serta uji fungsi validasi otomatis aplikasi.
- **Indikator Temuan / Red Flags Audit:**
  - ⚠️ Pengguna bisnis memiliki kombinasi hak akses yang melanggar SoD di aplikasi (mis. dapat membuat master data pemasok sekaligus menyetujui pencairan pembayaran).
  - ⚠️ Perubahan pada parameter bunga/harga atau saldo langsung dilakukan lewat backend database (direct DB update) dengan melewati kontrol aplikasi.

---
