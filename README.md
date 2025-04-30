# 🧠 Sales Insights ChatApp using Claude + MCP

This project showcases a fully functional **AI-powered Business Intelligence assistant** that interacts with a SQLite sales dataset using **Natural Language Commands**. It is built using [MCP (Modular Chat Prompting)](https://github.com/mayooear/mcp) and uses **Claude Desktop** as the LLM backend.

---

## 🔧 Overview

- `app.py` creates a **dummy sales dataset** (`sale.db`) with:
  - `customer_name` (with variations like upper case, trailing spaces),
  - `region` (North, South, East, West),
  - `amount` (in ₹),
  - `date` (last 6 months).
  - Also includes **duplicate entries** for testing detection logic.

- `main.py` launches a **FastMCP** server, exposing tools and prompts that let Claude interact intelligently with the dataset:
  - Ask for summaries, insights, KPIs, customer segments, trends, etc.
  - Uses `@mcp.tool`, `@mcp.prompt`, and `@mcp.resource` decorators.

---

## 📂 Files

### `app.py`
- Creates a SQLite database `sale.db` with 100 dummy records.
- Adds slight inconsistencies in names for real-world simulation.
- Inserts known duplicate records (e.g., Bob on 01-12-2024).
- Run this once before launching the server:
  
  ```bash
  python app.py
