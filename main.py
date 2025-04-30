import sqlite3
from mcp.server.fastmcp import FastMCP
from datetime import datetime
import os

DB_FILE = os.path.join(os.path.dirname(__file__), "sale.db")
mcp = FastMCP("Final Sales")

# ---------------------- Schema Tools ----------------------

@mcp.resource("schema://sale.db")
def get_schema() -> str:
    with sqlite3.connect(DB_FILE) as conn:
        schema = conn.execute(
            "SELECT sql FROM sqlite_master WHERE type='table'"
        ).fetchall()
    return "\n".join(sql[0] for sql in schema if sql[0])

@mcp.tool()
def get_column_types() -> str:
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.execute("PRAGMA table_info(sales)")
        cols = cursor.fetchall()
    return "Columns:\n" + "\n".join(f"{col[1]} ({col[2]})" for col in cols)

# ---------------------- Basic Stats & Summaries ----------------------

@mcp.tool()
def get_summary() -> str:
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        total = cursor.execute("SELECT COUNT(*) FROM sales").fetchone()[0]
        rows = cursor.execute("SELECT * FROM sales LIMIT 5").fetchall()
    return f"Total records: {total}\nSample:\n" + "\n".join(str(r) for r in rows)

@mcp.tool()
def detect_duplicates() -> str:
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        rows = cursor.execute("""
            SELECT customer_name, date, COUNT(*)
            FROM sales
            GROUP BY customer_name, date
            HAVING COUNT(*) > 1
        """).fetchall()
    return (
        "Duplicate entries by customer_name/date:\n" +
        "\n".join(str(r) for r in rows)
    )

# ---------------------- Business Intelligence Prompts ----------------------

@mcp.prompt()
def summary_prompt() -> str:
    with sqlite3.connect(DB_FILE) as conn:
        rows = conn.execute("SELECT * FROM sales").fetchall()
    return f"Give a business summary of this sales data: {rows}"

@mcp.tool()
def business_summary() -> str:
    return summary_prompt()

@mcp.prompt()
def customer_segment_prompt() -> str:
    with sqlite3.connect(DB_FILE) as conn:
        rows = conn.execute("SELECT customer_name, amount FROM sales").fetchall()
    return f"Based on these sales amounts by customer, can you segment customers into high, medium, and low spenders? Data: {rows}"

@mcp.tool()
def customer_segmentation() -> str:
    return customer_segment_prompt()

@mcp.prompt()
def stats_prompt() -> str:
    with sqlite3.connect(DB_FILE) as conn:
        rows = conn.execute("SELECT region, amount FROM sales").fetchall()
    return (
        "Give total revenue, average sale, "
        f"and top 3 regions based on this data: {rows}"
    )

@mcp.tool()
def kpi_analysis() -> str:
    return stats_prompt()

@mcp.prompt()
def question_prompt() -> str:
    with sqlite3.connect(DB_FILE) as conn:
        rows = conn.execute("SELECT * FROM sales").fetchall()
    return f"Given this data: {rows}, what are some insightful questions I can ask?"

@mcp.tool()
def generate_bi_questions() -> str:
    return question_prompt()

@mcp.prompt()
def dynamic_analysis_prompt() -> str:
    with sqlite3.connect(DB_FILE) as conn:
        rows = conn.execute("SELECT region, date, amount FROM sales").fetchall()
    return f"Analyze this for trends over the last 3 months and region-wise performance: {rows}"

@mcp.tool()
def dynamic_trend_analysis() -> str:
    return dynamic_analysis_prompt()

@mcp.prompt()
def trend_explanation_prompt() -> str:
    with sqlite3.connect(DB_FILE) as conn:
        rows = conn.execute("SELECT date, amount FROM sales").fetchall()
    return f"Can you explain monthly or weekly sales trends based on this data: {rows}?"

@mcp.tool()
def explain_sales_trend() -> str:
    return trend_explanation_prompt()

# ---------------------- Entry Point ----------------------

if __name__ == "__main__":
    if not os.path.exists(DB_FILE):
        raise FileNotFoundError(
            "Run app.py to create and populate the sales_data.db first."
        )
    mcp.run()
