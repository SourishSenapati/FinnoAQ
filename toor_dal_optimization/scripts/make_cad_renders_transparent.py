import os
import numpy as np
from PIL import Image
from scipy import ndimage

DRAWINGS_DIR = 'toor_dal_optimization/portal/public/drawings'

TARGET_FILES = [
    'PLANT-15T_Joined_Iso_HumanView.png',
    'PLANT-15T_SolidWorks_3D_Iso.png',
    'TK-101_SolidWorks_3D_Iso.png',
    'CHU-100_SolidWorks_3D_Iso.png',
    'SC-101_SolidWorks_3D_Iso.png',
    'DR-101_SolidWorks_3D_Iso.png',
    'EV-101_SolidWorks_3D_Iso.png',
    'STR-100_SolidWorks_3D_Iso.png',
    'SK-100_SolidWorks_3D_Iso.png'
]

def make_transparent(input_path, output_path):
    img = Image.open(input_path).convert('RGBA')
    arr = np.array(img)
    rgb = arr[:, :, :3]
    
    # Background is pure or near pure white
    is_white = (rgb[:, :, 0] > 245) & (rgb[:, :, 1] > 245) & (rgb[:, :, 2] > 245)
    
    # Label connected components of white pixels starting from the perimeter
    labeled, num_features = ndimage.label(is_white)
    
    # Find labels touching any image border
    border_labels = set()
    border_labels.update(np.unique(labeled[0, :]))
    border_labels.update(np.unique(labeled[-1, :]))
    border_labels.update(np.unique(labeled[:, 0]))
    border_labels.update(np.unique(labeled[:, -1]))
    border_labels.discard(0) # 0 is non-white
    
    # Mask of external background
    bg_mask = np.isin(labeled, list(border_labels))
    
    # Create smooth alpha channel
    # 255 for foreground, 0 for external background
    alpha = np.ones(bg_mask.shape, dtype=np.uint8) * 255
    alpha[bg_mask] = 0
    
    # Smooth edges slightly to avoid harsh pixelation
    dist = ndimage.distance_transform_edt(alpha)
    smooth_alpha = np.clip(dist * 128, 0, 255).astype(np.uint8)
    smooth_alpha[bg_mask] = 0
    
    arr[:, :, 3] = smooth_alpha
    
    # Save transparent PNG
    out_img = Image.fromarray(arr)
    out_img.save(output_path, format='PNG')
    print(f"Saved: {output_path} (size: {out_img.size})")

def main():
    for f in TARGET_FILES:
        in_p = os.path.join(DRAWINGS_DIR, f)
        if os.path.exists(in_p):
            base_name, ext = os.path.splitext(f)
            out_p = os.path.join(DRAWINGS_DIR, f"{base_name}_transparent.png")
            make_transparent(in_p, out_p)

if __name__ == '__main__':
    main()

