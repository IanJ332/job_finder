import pandas as pd

# Step 1: 读取Excel文件，使用原始字符串r来避免转义字符错误
file_path = r'C:\Users\User\Desktop\TheFiles\job_finder\LCA_Disclosure_Data_FY2024_Q3.xlsx'

# Step 2: 读取文件并创建DataFrame
df = pd.read_excel(file_path)

# Step 3: 提取支持H-1B申请的公司
# 选择'EMPLOYER_NAME'列，过滤'SUPPORT_H1B'列为'Yes'的行
companies = df[df['SUPPORT_H1B'] == 'Yes']['EMPLOYER_NAME'].dropna().unique()

# Step 4: 将公司名单写入txt文件
with open('h1_support_company.txt', 'w') as f:
    for company in companies:
        f.write(company + '\n')

print("公司名单已成功生成并保存到 h1_support_company.txt 文件中！")
