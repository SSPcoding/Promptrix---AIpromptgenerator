import streamlit as st 
import google.generativeai as genai


# ========================
# 🤖 Prompt Generator
# ========================
def generate_prompt(role, output_type, description, target, constraints):
    model = genai.GenerativeModel("gemini-1.5-flash")
    input_text = f"""
    You are a Prompt Engineering Assistant.
    
    Role: {role}
    Category: {output_type}
    Description: {description}
    Target Audience: {target}
    Constraints: {constraints}

    Generate ONLY a highly precise, context-aware, well-structured PROMPT
    that will work effectively with any GenAI model like Gemini, ChatGPT, or Claude.
    Do not answer the task — only return the optimized prompt itself.
    """
    response = model.generate_content(input_text)
    return f"Your role is of {role}\n Your task is to {response.text}" or "⚠️ No prompt generated."

def improve_prompt(existing_prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    input_text = f"""
    You are a Prompt Critic and Optimizer.

    Here is a prompt:
    {existing_prompt}

    Improve it by making it more clear, structured, and optimized for best results.
    """
    response = model.generate_content(input_text)
    return response.text or "⚠️ No improved version generated."

