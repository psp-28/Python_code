import pandas as pd
 
# Function to read and process sales data
def generate_sales_summary(input_file, output_file):
    try:
        # Read Excel file
        df = pd.read_excel(input_file)
        print(df)
        # Group by 'Product Category' and sum 'Sales Amount'
        summary_df = df.groupby('Product Category')['Sales Amount'].sum().reset_index()
        # Write summary to new Excel file
        summary_df.to_excel(output_file, index=False)
        print(f"Summary report generated successfully: {output_file}")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")
 
# Example usage:
generate_sales_summary('C:\\PyDemos\\sales_data.xlsx', 'C:\\PyDemos\\sales_summary.xlsx')