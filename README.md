# fyuse_imageDownload
A simple Python code to download all images created by Fyuse on https://fyu.se

* You will need to go to your Fyuse profile webpage, 
    > e.g. https://fyu.se/u/sciit
    
    then open an inspector (source edit) in your browser to find out the link to your target Fyuse image squence, 
    > e.g. https://i.fyu.se/kqysvi4w01v7f0ou/7naymp0llj/frames_0.jpg 

    where 0 is the image index.

* Next step is copying 
    > https://i.fyu.se/kqysvi4w01v7f0ou/7naymp0llj/frames_0.jpg 

    to the Python code and replace the image index to {}.

* Final step is executing
    ```
    python fyuse_download.py
    ```
