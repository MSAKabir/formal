close all
clear all
clc;
k=imread('w3.jpg');
k2=k*.3;
imshow(k);
figure
imshow(k2);
imwrite(k2,'w3a.jpg');