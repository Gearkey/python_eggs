# Soft_renamer

软件批量重命名，指定工作目录，然后添加已分类好的文件来源和修改时间信息。

文件结构：

```
workspace
|- source1
|-- xxx.exe
|-- xxx2.exe
|- source2
|-- xxx.exe
|-- xxx2.exe
```

处理结果：

```
workspace
|- source1
|-- xxx_source1_20210803.exe
|-- xxx2_source1_20210803.exe
|- source2
|-- xxx_source2_20210803.exe
|-- xxx2_source2_20210803.exe
```

## 更新日志

```
v0.1-20210803：基础的文件来源和修改时间添加
```

