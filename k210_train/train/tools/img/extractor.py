"""
https://gitlab.com/makeblock-ai/ai-kit/-/blob/master/ai_kit/extractor.py
功能：通过视频 采集图片
"""

import cv2
import os
try:
    from file import make_dir
except ImportError:
    from .file import make_dir


def extract_images_from_video(
        file_path,
        save_dir,
        save_name_prefix='extract',
        start_index=0,
        force_replace=False):
    save_dir = make_dir(save_dir, force_replace)
    cap = cv2.VideoCapture(file_path)
    success, image = cap.read()
    count = start_index
    while success:
        file_name = f'{save_name_prefix}{count}.jpg'
        save_file_path = os.path.join(save_dir, file_name)
        cv2.imwrite(save_file_path, image)
        success, image = cap.read()
        count += 1
    print(f'extract {count} images')


if __name__ == '__main__':
    file_path = '/Users/catchzeng/Desktop/train.mp4'
    save_dir = '/Users/catchzeng/Desktop/train'
    extract_images_from_video(
        file_path, save_dir, save_name_prefix='ball', start_index=1, force_replace=True)
