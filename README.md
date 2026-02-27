# FHIR-EHR-QC: Making Pathogen Genome Data Interoperable with Patient Health Records

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FHIR Standard](https://img.shields.io/badge/FHIR-R4%20%2F%20R5-green.svg)](https://www.hl7.org/fhir/)

**FHIR-EHR-QC** is a comprehensive framework designed to harmonise pathogen genomic data and patient Electronic Health Records (EHR). By leveraging the **HL7 FHIR** standard, this tool facilitates the development of integrated data representations, interactive visualizations, and harmonized data matrices suitable for multimodal machine learning workflows.

---

## 🚀 Key Features

* **Integrated Representation**: Combines EHR with high-resolution pathogen genomic information.
* **Bidirectional Interoperability**: Supports `FHIR-to-DB` bidirectional transfers and incremental data loading to keep systems in sync.
* **Research-Ready Export**: Generates harmonized data matrices (Demographics, Measurements, and Genomics) ready for Machine Learning.
* **Interactive Visualization**: A web-based application for exploratory analysis of genomic information and AMR summaries.

---

## 🛠 System Architecture

![Schematic Overview](images/schematic_representation.png)

The framework is composed of two primary components:
1.  **Ingestion/Extraction Utility**: A Python CLI tool driven by `AppConfig` (connection details) and `RunConfig` (workflow logic).
2.  **Web-Based Insights App**: An interactive dashboard for real-time visualization of risk scores, admission dates, and genomic summaries.

---

## 📋 Prerequisites

* **Python**: 3.8 or higher
* **Node.js**: (For the web visualization dashboard)
* **FHIR Server**: Access to a server (e.g., HAPI FHIR, Azure API for FHIR)
* **Database**: Access to a relational database (optional, for ingestion modules)

---

## 📖 Documentation

For detailed installation guides, API references, and comprehensive usage tutorials, please visit our official documentation:

👉 **[https://ehr-int-tutorial.readthedocs.io/en/latest/index.html](https://ehr-int-tutorial.readthedocs.io/en/latest/index.html)**

## 📝 Statement of Need

Accurate modeling of infectious diseases requires high-resolution datasets integrating both pathogen-specific genomic traits and host-specific clinical responses. While FHIR provides a robust platform for data harmonization, existing tools often lack support for relational EHR ingestion or bidirectional genomic data flow. FHIR-EHR-QC addresses these gaps by offering a flexible, modular utility that supports all FHIR resources and OMOP-CDM versions.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue for:

New FHIR resource templates.

Support for additional relational database schemas.

Improved visualization widgets.

## 🎓 Citation

If you use this software in your research, please cite:

Yashpal Ramakrishnaiah, et al. (2026). FHIR-EHR-QC: Making Pathogen Genome Data Interoperable with Patient Health Records. (**Unpublished**)

## 📧 Contact

For questions, feedback, or collaborations, please contact:

Sonika Tyagi: sonika.tyagi@rmit.edu.au

## 🙏 Acknowledgments

We acknowledge the following individuals and organizations for their support:

**Funding**: ST acknowledges funding support from (??). YR received the Monash Graduate Scholarship for his PhD.

**Standards**: The FHIR and OMOP communities for developing and providing crucial data representation standards.

**Open Source**: The developers of Gosling, React, and Material UI, which were instrumental in the development of the framework.

**Resources**: The ARDC Nectar Research Cloud for providing the computational resources necessary for this project.

<img width="150" alt="monash" src="https://github.com/user-attachments/assets/befc1ae6-eb52-46b4-a9a9-4507549da95f" />

<img width="150" alt="superbugai" src="https://github.com/user-attachments/assets/f26d1d49-1ffb-433b-b593-0fc67604a7c1" />

<img width="150" alt="alfred" src="https://github.com/user-attachments/assets/7e9deedf-992e-4f2e-a3f4-6aa883c85b89" />

<img width="150" alt="rmit" src="https://github.com/user-attachments/assets/d2bfed0b-02b4-4777-a44f-532ac46a9553" />
