#include<iostream>
#include<opencv2/opencv.hpp>

using namespace cv;
using namespace std;

int main()
{

	Mat image1, output_image, image1_gray;   //定义输入图像，输出图像，灰度图像
	image1 = imread("lena.png");  //读取图像；
	if (image1.empty())
	{
		cout << "读取错误" << endl;
		return -1;
	}

	cvtColor(image1, image1_gray, COLOR_BGR2GRAY);  //灰度化
	imshow(" image1_gray", image1_gray);   //显示灰度图像

	output_image = image1_gray.clone();
	for (int i = 0; i < image1_gray.rows; i++)
	{
		for (int j = 0; j < image1_gray.cols; j++)
		{
			output_image.at<uchar>(i, j) = 255 - image1_gray.at<uchar>(i, j);  //灰度反转
		}
	}
	imshow("output_image", output_image);  //显示反转图像


	waitKey(0);  //暂停，保持图像显示，等待按键结束
	return 0;
}