import pandas as pd
from fpdf import FPDF

# Function to read data from a CSV file
def read_data(file_path):
    return pd.read_csv(file_path)

# Function to analyze data
def analyze_data(df):
    summary = {
        'Total Rows': len(df),
        'Total Columns': len(df.columns),
        'Column Names': df.columns.tolist(),
        'Data Types': df.dtypes.to_dict(),
        'Missing Values': df.isnull().sum().to_dict(),
        'Description': df.describe().to_dict()
    }
    return summary

# Function to generate PDF report
def generate_pdf_report(data, output_path):
    pdf = FPDF()
    pdf.add_page()
    
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Data Analysis Report", ln=True, align='C')
    
    pdf.ln(10)
    
    pdf.cell(200, 10, txt="Summary:", ln=True, align='L')
    pdf.ln(5)
    
    for key, value in data.items():
        if isinstance(value, dict):
            pdf.cell(200, 10, txt=f"{key}:", ln=True, align='L')
            for sub_key, sub_value in value.items():
                pdf.cell(200, 10, txt=f"  {sub_key}: {sub_value}", ln=True, align='L')
        else:
            pdf.cell(200, 10, txt=f"{key}: {value}", ln=True, align='L')
        pdf.ln(5)
    
    pdf.output(output_path)
    
if __name__ == "__main__":
    # Example: Replace 'data.csv' with your data file
    file_path = 'data.csv'
    output_path = 'report.pdf'
    
    df = read_data(file_path)
    analysis = analyze_data(df)
    generate_pdf_report(analysis, output_path)
