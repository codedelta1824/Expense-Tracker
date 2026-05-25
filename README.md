# ExpenseTracker

## A Decoupled Local Expense Tracking & Analytical Framework

ExpenseTracker is a modular desktop application engineered around a clean separation of concerns and subsystem isolation principles.

The project combines:

- Python for transaction validation, in-memory state representation, dynamic calculations, and storage access pipelines
- Tkinter for a lightweight, zero-dependency, native desktop graphical interface

ExpenseTracker demonstrates how desktop applications can be architected using a decoupled software design methodology where:

- UI systems remain isolated from computational logic
- File I/O pipelines remain abstracted away from rendering layers
- Internal state management is separated from user interaction systems
- Computational operations never directly bleed into presentation or storage layers

---

# Core Objectives

The primary goals of ExpenseTracker are:

- Maintain real-time transactional session state in memory
- Calculate cumulative expense metrics dynamically during runtime
- Serialize internal ledger data safely to local persistent storage
- Validate user-provided inputs using strict exception-safe validation pipelines
- Isolate presentation, orchestration, computation, and physical storage subsystems
- Export internal transaction sheets into parseable and analytically compatible formats
- Demonstrate modular desktop application engineering using decoupled architectural practices

---

# Architecture Philosophy

ExpenseTracker follows a subsystem-oriented modular architecture where each file represents an isolated business, utility, rendering, or storage layer.

A centralized execution model is used where a single entry point manages:

- Application bootstrap initialization
- Dependency injection
- Runtime orchestration
- Lifecycle management
- Cross-module communication routing

The project is intentionally designed around the following principles:

- Strict modular architecture
- Centralized execution entry model
- In-memory transactional representation
- Robust file I/O separation
- Isolated business logic processing
- Minimal subsystem coupling
- Explicit runtime responsibility segregation

---

# Key Capabilities

ExpenseTracker includes the following capabilities:

- Asynchronous and automated transactional logging
- Dynamic runtime aggregation of cumulative spending totals
- Flexible local flat-file storage pipelines
- Clean and crash-resistant exception containment
- Structured programmatic exporting of ledger entries
- Adaptive GUI presentation targeting both native and upgraded display densities
- Decoupled dependency injection methodology
- Real-time ledger state synchronization
- Lightweight desktop deployment without external runtime dependencies

---

# Repository Structure

```text
ExpenseTracker/
│
├── README.md
│
├── Program Files/
│   ├── ExpenseTracker.py
│   ├── GUI.py
│   ├── Engine.py
│   └── Storage.py
│
├── Data Files/
│   ├── data.json
│   └── export.csv
│
└── Docs/
    ├── System Design Overview.pdf
    └── UI Design Mockup.png
```

---

# Architecture Overview

```text
             +--------------------------------+
             |       ExpenseTracker.py        |
             |--------------------------------|
             | Application Bootstrapper       |
             | Dependency Injector            |
             | Lifecycle Orchestrator         |
             +---------------+----------------+
                             |
                             v
             +--------------------------------+
             |             GUI.py             |
             |--------------------------------|
             | Window Frames & Bounding Boxes |
             | Touch/Click Event Binding      |
             | Live List & Input Elements     |
             +---------------+----------------+
                             |
                             v
             +--------------------------------+
             |           Engine.py            |
             |--------------------------------|
             | Active Ledger State Processor  |
             | Real-time Transaction Totals   |
             | Validation Checking Logic      |
             +---------------+----------------+
                             |
                             v
             +--------------------------------+
             |           Storage.py           |
             |--------------------------------|
             | JSON File Read/Write Operations|
             | CSV Data Exporter Engine       |
             | Local State Serialization      |
             +--------------------------------+
```

---

# Module Responsibilities

## ExpenseTracker.py

Acts as the centralized application entry point responsible for:

- Runtime initialization
- Dependency construction
- Cross-module orchestration
- Application lifecycle management
- GUI startup sequencing

## GUI.py

Responsible for all user-facing graphical operations including:

- Window rendering
- Layout construction
- User interaction handling
- Input collection systems
- Dynamic visual updates

## Engine.py

Handles all computational and logical processing operations including:

- Transaction validation
- Ledger state management
- Dynamic expense calculations
- Runtime aggregation logic
- Exception-safe processing pipelines

## Storage.py

Provides persistent local storage abstraction including:

- JSON serialization pipelines
- CSV export operations
- File read/write management
- Local ledger persistence
- Structured storage formatting

---

# Design Characteristics

ExpenseTracker is intentionally engineered as a lightweight yet structurally scalable desktop framework.

The project emphasizes:

- Separation of concerns
- Predictable runtime behavior
- Reduced subsystem coupling
- Maintainable modular code organization
- Safe storage handling
- Explicit ownership of responsibilities across layers
- Simplified future scalability and extensibility

This architectural model allows the project to evolve into more advanced analytical or database-backed implementations without requiring major structural rewrites.

---

# Technologies Used

- Python
- Tkinter
- JSON
- CSV

---

# Project Status

ExpenseTracker is currently under active development.

Planned future improvements include:

- Advanced filtering systems
- Monthly and yearly analytics
- Category-based transaction grouping
- Visual chart rendering
- SQLite-backed storage systems
- Search and query pipelines
- Multi-window analytical dashboards

---

# Contact

For questions regarding contributions, architecture, implementation details, or repository-related discussions:

**Email:** codedelta1824@gmail.com

