#Fun Little MCP Application

So, I kinda got curious about the buzz around Model Context Protocol and made one using Claude and a local sqlite database.. Gotta say tat its cool

It includes:
- A script to generate a **dummy sales dataset** with names, regions, amounts, and dates.
- An **MCP server** to interact with this data using intelligent analysis tools and prompt-based insights.
- **Two demo videos** showcasing core functionality and advanced upgrades.

---

## 🛠 `app.py`: Sales Dataset Generator

This file generates a dummy dataset `sale.db` using SQLite. Here's what it does:

- Creates a table named `sales` with fields:
  - `customer_name`, `region`, `amount`, `date`
- Fills 100 entries with:
  - Random customer names, regions (`North`, `South`, `East`, `West`)
  - Random amounts in ₹ (Indian Rupees)
  - Random dates within the last 6 months
- Adds some **intentional duplicates and inconsistencies** (extra spaces, uppercase names) to simulate real-world data issues

## ⚙️ `main.py`: MCP Server + Data Insights

This script powers the Claude Desktop MCP server and enables interactive business intelligence (BI) through **tools**, **prompts**, and **resources**.

### Key Features

✅ Connects to the `sale.db`  
✅ Exposes schema and metadata  
✅ Performs BI summaries, trends, and segmentation  
✅ Detects duplicates  
✅ Uses **MCP Tools**, **MCP Prompts**, and **MCP Resources**

### Tools and Prompts 

| Tool Name               | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| `get_schema`            | MCP resource: Returns raw SQL schema of the `sales` table                  |
| `get_column_types`      | Lists columns and their types using SQLite `PRAGMA`                        |
| `get_summary`           | Total record count + first 5 sample rows                                   |
| `detect_duplicates`     | Finds repeated `customer_name` + `date` combinations                       |
| `business_summary`      | AI-generated business summary using all sales records                     |
| `customer_segmentation` | Segments customers into low, medium, and high spenders                    |
| `kpi_analysis`          | Returns total revenue, average sale, and top-performing regions           |
| `generate_bi_questions` | AI generates potential business questions based on dataset                |
| `dynamic_trend_analysis`| Trends over last 3 months and by region                                    |
| `explain_sales_trend`   | Breaks down sales patterns over time                                       |

I tried 4-5 of these and worked until the claude free trail ended . Will update  when I verify that every tools work.

### How to Run MCP Server

Make sure the database (`sale.db`) is created first:
```bash
python app.py
```

Then, start the MCP app:
```bash
python main.py
```

---

## Guide to do the MCP 
- [MCP](https://modelcontextprotocol.io)
- [Github Python SDK](https://github.com/modelcontextprotocol/python-sdk/tree/main)
- [TECHWITHTIM](https://github.com/techwithtim/PythonMCPServer)
## 🧠 Why This Is Awesome

- Uses Model Context Protocol for powerful local AI workflows
- Completely extensible — plug more prompts/tools as needed


I have to say thanks to [TechwithTim](https://www.youtube.com/watch?v=-8k9lGpGQ6g) video about it, which gave me understanding of the capabilities of MCP Server

