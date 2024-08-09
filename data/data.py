"""
Download the Caltech 101 dataset locally to the current directory. 
"""

import os
import torchvision.datasets as ds

def main():
    dataset = ds.Caltech101(
        root=os.path.dirname(os.path.realpath(__file__)),
        target_type='category',
        transform=None,
        download=True
    )

if __name__ == '__main__':
    main()