#  DVC basic demo

## create the fresh annconda env 

```bash 
        $ conda create -n dvc python=3.6 -y 
        $ conda activate dvc 
```

## command in use commanly 

```bash 
        $ pip install dvc 
        $ git init
        $ dvc init  
```
- after initializing the 'DVC' , there will be two files created namely **".dvc"** , **".dvcignore"**


## how you can run the Operations Sequentially ?

- create the file dvc.yaml
- write the neccessary stages into it , their deps & outs ...
- run this file using command **'dvc repro'** 

```
        $ touch dvc.yaml 
             # file content 
                stages:
                        stage_01 :
                                cmd : python stage_01.py 
                                deps :
                                        - stage_01.py
                                outs :
                                        - Artifact01.txt

                                stage_02 :
                                        cmd : python stage_02.py 
                                        deps :
                                                - stage_02.py
                                                - Artifact01.txt
```


```bash 
          $ dvc repro   # to run the file (dvc.yaml )
          
          # if you run command twice it'll give you massage 
                # Stage 'stage_01' didn't change, skipping
                # Stage 'stage_02' didn't change, skipping
                # Data and pipelines are up to date.
(dvc) 

```
- it'll create File **dvc.lock** which keep info of operation history.