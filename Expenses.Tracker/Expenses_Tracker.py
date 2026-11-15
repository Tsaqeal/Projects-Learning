from datetime import date
import pandas as pd
from supabase import create_client
import streamlit as st

st.set_page_config(
    page_title="SQL Expenses Tracker", page_icon="📊", layout="wide"
)

# --- 1. CONNECT TO SUPABASE ---
@st.cache_resource
def init_connection():
  url = st.secrets["supabase"]["url"]
  key = st.secrets["supabase"]["key"]
  return create_client(url, key)


supabase = init_connection()

# --- 2. PASSWORD PROTECTION ---
if "authenticated" not in st.session_state:
  st.session_state.authenticated = False

if not st.session_state.authenticated:
  st.title("🔒 Login Required")
  password = st.text_input("Enter Password", type="password")
  if st.button("Unlock", use_container_width=True):
    if password == st.secrets.get("app_password", "YourSecretPasswordHere"):
      st.session_state.authenticated = True
      st.rerun()
    else:
      st.error("Incorrect password")
  st.stop()

# --- 3. MAIN DASHBOARD UI ---
st.title("📊 SQL Expenses & Financials Dashboard")

# Input Form in Sidebar
with st.sidebar:
  st.subheader("➕ Add New Expense")
  with st.form("expense_form", clear_on_submit=True):
    expense_date = st.date_input("Date", value=date.today())
    amount = st.number_input("Amount (£)", min_value=0.01, format="%.2f")
    reason = st.text_input("Reason", placeholder="e.g., Groceries, Coffee")

    submitted = st.form_submit_button("Save to Database", use_container_width=True)

  if submitted:
    if not reason.strip():
      st.error("Please enter a reason.")
    else:
      try:
        supabase.table("expenses").insert({
            "date": str(expense_date),
            "amount": float(amount),
            "reason": reason.strip(),
        }).execute()
        st.success("Saved successfully!")
        st.rerun()
      except Exception as e:
        st.error(f"Error saving data: {e}")

# --- 4. FETCH AND DISPLAY DATA FROM SQL ---
response = (
    supabase.table("expenses").select("*").order("date", desc=True).execute()
)
data = response.data

if data:
  df = pd.DataFrame(data)

  total_spent = df["amount"].sum()
  total_transactions = len(df)

  col1, col2 = st.columns(2)
  col1.metric(label="Total Spent", value=f"£{total_spent:,.2f}")
  col2.metric(label="Total Transactions", value=total_transactions)

  st.divider()

  st.subheader("Spending Over Time")
  df["date"] = pd.to_datetime(df["date"])
  chart_df = df.groupby("date")["amount"].sum().reset_index()
  st.line_chart(chart_df, x="date", y="amount", use_container_width=True)

  st.divider()
  st.subheader("All Records")
  st.dataframe(df, use_container_width=True)
else:
  st.info("No expenses recorded in the database yet. Add one using the sidebar!")