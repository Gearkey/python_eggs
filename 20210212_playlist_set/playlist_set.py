import os

def main():
    # 开始
    print('\n-- playlist_set v0.3b --\n')

    # 指定生成的文件格式，默认 m3u
    file_format = 'm3u'

    # 功能选择
    print('1，生成指定目录的播放列表')
    print('')
    go = input('选择需要的功能：')

    if go == '1': one_path(file_format)
    else: pass

# 业务模块 --------------------------

def one_path(file_format):
    path = input('操作路径：')
    path_out = input('输出路径：')
    path_prefix = input('前缀路径：')

    if file_format == 'm3u': print("\n文件已生成至：" + print_m3u(path, path_out, path_prefix))
    else: pass

# 功能模块 --------------------------

def print_m3u(path, path_out, path_prefix):
    path_out = os.path.join(path_out, 'playlist.m3u')
    
    m3u = open(path_out, "w")
    m3u.write('#EXTM3U\n')

    with os.scandir(path) as files:
        for file in files:
            m3u.write('#EXTINF:-1,\n')
            m3u.write(os.path.join(path_prefix, file.name) + '\n')
    
    m3u.close
    return path_out

if __name__ == '__main__':
    main()