#PROMPT

# 1. sales data 

# SalesData_mmddyyy.txt
# date, salesmandid, quantity, price 


# 2. salesMan data 

# SalesMan.txt 
# salesmanid, name, DOB

# 3. Task 
# calcuate Daily aggregates to CSV File


# 4. PSEDU-CODE 
#   1. read File 1
#   2. read file 2
#   3. Transformation 1
#       - create column totalSales = Quantity* price with UDF
#   4.  Transformation 2
#       - aggregate on the basis of   date, salesmandid
#   5. join on the basis of salesmandid

#   6.Show output as following 
#   Date, alesmanID,name,totalSales
#       11/09/2024,123,Vishal,3000
#       11/09/2024,345,Praketa,360

# 5. CODE
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import DoubleType

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("SalesDataAnalysis") \
    .getOrCreate()

# File paths
sales_data_path = "path/to/SalesData_mmddyyy.txt"
salesman_data_path = "path/to/SalesMan.txt"

# Read the sales data
sales_df = spark.read.csv(sales_data_path, header=True, inferSchema=True)

# Read the salesman data
salesman_df = spark.read.csv(salesman_data_path, header=True, inferSchema=True)

# Define UDF to calculate total sales
def calculate_total_sales(quantity, price):
    return quantity * price

#Register the UDF
total_sales_udf = udf(calculate_total_sales, DoubleType())

# Apply UDF to add totalSales column
sales_with_total_df = sales_df.withColumn("totalSales", total_sales_udf(col("quantity"), col("price")))

# Aggregate data by date and salesmandid
aggregated_df = sales_with_total_df.groupBy("date", "salesmandid") \
    .agg(sum("totalSales").alias("totalSales"))

# Join with salesman data to get names
final_df = aggregated_df.join(salesman_df, aggregated_df.salesmandid == salesman_df.salesmanid, "inner") \
    .select(
        aggregated_df.date,
        aggregated_df.salesmandid,
        salesman_df.name,
        aggregated_df.totalSales
    )

# Show the output
final_df.show()

# Stop the SparkSession
spark.stop()
