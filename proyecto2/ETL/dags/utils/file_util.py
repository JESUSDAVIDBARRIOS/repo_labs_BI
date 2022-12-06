import pandas as pd
import os

def cargar_datos(name):
    df = pd.read_csv("/opt/airflow/data/" + name + ".csv", sep=',', encoding = 'latin1', index_col=False)
    return df

def guardar_datos(df, nombre):
    df.to_csv("/opt/airflow/data/" + nombre + ".csv" , encoding = 'latin1', sep=',', index=False)  
    
    
def procesar_datos():
    
    ## Dimension city
    city = pd.read_csv("http://bigdata-cluster4-01.virtual.uniandes.edu.co:50070/webhdfs/v1/user/monitorbi/datalakeBI/dimension_city.csv?op=OPEN&user.name=cursobi13", sep=',', encoding = 'latin1', index_col=False)
    # To Do: Limpiar los datos y guardarlos
    city.drop('row ID', axis=1, inplace=True)
    city.drop_duplicates(inplace=True)
    for col in city.columns:
        if city[col].dtype == 'int64' or city[col].dtype == 'float64':
            city[col] = city[col].fillna(0)
        else:
            city[col] = city[col].fillna("")
    guardar_datos(city, "dimension_city")

    ## Dimension Customer
    customer = pd.read_csv("http://bigdata-cluster4-01.virtual.uniandes.edu.co:50070/webhdfs/v1/user/monitorbi/datalakeBI/dimension_customer.csv?op=OPEN&user.name=cursobi13", sep=',', encoding = 'latin1', index_col=False)
    # To Do: Limpiar los datos y guardarlos
    for col in customer.columns:
        if customer[col].dtype == 'int64' or customer[col].dtype == 'float64':
            customer[col] = customer[col].fillna(0)
        else:
            customer[col] = customer[col].fillna("")
    customer.drop_duplicates(inplace=True)
    customer['Customer'] = customer['Customer'].str.replace('\'', '')
    customer['Postal_Code'] = customer['Postal_Code'].astype('int64')
    guardar_datos(customer, "dimension_customer")
    
    ## Dimension Date
    date = pd.read_csv("http://bigdata-cluster4-01.virtual.uniandes.edu.co:50070/webhdfs/v1/user/monitorbi/datalakeBI/dimension_date.csv?op=OPEN&user.name=cursobi13", sep=',', encoding = 'latin1', index_col=False)
    # To Do: Limpiar los datos y guardarlos
    for col in date.columns:
        if date[col].dtype == 'int64' or date[col].dtype == 'float64':
            date[col] = date[col].fillna(0)
        else:
            date[col] = date[col].fillna("")
    date.drop_duplicates(inplace=True)
    guardar_datos(date, "dimension_date")

    ## Dimension Employee
    employee = pd.read_csv("http://bigdata-cluster4-01.virtual.uniandes.edu.co:50070/webhdfs/v1/user/monitorbi/datalakeBI/dimension_employee.csv?op=OPEN&user.name=cursobi13", sep=',', encoding = 'latin1', index_col=False)
    # To Do: Limpiar los datos y guardarlos
    employee.drop_duplicates(inplace=True)
    for col in employee.columns:
        if employee[col].dtype == 'int64' or employee[col].dtype == 'float64':
            employee[col] = employee[col].fillna(0)
        else:
            employee[col] = employee[col].fillna("")
    guardar_datos(employee, "dimension_employee")

    ## Dimension Stock item
    stock_item = pd.read_csv("http://bigdata-cluster4-01.virtual.uniandes.edu.co:50070/webhdfs/v1/user/monitorbi/datalakeBI/dimension_stock_item.csv?op=OPEN&user.name=cursobi13", sep=',', encoding = 'latin1', index_col=False)
    # To Do: Limpiar los datos y guardarlos
    for col in stock_item.columns:
        if stock_item[col].dtype == 'int64' or stock_item[col].dtype == 'float64':
            stock_item[col] = stock_item[col].fillna(0)
        else:
            stock_item[col] = stock_item[col].fillna("")
    stock_item.drop_duplicates(inplace=True)
    stock_item['Tax_Rate'] = stock_item['Tax_Rate'].str.replace(',', '.')
    stock_item['Unit_Price'] = stock_item['Unit_Price'].str.replace(',', '.')
    stock_item['Recommended_Retail_Price'] = stock_item['Recommended_Retail_Price'].str.replace(',', '.')
    stock_item['Typical_Weight_Per_Unit'] = stock_item['Typical_Weight_Per_Unit'].str.replace(',', '.')
    stock_item['Stock_Item'] = stock_item['Stock_Item'].str.replace('\'', '')

    guardar_datos(stock_item, "dimension_stock_item")
    
    ## Fact Table
    fact_order = pd.read_csv("http://bigdata-cluster4-01.virtual.uniandes.edu.co:50070/webhdfs/v1/user/monitorbi/datalakeBI/fact_order.csv?op=OPEN&user.name=cursobi13", sep=',', encoding = 'latin1', index_col=False)
    # To Do: Limpiar los datos y guardarlos
    for col in fact_order.columns:
        if fact_order[col].dtype == 'int64' or fact_order[col].dtype == 'float64':
            fact_order[col] = fact_order[col].fillna(0)
        else:
            fact_order[col] = fact_order[col].fillna("")
    fact_order.drop_duplicates(inplace=True)
    guardar_datos(fact_order, "fact_order")


