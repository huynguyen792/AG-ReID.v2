# AG-ReID Person Re-Identification Toolkit Instructions

The following steps will guide you through the process of setting up the AG-ReID person re-identification toolkit:

1. Begin by extracting the downloaded data into the ``data`` folder.

2. Then, you can initialize the dataloader by executing the reader script. The command for this is:
```bash
python AG-ReIDReader.py --data_path /your/reid_data_root/path
```
   Replace `/your/reid_data_root/path` with the actual path to your re-identification data root directory.

The expected directory structure in `/your/reid_data_root/path` should be as follows:

```
└───[reid_data_root]
    ├───train_all
        ├───P0001T04041A0
            ├───P0001T04041A0C0F31.jpg
            ├───P0001T04041A0C0F61.jpg
            └───...
        └───...
    ├───gallery
        ├───P0000T02140A0
            ├───P0000T02140A0C0F31.jpg
            ├───P0000T02140A0C0F61.jpg
            └───...
        └───...
    ├───query
        ├───P0000T02140A0
            ├───P0000T02140A0C0F91.jpg
            ├───P0000T02140A0C0F121.jpg
            └───...
        └───...
    └───qut_attribute_v8.mat
```

Remember, the `reid_data_root` directory should contain separate sub-directories for training and testing bounding boxes, and for queries from different cameras.