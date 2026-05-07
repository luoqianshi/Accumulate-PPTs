import os
import fitz  # PyMuPDF

def extract_images_from_pdf(pdf_path, output_folder):
    # 创建输出目录（如果不存在）
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 打开PDF文件
    pdf_document = fitz.open(pdf_path)
    print(f"开始处理 PDF 文件: {pdf_path}")
    
    # 遍历每一页
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        image_list = page.get_images(full=True)  # 获取当前页所有图像
        
        # 如果当前页没有图像则跳过
        if not image_list:
            continue
        
        print(f"正在处理第 {page_num + 1} 页，找到 {len(image_list)} 张图片")
        
        # 遍历当前页的每个图像
        for image_index, img in enumerate(image_list):
            xref = img[0]  # 图像对象的交叉引用编号
            base_image = pdf_document.extract_image(xref)
            
            # 获取图像字节数据和格式
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]  # 自动识别扩展名（如 png, jpeg 等）
            
            # 生成文件名
            filename = f"page_{page_num + 1}_img_{image_index + 1}.{image_ext}"
            file_path = os.path.join(output_folder, filename)
            
            # 保存图像文件
            with open(file_path, "wb") as image_file:
                image_file.write(image_bytes)
                print(f"已保存: {filename}")

    pdf_document.close()
    print(f"所有图片已保存到: {output_folder}")

if __name__ == "__main__":
    # 使用示例
    pdf_path = "your_paper.pdf"  # 替换为你的PDF路径
    output_folder = "./extracted_images"  # 输出目录
    
    extract_images_from_pdf(pdf_path, output_folder)