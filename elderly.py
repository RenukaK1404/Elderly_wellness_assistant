import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import subprocess
import os
from datetime import datetime
from streamlit_lottie import st_lottie

# Function to load CSV files
def load_csv(file_path, columns):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        st.warning(f"CSV file not found: {file_path}")
        return pd.DataFrame(columns=columns)

# Load CSV files
daily_reminders = load_csv('daily_reminder.csv', ['Reminder Type', 'Scheduled Time', 'Reminder Sent (Yes/No)', 'Acknowledged (Yes/No)'])
health_monitoring = load_csv('health_monitoring.csv', ['Timestamp', 'Heart Rate', 'Glucose Levels', 'SPO2 Levels', 'Blood Pressure'])
safety_checklist = load_csv('safety_monitoring.csv', ['Movement Activity', 'Fall Detected (Yes/No)', 'Location', 'Alert Triggered (Yes/No)'])

# Function to call local LLM for advice
def get_advice(vitals):
    # This is a placeholder function. Replace with actual call to local LLM.
    advice = subprocess.run(['ollama', 'llama3', 'generate', f'Vitals: {vitals}'], capture_output=True, text=True)
    return advice.stdout

# Function to display Health Monitor page
def health_monitor():
    st.title("Health Monitor")

    # Input fields for vital signs
    heart_rate = st.number_input("Heart Rate (bpm)", min_value=30, max_value=200, step=1)
    glucose = st.number_input("Glucose Level (mg/dL)", min_value=50, max_value=300, step=1)
    spo2 = st.number_input("SPO2 Level (%)", min_value=70, max_value=100, step=1)

    # Display charts
    st.subheader("Vital Signs Chart")
    fig, ax = plt.subplots()
    ax.plot(["Heart Rate", "Glucose", "SPO2"], [heart_rate, glucose, spo2], marker='o')
    st.pyplot(fig)

    # Show latest 10 historical health data entries
    if not health_monitoring.empty:
        health_monitoring['Timestamp'] = pd.to_datetime(health_monitoring['Timestamp'])
        latest_data = health_monitoring.sort_values(by='Timestamp', ascending=False).head(10)
        latest_data['Alert'] = latest_data.apply(lambda row: '✅' if 60 <= row['Heart Rate'] <= 100 and row['Blood Pressure'] == 'Normal' else '🟥', axis=1)
        st.subheader("Latest Health Data (10 entries)")
        st.dataframe(latest_data[['Timestamp', 'Heart Rate', 'Glucose Levels', 'Oxygen Saturation (SpO₂%)']])



    else:
        st.write("No historical health data available.")

         # Predict Alert button
    if st.button("Check Health Status"):
        alerts = []
        if not (60 <= heart_rate <= 100):
            alerts.append("⚠ Heart Rate is abnormal!")
        if not (70 <= glucose <= 140):
            alerts.append("⚠ Glucose level is abnormal!")
        if spo2 < 90:
            alerts.append("⚠ SPO2 is below normal!")

        if alerts:
            st.error("Abnormal vitals detected:")
            for a in alerts:
                st.write(a)
        else:
            st.success("✅ All vitals are within the normal range.")

        # Optional: get local LLM advice
        vitals = {
            "Heart Rate": heart_rate,
            "Glucose": glucose,
            "SPO2": spo2
        }
        with st.spinner("🧠 Getting advice..."):
            advice = get_advice(vitals)
            st.info(f"LLM Advice:\n\n{advice}")


# Function to display Daily Reminders page
def daily_reminders_page():
    st.title("Daily Reminders")

    if 'acknowledged' not in st.session_state:
        st.session_state.acknowledged = daily_reminders['Acknowledged (Yes/No)'].copy()

    def mark_as_done(index):
        st.session_state.acknowledged[index] = 'Yes'

    for index, row in daily_reminders.iterrows():
        cols = st.columns([1, 2, 2, 1, 1])
        cols[0].write(row['Reminder Type'])
        cols[1].write(row['Scheduled Time'])
        cols[2].write('🟢' if st.session_state.acknowledged[index] == 'Yes' else '🔴')
        if st.session_state.acknowledged[index] == 'No':
            if cols[3].button("Mark as Done ✅", key=f"done_{index}"):
                mark_as_done(index)

# Function to display Safety Monitoring page
def safety_monitoring():
    st.title("Safety Monitoring")
    if not safety_checklist.empty:
        warnings = safety_checklist[['Movement Activity', 'Fall Detected (Yes/No)', 'Location', 'Alert Triggered (Yes/No)']]
        st.dataframe(warnings)
    else:
        st.write("No safety warnings available.")

# Function to display AI Assistant page
def ai_assistant():
    st.title("Talk to Assistant 🤖")
    st.write("Ask for advice or support from the assistant.")
    
    # Lottie animation placeholder
    lottie_url = "https://assets6.lottiefiles.com/packages/lf20_ydo1amjm.json"  # Sample Lottie URL
    st_lottie(lottie_url, height=200, key="assistant")

    if 'messages' not in st.session_state:
        st.session_state.messages = []

    def get_openai_response(user_input):
        # Placeholder for OpenAI response function
        response = subprocess.run(['ollama', 'llama3', 'generate', f'Question: {user_input}'], capture_output=True, text=True)
        return response.stdout

    user_input = st.text_input("Enter your question:")
    if user_input:
        response = get_openai_response(user_input)
        st.session_state.messages.append({"user": user_input, "assistant": response})

    for message in st.session_state.messages:
        st.chat_message("user").markdown(message["user"])
        st.chat_message("assistant").markdown(message["assistant"])

# Set up Streamlit UI
st.sidebar.title("Elderly Support Assistant")
tab = st.sidebar.radio("Navigation", ["Home", "Health Monitor", "Daily Reminders", "Safety Monitoring", "Talk to Assistant 🤖"])

# Home tab
if tab == "Home":
    st.title("Elderly Wellness Assistant")
    st.write("Welcome to the Elderly Support Assistant. Navigate through the tabs to monitor health, set reminders, ensure safety, and talk to your assistant.")

# Health Monitor tab
elif tab == "Health Monitor":
    health_monitor()

# Daily Reminders tab
elif tab == "Daily Reminders":
    daily_reminders_page()

# Safety Monitoring tab
elif tab == "Safety Monitoring":
    safety_monitoring()

# AI Assistant tab
elif tab == "Talk to Assistant 🤖":
    ai_assistant()